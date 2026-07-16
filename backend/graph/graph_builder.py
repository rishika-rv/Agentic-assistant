from langgraph.graph import StateGraph, START, END

from graph.state import GraphState
from graph.nodes import (router_node, chatbot_node, calculator_node, word_count_node, reverse_text_node)

builder = StateGraph(GraphState)

builder.add_node("router", router_node)
builder.add_node("chatbot", chatbot_node)
builder.add_node("calculator", calculator_node)
builder.add_node("word_count", word_count_node)
builder.add_node("reverse_text", reverse_text_node)

builder.add_edge(START, "router")

# Decide which node to execute

def route(state: GraphState):
    return state["tool"]


builder.add_conditional_edges(
    "router",
    route,
    {
        "calculator": "calculator",
        "word_count": "word_count",
        "reverse_text": "reverse_text",
        "chatbot": "chatbot",
    },
    )

# Every node ends the graph

builder.add_edge("calculator", END)
builder.add_edge("word_count", END)
builder.add_edge("reverse_text", END)
builder.add_edge("chatbot", END)

graph = builder.compile()