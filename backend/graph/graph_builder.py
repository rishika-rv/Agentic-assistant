from langgraph.graph import StateGraph, START, END

from graph.state import GraphState
from graph.nodes import chatbot_node

builder = StateGraph(GraphState)

builder.add_node("chatbot", chatbot_node)

builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()