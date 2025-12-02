---
title: "Blog 1"
date: 2025-10-16
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---


# Enabling customers to deliver production-ready AI agents at scale

*by Swami Sivasubramanian on 16 JUL 2025 in Amazon Bedrock, Amazon Connect, Amazon Nova, Amazon Q, Amazon Simple Storage Service (S3), Announcements, AWS Inferentia, AWS Trainium, AWS Transform, Featured, Thought Leadership*

AI agents are poised to have an impact as transformative as the internet itself, enabling automation, solving complex problems, and driving innovation. However, bringing AI agents into production at scale requires more than just training large models—it demands an architecture that ensures **security, reliability, scalability, and flexibility**.

AWS addresses this challenge with a **microservices-based** architecture: each agent capability (memory, identity, observability, tool access, customization) is encapsulated as a small, independent service, loosely coupled via a hub. This decomposition improves agility, makes it easier to add or replace components, and helps organizations focus on delivering business value instead of building infrastructure from scratch.

---

## Architecture Guidance

Compared to monolithic approaches, AWS decomposes agent functionality into multiple microservices:

**AgentCore**: the serverless runtime that orchestrates agents.

**Functional services**: memory, identity, observability, gateway, code interpreter.

**Model customization service**: Amazon Nova fine-tuning microservice.

This design allows customers to freely choose models, integrate existing data sources, and connect seamlessly with open-source frameworks.



---

## Technology Choices and Communication Scope

| Communication scope                       | Technologies                                                                            |
| ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| Within a single microservice              | AWS Lambda, Step Functions                                                                 |
| Between microservices in one agent        | Amazon SNS, AWS CloudFormation cross-stack references                                      |
| Between services/agent                    | Amazon EventBridge, API Gateway, AWS Cloud Map                                             |

---

## The Pub/Sub Hub

The **pub/sub hub** pattern is central to AWS’s approach:

- Each microservice interacts only with the hub, not directly with other microservices.

- Results, errors, or intermediate outputs are pushed back into the hub for further processing.

- Benefits: reduces synchronous calls, scales easily, keeps components loosely coupled.

-  Drawback: requires monitoring and coordination to prevent misrouted or duplicate messages.

---

## Core Microservice

The foundation of the solution, providing the data and communication layer:

- **Amazon S3** for data and artifacts.

- **Amazon DynamoDB** for metadata and catalog.

- **AWS Lambda** for consistent writes and runtime logic.

- **Amazon SNS** Topic as the central hub.

This ensures all writes to the data lake and catalog are controlled and consistent.

---

## Front Door Microservice

The primary entry point for external requests:

- Amazon API Gateway provides a REST interface.

- Amazon Cognito (OIDC) manages authentication and authorization.

- Deduplication mechanism built with DynamoDB, avoiding SNS FIFO limitations and enabling proactive duplicate detection.

---

## Processing Microservices

Agents often require specialized tools such as browsing, code execution, or search. These are implemented as microservices:

- Lambda triggers subscribe to the hub and filter messages.

- Step Functions orchestrate pipelines (e.g., preprocessing, model invocation).

- Lambda functions execute specific parsing or transformation logic.

- Results or errors are returned to the hub for downstream services.

---

## Model Customization Microservice (Nova)

Fine-tuning is handled as a dedicated microservice:

- Supports both full fine-tuning and parameter-efficient techniques.

- Methods include SFT, DPO, RLHF, CPT, and Knowledge Distillation.

- Runs independently, so updates or retraining do not disrupt the overall runtime.

---

## New Features in the Solution

### 1. Amazon Bedrock AgentCore

- Serverless runtime for agents.

- Session isolation and observability.

- Integrates with open-source frameworks.

### 2. Expanded Tooling Support

- Microservices for memory, identity, gateway, browser, and interpreter.

- Each is modular and replaceable.

### 3. Customer Adoption

- Enterprises like Itaú Unibanco, Innovaccer, Boomi, Box, and Epsilon are already adopting this architecture for scalable production deployment.


```yaml
Outputs:
  AgentCoreTopic:
    Value: !Ref AgentCoreTopic
    Export:
      Name: !Sub ${AWS::StackName}-AgentCoreTopic

  AgentMemoryTable:
    Value: !Ref AgentMemoryTable
    Export:
      Name: !Sub ${AWS::StackName}-AgentMemoryTable

  NovaCustomizationJob:
    Value: !Ref NovaCustomizationJob
    Export:
      Name: !Sub ${AWS::StackName}-NovaCustomizationJob

