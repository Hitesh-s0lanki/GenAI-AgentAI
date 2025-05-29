from typing import Annotated
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")

### Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

model = ChatOpenAI()

def make_default_graph():
    ## Creating the Graph
    graph_workflow = StateGraph(State)

    ## Defining the Node
    def call_model(state):
        return {"messages":[model.invoke(state["messages"])]}
    
    ## Adding the Node
    graph_workflow.add_node("agent", call_model)

    ##  Add the edge 
    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_edge("agent", END)

    ## Compiling the graph
    agent = graph_workflow.compile()

    ## Returing the Agent
    return agent

def make_alternative_graph():
    """Make a tool-calling agent"""

    @tool
    def add(a: int, b: int) -> int:
        """
        Adds a and b
        
        Args:
            a: first int
            b: first int
        """
        return a + b
    
    ## Creating the Tool Node
    tool_node = ToolNode([add])

    ## Binding the tool
    model_with_tools = model.bind_tools([add])

    ## Defining the Node
    def call_model(state):
        return {"messages":[model_with_tools.invoke(state["messages"])]}
    
    ## Creating the Graph
    graph_workflow = StateGraph(State)
    
    ## Adding the Node
    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_node("tools", tool_node)

    ##  Add the edge 
    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_edge("tools", "agent")
    graph_workflow.add_conditional_edges("agent", tools_condition)

    ## Compiling the graph
    agent = graph_workflow.compile()

    ## Returing the Agent
    return agent


agent = make_alternative_graph()