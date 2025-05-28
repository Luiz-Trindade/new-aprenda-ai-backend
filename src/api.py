from os import cpu_count
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from gemini_bot import *

app = FastAPI()

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/generate_topic_text/{topic}/{dificult}/")
async def generate_topic_text(topic: str, dificult: str):
    topic_text_response = topic_text(topic, dificult)
    return {"topic_text": topic_text_response}

@app.get("/api/generate_topic_quiz/{topic}/{dificult}/")
async def generate_topic_quiz(topic: str, dificult: str):
    topic_quiz_response = topic_quiz(topic, dificult)
    return {"topic_quiz": topic_quiz_response}

if __name__ == "__main__":
    uvicorn.run(
        "api:app", 
        host    = "0.0.0.0", 
        port    = 8100, 
        #reload  = True
        workers = cpu_count(),
        #ssl_certfile    = "/www/server/panel/vhost/cert/grupo-colab.tech/fullchain.pem",
        #ssl_keyfile     = "/www/server/panel/vhost/cert/grupo-colab.tech/privkey.pem"
    )
