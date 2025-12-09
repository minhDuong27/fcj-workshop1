---
title: "Using Large Language Models on Amazon Bedrock for Multi-step Task Execution"
date: 2025-10-16
weight: 1
chapter: false
pre: "<b> 3.1. </b>"
---

This article explains how to use **Large Language Models (LLMs)** on **Amazon Bedrock** to carry out analytical tasks that require multi-step reasoning and external APIs. The goal is to convert complex questions into a structured **Plan → Execute** workflow that is predictable and scalable.

---

## 1. Background

Business analytics questions are typically complex, such as:

- “What is the average hospital stay for patients with a specific condition across hospitals?”
- “How do prescription trends for a particular medication differ across regions?”

Traditional solutions require BI experts and data engineers.  
With **LLMs + tools**, we can automate and accelerate these workflows.

---

## 2. Tools in the LLM Context

Tools are external capabilities the LLM can call, such as:

- APIs for real-time data  
- Functions for computation or data processing  
- Filtering, grouping, or joining data  

Using tools allows the LLM to produce **accurate, contextual, and actionable** outputs.

---

## 3. Example Interaction

User: “Who is the patient with the lowest number of vaccines?”  
AI: “The patient is Sharleen176 Kulas532 with 1 vaccine.”

Steps performed:

1. Retrieve patient data  
2. Retrieve immunization data  
3. Group by patient  
4. Count vaccines  
5. Sort ascending  
6. Select top result  
7. Join with patient details  

---

## 4. Dataset & Setup

The system uses the **Synthetic Patient Generation Dataset**, containing multiple healthcare tables.

Setup involves downloading, extracting, and placing data in the project folder.

---

## 5. Solution Architecture: Plan → Execute

Two-phase workflow:

- **Plan**: LLM generates a step-by-step plan  
- **Execute**: Engine executes each step  

Flow:

User → LLM Plan → JSON Plan → Execution Engine → Answer

---

## 6. Planning Phase

### Why Planning?

The LLM:

- Performs step-by-step reasoning  
- Produces a structured workflow  
- Avoids hallucinated API calls  

Tools are provided as **function signatures** the LLM can use.

### RAG for Tool Selection

RAG helps show the LLM only relevant tools, improving accuracy and reducing complexity.

### Example Plan

For the query “Find the patient with the fewest vaccines,” the plan includes:

- Retrieve patients  
- Retrieve immunizations  
- Group by patient  
- Count  
- Sort  
- Limit  
- Join  
- Select  

---

## 7. Execution Phase

The engine takes the JSON plan and:

- Parses it  
- Executes each function  
- Stores intermediate results  
- Returns the final answer  

The LLM then frames the output into a natural-language response.

---

## 8. Error Handling

Possible failures:

- Empty or missing data  
- Invalid parameters  
- Type mismatches  

Engine responsibilities:

- Validate inputs  
- Validate outputs  
- Return meaningful errors  

The LLM may regenerate a better plan automatically.

---

## 9. Summary

We explored:

- How LLMs use APIs to answer complex questions  
- The Plan → Execute architecture  
- The role of RAG and function signatures  
- Error handling in execution  

LLMs can now act as **orchestration brains** for analytical workflows.

---

## 10. Future Improvements

Extensions include:

- More analytical questions  
- Additional tool signatures  
- A web UI for question input, plan visualization, and execution logs  

This makes the project both academically strong and practically relevant.
