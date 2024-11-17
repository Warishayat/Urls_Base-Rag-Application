import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.vectorstores import FAISS


load_dotenv()
urls = []
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, max_tokens=500)

st.title("Chatbot-Rag-Application")
st.header("Ask Me AnyThing About Given Urls")

st.text("Urls Preprocessing")
url=st.text_input("Enter url")
urls.append(url)

if urls:
    st.write(f"{urls} is uploaded successfully.")

    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs = text_splitter.split_documents(data)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstores = FAISS.from_documents(documents=docs,embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
    retriver = vectorstores.as_retriever(search_type='similarity',search_kwargs={'k':3})

    st.write("URLS Preprocessed successfully")

    question=st.text_input("Ask any Question About URLS?")

    result=st.button("Submit")

    if result:
        if question:
            system_prompt = """ 
            you are assistant for question answerig task.
            use the following peice to retrived context to answer.
            if you dont know the answer say that i dont have enough knowledge about the question.
            \n\n
            {context}
            """

            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", system_prompt),
                    ("human", "{input}"),
                ]
            )

            rag_chain =  create_retrieval_chain(
                retriever=retriver,
                combine_docs_chain = create_stuff_documents_chain(llm=llm,prompt=prompt)
            )

            result = rag_chain.invoke({"input": question})

            st.write(result['answer'])