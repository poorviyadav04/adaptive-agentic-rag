# Adaptive Agentic RAG (LangGraph)

An **Adaptive Retrieval-Augmented Generation (RAG) system** built with **LangGraph and LangChain** that dynamically routes queries between **vector retrieval and web search**, while grading document relevance, hallucinations, and answer quality.

The system uses a **graph-based LLM workflow** where each step is implemented as a node responsible for a specific reasoning task.

This project demonstrates how modern RAG pipelines can use **agents, graders, and routing logic** to improve answer quality and reduce hallucinations.

---

# Project Overview

Traditional RAG pipelines retrieve documents and immediately generate an answer.

However, real-world queries require more robust reasoning:

* retrieved documents may be irrelevant
* answers may hallucinate
* additional external knowledge may be required

This project implements an **adaptive RAG architecture** where the system:

1. Retrieves documents from a vector store
2. Grades document relevance
3. Falls back to web search if needed
4. Generates answers using retrieved context
5. Evaluates hallucinations and answer quality

The workflow is orchestrated using **LangGraph**, enabling structured LLM reasoning.

---

# System Architecture

The pipeline is implemented as a **LangGraph state machine**.

```
User Query
    │
    ▼
Retrieve Documents (Vector Store)
    │
    ▼
Document Relevance Grader
    │
    ├── Relevant → Generate Answer
    │
    └── Not Relevant → Web Search
                       │
                       ▼
                 Generate Answer
                       │
                       ▼
              Hallucination Grader
                       │
                       ▼
                 Answer Grader
```

The system ensures that the generated response is grounded in reliable information.

---

# Key Features

## Agentic RAG Pipeline

The system is implemented as a **LangGraph workflow**, where each reasoning step is a node.

Nodes include:

* retrieve documents
* grade document relevance
* perform web search
* generate answers

---

## Adaptive Retrieval

The system dynamically decides whether to use:

* vector database retrieval
* web search

based on document relevance grading.

---

## Document Relevance Grading

An LLM-based grader evaluates retrieved documents to determine if they are useful for answering the query.

If documents are irrelevant, the pipeline automatically performs **web search**.

---

## Hallucination Detection

Generated answers are evaluated by an **LLM hallucination grader** to determine whether the response is grounded in retrieved context.

---

## Answer Quality Evaluation

A separate grading chain evaluates whether the final answer sufficiently addresses the user query.

---

## Web Search Integration

When vector retrieval fails, the system uses **Tavily search API** to fetch external information.

---

## Observability with LangSmith

The project integrates **LangSmith tracing** for monitoring and debugging agent execution.

LangSmith enables:

* execution trace visualization
* chain-level debugging
* latency analysis
* prompt inspection

---

# Project Structure

```
adaptive-agentic-rag
│
├── graph/
│   │
│   ├── chains/
│   │   ├── answer_grader.py
│   │   ├── generation.py
│   │   ├── hallucination_grader.py
│   │   ├── retrieval_grader.py
│   │   └── router.py
│   │
│   ├── nodes/
│   │   ├── generate.py
│   │   ├── grade_documents.py
│   │   ├── retrieve.py
│   │   └── web_search.py
│   │
│   ├── consts.py
│   ├── graph.py
│   └── state.py
│
├── ingestion.py
├── main.py
│
├── graph.png
├── image.png
│
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

# Data Ingestion

Documents are ingested using **LangChain loaders** and stored in a **Chroma vector database**.

Run ingestion:

```
python ingestion.py
```

This step:

* loads documents
* generates embeddings
* stores them in ChromaDB

---

# Running the Agent

After ingesting documents, run the LangGraph workflow:

```
python main.py
```

Example query:

```
What is LangGraph and how does it work?
```

---

# Example Pipeline Flow

1. User submits query
2. System retrieves documents from ChromaDB
3. LLM grades document relevance
4. If documents are irrelevant → perform web search
5. Generate answer using retrieved context
6. Evaluate hallucinations
7. Evaluate answer quality

---

# Tech Stack

### LLM Framework

* LangChain
* LangGraph

### Retrieval

* ChromaDB vector store
* LangChain document loaders

### Tools

* Tavily Search API

### Observability

* LangSmith tracing

### Language

* Python

### Dependency Management

* Poetry

---

# Concepts Demonstrated

This project demonstrates several modern AI system concepts:

* Adaptive RAG pipelines
* Agentic workflows with LangGraph
* LLM-based grading systems
* Hallucination detection
* Retrieval quality evaluation
* Tool-augmented LLM reasoning
* Observability with LangSmith

---

# Future Improvements

Possible extensions include:

* streaming responses
* hybrid retrieval strategies
* caching layer
* UI interface
* automated evaluation datasets

---

# License

MIT License
