---
title: "Event 1"
date: 2025-11-15
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---



# Workshop Report: "AI/ML/GenAI on AWS"

### Workshop Objectives

- Gain an overview of the AI/ML landscape and how AWS is adopted in Vietnam  
- Understand the full ML workflow using Amazon SageMaker  
- Explore Generative AI capabilities through Amazon Bedrock  
- Practice prompt engineering and RAG (Retrieval-Augmented Generation)  
- Learn how to build practical AI/ML solutions using AWS services  

### Event Information

- **Location:** AWS Vietnam Office  
- **Time:** 8:30 AM – 12:00 PM, Saturday, November 15, 2025  

### Speakers & Organizing Team

**Instructors:**

- **Lâm Tuấn Kiệt** – Senior DevOps Engineer, FPT Software  
  - Presented the SageMaker overview and general AWS ML services  
- **Đinh Lê Hoàng Anh** – Cloud Engineer Trainee, FCAJ, Swinburne University of Technology  
  - Covered Amazon Bedrock and AWS AI/ML service ecosystem  
- **Danh Hoàng Hiếu Nghị** – Fresher AI Engineer, Renova Cloud  
  - Demonstrated Bedrock Agent Core and guided the hands-on practice  

**Coordinators:**

- AWS Vietnam Community Team  
- FCJ (First Cloud Journey) Program Leads  

---

### Agenda Overview

#### 8:30 – 9:00 AM: Registration & Kickoff

- Participant check-in and early networking  
- Introduction to the workshop structure and expected outcomes  
- Ice-breaker session  
- A quick look at the AI/ML market and adoption trends in Vietnam  

---

#### 9:00 – 10:30 AM: AWS AI/ML Overview – Deep Dive into Amazon SageMaker

**Amazon SageMaker – The End-to-End ML Platform**

- **Data Preparation & Labeling:**
  - Data Wrangler for cleaning and transforming datasets  
  - Ground Truth for labeling and annotation  
  - Feature Store for centralizing and reusing features  

- **Training, Tuning & Deployment:**
  - Use built-in algorithms or bring your own training scripts  
  - Run hyperparameter tuning jobs  
  - Deploy models via real-time, batch, or serverless inference  
  - Experiment with A/B testing models and multi-model endpoints  

- **Built-in MLOps Capabilities:**
  - SageMaker Pipelines to automate ML workflows  
  - Model Registry for tracking versions and governance  
  - Model Monitor to detect drift and quality issues  
  - CI/CD integration for continuous deployment  

- **Live Demo – SageMaker Studio:**
  - Launch a notebook instance  
  - Train a sample ML model  
  - Deploy an endpoint and send test requests  

---

#### 10:30 – 10:45 AM: Coffee Break

- Short break for refreshments  
- Casual Q&A with AWS engineers  

---

#### 10:45 AM – 12:00 PM: Generative AI with Amazon Bedrock & AWS AI/ML Services

**AWS AI/ML Services Overview**

- **Rekognition** – Image/video analysis  
- **Translate** – Neural machine translation  
- **Textract** – Document text extraction  
- **Transcribe** – Speech-to-text  
- **Polly** – Natural-sounding text-to-speech  
- **Comprehend** – NLP and text analytics  
- **Kendra** – Intelligent search engine  
- **Lookout** – Industrial anomaly detection  
- **Personalize** – ML-powered recommendations  

---

**Foundation Models: Claude, Llama, Titan**

- **Model Selection Insights:**
  - *Claude*: Strong in reasoning-heavy conversation tasks  
  - *Llama*: Good for customization, open-source flexibility  
  - *Titan*: Amazon-native, cost-effective, integrated with AWS  
  - How to choose depending on use case  

---

**Prompt Engineering Essentials**

- **Core Prompting Techniques:**
  - Provide clear instructions and meaningful context  
  - Use few-shot examples  
  - Apply chain-of-thought for complex logic  
  - Use role-based prompting to guide model behavior  

- **Advanced Prompting:**
  - Tuning temperature and token limits  
  - Knowing when to use system vs user prompts  
  - Template-based prompting for reusability  

---

**Retrieval-Augmented Generation (RAG)**

- **RAG Architecture:**
  - Embeddings + vector search  
  - Semantic retrieval before generating answers  
  - Feeding retrieved context back into prompts  

- **Knowledge Base Integration:**
  - Bedrock Knowledge Bases  
  - Store documents in **Amazon S3**  
  - Connect to data sources (S3, DBs, external APIs)  
  - Best practices for chunking and metadata  
  - Set correct bucket policies for secure access  

---

