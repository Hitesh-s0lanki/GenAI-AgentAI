from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

generic_template = "Translate the following into {langauge}"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])

parser = StrOutputParser()

chain = prompt | model | parser

## App definition
app = FastAPI(title="Langchain Serve", version="1.0")

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)