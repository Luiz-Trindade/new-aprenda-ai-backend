import os
from dotenv import load_dotenv
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from gemini_prompts import *
from random import choice

load_dotenv()
api_keys = os.getenv("GOOGLE_API_KEYS", "").split(",")
models  = ["gemini-2.0-flash-lite", "gemini-2.0-flash", "gemini-2.0-flash-thinking-exp-01-21"]

def topic_text(topic: str, dificult: str):
    llm = ChatGoogleGenerativeAI(
        model           = choice(models),
        google_api_key  = choice(api_keys)
    )

    # Cria um template de prompt
    prompt = ChatPromptTemplate.from_template(topic_text_prompt)

    # Define a Chain usando pipes (|) para encadear os componentes
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "topic"     : topic,
        "dificult"  : dificult
    })

    # Exibe a resposta
    return response.replace("*", "")

def topic_quiz(topic: str, dificult: str):
    llm = ChatGoogleGenerativeAI(
        model           = choice(models),
        google_api_key  = choice(api_keys)
    )

    # Cria um template de prompt
    prompt = ChatPromptTemplate.from_template(topic_quiz_prompt)

    # Define a Chain usando pipes (|) para encadear os componentes
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "topic"     : topic,
        "dificult"  : dificult
    })

    # Exibe a resposta
    return response.replace("*", "")