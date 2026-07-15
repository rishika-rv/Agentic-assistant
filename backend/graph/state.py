from typing import TypedDict
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    messages: list[BaseMessage]