import os
import pinecone
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

def ingestPDF(docPath):
    try:
        pinecone.init(
            api_key=os.environ.get('PINECONE_API_KEY'),
            environment=os.environ.get('PINECONE_API_ENV')
        )

        loader = TextLoader(f'static/{docPath}')
        document = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(document)
        embeddings = OpenAIEmbeddings()
        Pinecone.from_documents(document, embeddings, index_name=os.environ.get('PINECONE_INDEX_NAME'))
        return str(f'Loaded {len(texts)} to Pinecone')
    except Exception as e:
        return str(f'Error: {e}')
    