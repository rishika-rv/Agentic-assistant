from fastapi import FastAPI
from services.llm import llm
from graph.graph_builder import graph
from langchain_core.messages import HumanMessage

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Office Assistant is running"}


@app.get("/test")
def test_llm():
    response = graph.invoke({"messages": [HumanMessage(content="Say hello in one sentence.")]})
    return {"response": response["messages"][-1].content}