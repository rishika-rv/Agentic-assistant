from graph.state import GraphState
from services.llm import llm


def chatbot_node(state: GraphState):

    response = llm.invoke(state["messages"])

    return {
        "messages": state["messages"] + [response]
    }