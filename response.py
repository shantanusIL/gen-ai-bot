import os
import openai
# from langchain.llms import AzureOpenAI
# import pinecone
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.prompts import PromptTemplate
# from langchain.vectorstores import Pinecone
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv(), override=True)


# def get_llm_response(query):
#     # llmturbo = AzureOpenAI(
#     #     temperature=0,
#     #     openai_api_base=os.environ.get('OPENAI_API_BASE'),
#     #     openai_api_key=os.environ.get('OPENAI_API_KEY'),
#     #     deployment_name=os.environ.get('DEPLOYMENT_NAME')
#     # )
#     llmturbo = AzureOpenAI(
#     # verbose=True,
#     temperature=0,
#     top_p=0,
#     openai_api_base=os.environ.get('OPENAI_API_BASE'),
#     openai_api_key=os.environ.get('OPENAI_API_KEY'),
#     # model_kwargs={'openai_api_version':'2023-03-15-preview'},
#     deployment_name='gpt-35-turbo'
#     )

#     pinecone.init(
#         api_key=os.environ.get('PINECONE_API_KEY'),
#         environment=os.environ.get('PINECONE_API_ENV')
#     )

#     embeddings = OpenAIEmbeddings(
#         deployment=os.environ.get('OPENAI_DEPLOYMENT'), 
#         chunk_size=1,
#         openai_api_key=os.environ.get('OPENAI_API_KEY'),
#         openai_api_base=os.environ.get('OPENAI_API_BASE'),
#         openai_api_type=os.environ.get('OPENAI_API_TYPE'),
#         openai_api_version=os.environ.get('OPENAI_API_VERSION')
#     )

#     docsearch = Pinecone.from_existing_index(
#         embedding=embeddings,
#         index_name='my-first-index',
#     )

#     # CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template("""Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
#     #     Chat History:
#     #     {chat_history}
#     #     Follow Up Input: {question}
#     #     Standalone question:"""
#     #                                                         )

#     qa = ConversationalRetrievalChain.from_llm(llm=llmturbo,
#                                                retriever=docsearch.as_retriever(),
#                                             #    condense_question_prompt=CONDENSE_QUESTION_PROMPT,
#                                                return_source_documents=True,
#                                                verbose=False)

#     result = qa({"question": query, "chat_history": []})

#     resp = result["answer"]
    
#     return {
#         "query": query,
#         "response": resp
#     }

#openai.api_key=os.environ.get('OPENAI_API_KEY_TUNED')
openai.api_key='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'
def get_llm_responseTuned(query):
    print('@@@ Query : '+query)
    prompt = query + '\n\n###\n\n'
    responseTuned = openai.Completion.create(
        engine="ft:davinci-002:personal::7spzBHCf",
        prompt= prompt,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n","###"]
    )
    resp=responseTuned['choices'][0]['text']
    return {
        "query": query,
        "response": resp
    }