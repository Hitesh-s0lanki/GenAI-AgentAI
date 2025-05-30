# Agentic AI Architectures

This repository demonstrates multiple Agentic AI patterns and architectures built on top of foundational tools like LangChain, LangGraph, and OpenAI. Specifically, it includes:

- **ReAct Agent**: Leveraging reasoning and action for dynamic tool use with LangChain.
- **PromptChain**: Chaining prompts and intermediate steps for complex workflows.
- **Agentic RAG**: Retrieval-Augmented Generation with agentic control flows.
- **Corrective Agentic RAG**: Enhanced RAG with document grading and corrective feedback loops.
- **Adaptive RAG**: An adaptive retrieval pipeline that rewrites queries and invokes web search when needed.
- **LangGraph Workflows**: Visualizing agent flows and integrating vector stores, web search, and custom tools.

---

## Architecture Overview

Agentic AI combines traditional language model prompting with autonomous decision-making and tool usage. This repo explores several patterns:

- **ReAct Agent**: Integrates chain-of-thought reasoning with action calls to tools (e.g., vectorstore, web search).
- **PromptChain**: Splits complex tasks into a sequence of specialized prompts with structured intermediate outputs.
- **Agentic RAG**: Uses a vector retriever to fetch documents, then an agent orchestrates reasoning to form answers.
- **Corrective Agentic RAG**: Adds a grading step where retrieved documents are evaluated; if none are relevant, a corrective query rewrite triggers web search.
- **Adaptive RAG**: Extends corrective RAG by dynamically choosing retrieval or web search based on a document grading node; supports fallbacks and query transforms.
- **LangGraph**: Provides visual representations of these flows, enabling rapid inspection and debugging of agent decision branches.

---

## Prerequisites

- Python 3.10+
- OpenAI API Key
- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langgraph-ai/langgraph) (for graph visualizations)
- Other optional dependencies: `faiss-cpu` or `weaviate-client`, `requests` for web search

---

## Installation

```bash
# Clone this repo
git clone https://github.com/Hitesh-s0lanki/GenAI-AgentAI.git
cd GenAI-AgentAI

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install core dependencies
pip install -r requirements.txt
```

Set your OpenAI key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## Agent Implementations

### ReAct Agent

- Combines reasoning (Thoughts) and actions (e.g., vector store retrieval, API calls).
- Implemented via LangChain's `AgentExecutor` with `Tool` definitions.

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

tools = [
    Tool(name="search", func=web_search, description="Use for online queries."),
    Tool(name="vector_retrieval", func=vector_retrieve, description="Fetch docs.")
]

agent = initialize_agent(tools, OpenAI(temperature=0), agent="react")
response = agent.run("What is the latest news on Agentic AI?")
```

### PromptChain

- Orchestrates a sequence of prompts with structured outputs.
- Useful for multi-step workflows like summarization followed by QA.

```python
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

summary_prompt = PromptTemplate(input_variables=["doc"], template="Summarize: {doc}")
qa_prompt = PromptTemplate(input_variables=["summary","question"], template="Based on the summary, answer: {question}")

chain = SequentialChain(chains=[
    LLMChain(llm=OpenAI(), prompt=summary_prompt),
    LLMChain(llm=OpenAI(), prompt=qa_prompt)
], input_variables=["doc","question"], output_variables=["answer"])

result = chain.run({"doc": text, "question": "..."})
```

### Agentic RAG

- Retrieval-augmented generation pipeline wrapped by an agent.
- Flow: `__start__` → `agent` → vector `retrieve` → `generate` → `__end__`.

### Corrective Agentic RAG

- Adds a `grade_documents` step after retrieval.
- If no documents are relevant, uses `transform_query` to rewrite and triggers `web_search`.
- Otherwise proceeds to `generate`.

### Adaptive RAG

- Combines both vector retrieval and web search in a unified graph.
- Dynamically branches based on document relevance and supported content types.

---

## LangGraph Visualizations

This repo includes `.lg.json` graph definitions for each agent, viewable in the [LangGraph Playground](https://play.langgraph.ai):

- `graphs/agentic_rag.lg.json`
- `graphs/corrective_rag.lg.json`
- `graphs/adaptive_rag.lg.json`

Open these files to explore interactive flowcharts of decision paths and tool integrations.

---

## Usage Examples

1. **Agentic RAG Demo**

   ```bash
   python examples/agentic_rag_demo.py
   ```

2. **Corrective Agentic RAG**

   ```bash
   python examples/corrective_rag_demo.py
   ```

3. **Adaptive RAG with Fallback**

   ```bash
   python examples/adaptive_rag_demo.py
   ```

Results will showcase how each architecture handles missing context, irrelevant documents, and dynamic query rewrites.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with:

- New agent patterns or improvements.
- Additional tool integrations (e.g., search engines, custom APIs).
- Bug fixes and performance optimizations.
