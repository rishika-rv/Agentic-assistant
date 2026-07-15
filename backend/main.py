from fastapi import FastAPI
from services.llm import llm

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Office Assistant is running"}


@app.get("/test")
def test_llm():
    response = llm.invoke("Say hello in one sentence.")
    return {"response": response.content}