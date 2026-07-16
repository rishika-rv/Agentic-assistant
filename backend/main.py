from fastapi import FastAPI
from services.llm import llm
from graph.graph_builder import graph
from langchain_core.messages import HumanMessage
from fastapi import Query
app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Office Assistant is running"}


# @app.get("/test")
# def test_llm():
#     response = graph.invoke({"messages": [HumanMessage(content=query)]})
#     return {"response": response["messages"][-1].content}


@app.get("/chat")

def chat(query: str = Query(...)):

    response = graph.invoke({

        "messages": [HumanMessage(content=query)]

    })

    return {
        "tool_used": response["tool"],

        "response": response["messages"][-1].content

    }