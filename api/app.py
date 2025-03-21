from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
# from langchain_community.llsm import Ollama
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"

)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"

# )
# model=ChatOpenAI()

##Groq llama3
llm=ChatGroq(model="llama-3.3-70b-versatile", temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"))
llmDeep=ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"))

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words.")

add_routes(
    app,
    prompt1|llmDeep,
    path="/essay"

)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)