**Amazon Bedrock Agent Core**

- **Building Autonomous Agents:**
  - Multi-step task planning and orchestration  
  - Action groups for calling APIs  
  - Persistent memory for context retention  

- **Tool Integration with Lambda:**
  - Lambda as an execution engine for custom logic  
  - Real-time data processing  
  - Querying databases or external systems  
  - Serverless approach → simplified scaling and maintenance  

---

**Guardrails for Safe AI**

- Content filtering and moderation  
- PII detection and redaction  
- Topic restrictions and safety rules  
- Custom guardrails for enterprise policies  

---

**Live Demo – Creating a GenAI Chatbot with Bedrock**

- Enabling foundation model access  
- Designing prompts for a basic chatbot  
- Adding RAG with Knowledge Bases  
- Applying guardrails to control responses  
- Testing and fine-tuning the bot  

---

### Key Insights

#### From Amazon SageMaker

- A complete platform that covers the entire ML lifecycle  
- Well-integrated MLOps tools  
- Easy scaling from experimentation to production  
- Flexible pricing models to control cost  

#### From Amazon Bedrock

- Variety of foundation models readily available  
- Prompt engineering plays a major role in result quality  
- RAG helps integrate enterprise knowledge effectively  
- Guardrails are essential for safe deployment  
- Agent Core enables multi-step intelligent workflows  

#### Practical Lessons

- Start with the business problem, not the tool  
- Prototype quickly using SageMaker Studio  
- Use foundation models before investing in custom training  
- Guardrails ensure safety and compliance  
- Always monitor performance and optimize workloads  

---

### Applying the Knowledge

- Experiment in **SageMaker Studio** using small datasets  
- Build a **RAG-based chatbot** using Bedrock + S3  
- Practice prompt engineering with different models  
- Automate ML pipelines with **SageMaker Pipelines**  
- Try building simple **Bedrock Agents** for internal workflows  
- Implement guardrails before deploying any AI app  
- Share learnings with teammates to improve team-wide standards  

---

### Personal Experience

Attending the **“AI/ML/GenAI on AWS Workshop”** at the AWS Vietnam Office was a hands-on and insightful experience. The mix of explanations, demos, and real-world examples made the content easier to understand.

#### Learning from AWS Experts

- Clear explanations on SageMaker’s end-to-end workflow  
- Solid demos of Bedrock and real GenAI applications  
- Many Vietnam-based use cases provided good context  
- Practical advice on choosing the right AWS tools  

#### Hands-on Demonstrations

- Observed the full ML process: data → training → deployment  
- Learned how Bedrock simplifies building GenAI applications  
- Applied prompt engineering tricks in real examples  
- Understood how RAG makes LLMs more accurate with enterprise data  
- Saw how Agents organize multi-step tasks  

#### Understanding AI/ML Trends

- Differences between traditional ML and GenAI became clearer  
- Better idea of when to pick SageMaker vs Bedrock  
- Understood the importance of proper MLOps for production systems  

#### Networking

- Met many developers and data enthusiasts exploring AWS AI/ML  
- Exchanged experiences about real-world implementation challenges  
- Built new connections with AWS community members  

#### Important Takeaways

- Foundation models significantly reduce development effort  
- Good prompts dramatically improve model output  
- RAG is essential for knowledge-heavy chatbot applications  
- Guardrails are not optional—they are required for safe AI  
- SageMaker is ideal for long-term, scalable ML projects  

---

### Next Steps

- Continue exploring SageMaker Studio hands-on  
- Build a small RAG proof-of-concept using Bedrock  
- Practice prompt engineering with multiple foundation models  
- Experiment with Bedrock Agents for automation workflows  
- Learn more about MLOps and monitoring practices  
- Engage with the AWS AI/ML community for ongoing learning  

#### Event Pictures

![AI/ML Workshop](/images/4-EventParticipated/images/1.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/2.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/3.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/4.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/5.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/6.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/7.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/8.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/9.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/10.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/11.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/12.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/13.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/14.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/15.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/16.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/17.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/18.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/19.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/20.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/21.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/22.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/23.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/24.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/25.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/26.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/27.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/28.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/29.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/30.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/31.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/32.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/33.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/34.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/35.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/36.jpg)

> Overall, this workshop provided a comprehensive introduction to AWS AI/ML services, from traditional machine learning with SageMaker to cutting-edge Generative AI with Bedrock. The hands-on demonstrations and expert guidance made complex concepts accessible and immediately applicable. The key takeaway is that AWS provides a complete ecosystem for building, deploying, and scaling AI/ML applications, making it easier than ever to bring AI innovations to production.
