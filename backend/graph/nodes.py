from graph.state import GraphState
from services.llm import llm
from langchain_core.messages import AIMessage
from tools.calculator import calculator
from tools.word_count import word_count
from tools.reverse_text import reverse_text


def chatbot_node(state: GraphState):

    response = llm.invoke(state["messages"])

    return {
        "messages": state["messages"] + [response]
    }

def calculator_node(state: GraphState):
    query = state["messages"][-1].content
    result = calculator(query)
    return {
        "messages": state["messages"] + [AIMessage(content=str(result))]
    }

def word_count_node(state: GraphState):
    query = state["messages"][-1].content
    result = word_count(query)
    return {
        "messages": state["messages"] + [AIMessage(content=str(result))]
    }

def reverse_text_node(state: GraphState):
    query = state["messages"][-1].content
    result = reverse_text(query)
    return {
        "messages": state["messages"] + [AIMessage(content=str(result)) ]
    }

def router_node(state: GraphState):
    query = state["messages"][-1].content.lower()

    if "calculate" in query or any(op in query for op in ["+", "-", "*", "/"]):
        return {"tool": "calculator"}

    elif "count words" in query:
        return {"tool": "word_count"}

    elif "reverse" in query:
        return {"tool": "reverse_text"}

    else:
        return {"tool": "chatbot"}