---
title: "Event 2"
date: 2025-11-17
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---


# Workshop Report: "DevOps on AWS"

### Event Objectives

- Get a clear understanding of DevOps culture, principles, and how it changes the way teams work  
- Learn how to build CI/CD pipelines using AWS DevOps services  
- Practice Infrastructure as Code with AWS CloudFormation and the AWS CDK  
- Explore container platforms on AWS: ECR, ECS, EKS, and App Runner  
- Set up monitoring and observability with Amazon CloudWatch and AWS X-Ray  
- See how DevOps practices are applied in real production environments  

### Event Details

- **Location**: AWS Vietnam Office  
- **Date & Time**: 8:30 AM – 5:00 PM, Monday, November 17, 2025  

### Speakers & Facilitators

**Instructors:**

- **Truong Quang Tinh** – AWS Community Builder  
  - DevOps culture and CI/CD fundamentals  
- **Van Hoang Kha** – AWS Community Builder  
  - Infrastructure as Code with CloudFormation  
- **Nguyen Khanh Phuc Thinh** – AWS Community Builder  
  - AWS CDK deep dive  
- **Le Huynh Nghiem** – AWS Community Builder  
  - Container services on AWS  
- **Huynh Hoang Long** – AWS Community Builder  
  - Monitoring and observability  
- **Pham Hoang Quy** – AWS Community Builder  
  - DevOps best practices and real-world stories  

**Facilitators:**

- **AWS Vietnam Team**  
- **AWS Community Builders Vietnam**  

---

### Event Agenda

#### 8:30 AM – 9:00 AM: Registration and Opening

- Check-in and informal networking  
- Welcome talk and overview of the workshop flow  
- Short introduction to key AWS DevOps services  

---

#### 9:00 AM – 10:30 AM: DevOps Culture and CI/CD Pipeline

**Speaker: Truong Quang Tinh**

- **DevOps Mindset** – shifting from “Dev vs Ops” to “one team”:
  - **Collaboration**: Dev and Ops work together instead of separately  
  - **Automation**: Let tools handle repetitive work so teams can focus on value  
  - **Continuous Improvement**: Use feedback to adjust and improve over time  
  - **Shared Ownership**: Quality, security, and reliability are everyone’s job  

- **DORA Metrics** – how to know if DevOps is working:
  - **Deployment Frequency** – how often you push changes live  
  - **Lead Time for Changes** – time from commit to production  
  - **Mean Time to Recovery (MTTR)** – how fast you recover from incidents  
  - **Change Failure Rate** – how many releases cause problems  

- **Core CI/CD Services on AWS**:
  - **AWS CodeCommit** – Git repositories hosted on AWS  
  - **AWS CodeBuild** – build and test automation service  
  - **AWS CodeDeploy** – roll out changes to EC2, Lambda, ECS, or on-prem servers  
  - **AWS CodePipeline** – main pipeline that ties all stages together  

- **Deployment Strategies**:
  - **Blue/Green** – switch traffic between two environments to reduce downtime  
  - **Canary** – release changes to a small portion of users first  
  - **Rolling** – update instances gradually so the service stays available  

- **Live Demo**:
  - Set up a basic CI/CD pipeline end-to-end using AWS DevOps tools  

---

#### 10:30 AM – 10:45 AM: Coffee Break

- Short break for coffee and networking  

---

#### 10:45 AM – 12:00 PM: Infrastructure as Code with CloudFormation

**Speaker: Van Hoang Kha**

- **Core Ideas of Infrastructure as Code (IaC)**:
  - **Version Control** – treat infrastructure like code stored in Git  
  - **Repeatability** – spin up the same environment again and again  
  - **Living Documentation** – templates describe what exists in the cloud  
  - **Pre-deployment Testing** – validate before roll-out  

- **CloudFormation Basics**:
  - **Templates** – YAML/JSON files that describe AWS resources  
  - **Stacks** – a group of resources created and managed together  
  - **Change Sets** – preview what will change before you apply it  
  - **Drift Detection** – detect manual changes that differ from the template  

- **Best Practices with CloudFormation**:
  - **Modular Design** – use nested stacks to reuse patterns  
  - **Parameters** – keep templates flexible with input values  
  - **Outputs** – expose useful values for other stacks or teams  
  - **Cross-Stack References** – connect multiple stacks cleanly  

- **Advanced Concepts**:
  - **Stack Policies** – prevent accidental changes to critical pieces  
  - **Rollback Triggers** – roll back when CloudWatch alarms are triggered  
  - **StackSets** – roll out stacks to multiple accounts/regions at once  

- **Live Demo**:
  - Deploy a simple multi-tier app using CloudFormation templates  

---

#### 12:00 PM – 1:00 PM: Lunch Break

- Lunch and informal discussion with speakers and participants  

---

#### 1:00 PM – 2:15 PM: AWS CDK Deep Dive

**Speaker: Nguyen Khanh Phuc Thinh**

- **What is AWS CDK?**
  - Infrastructure described with real programming languages  
  - Supports TypeScript, Python, Java, C#, Go, and more  
  - Different abstraction layers:  
    - L1 – direct CloudFormation mapping  
    - L2 – higher-level constructs  
    - L3 – ready-made patterns  

- **CDK Building Blocks**:
  - **Constructs** – reusable building units for cloud apps  
  - **Stacks** – deployment units made of constructs  
  - **Apps** – a collection of stacks deployable as one project  
  - **Synthesis** – CDK code → CloudFormation template  

- **CDK vs CloudFormation**:
  - **Imperative vs Declarative** – use loops, conditions, functions in CDK  
  - **Type Safety** – catch mistakes early via the compiler  
  - **IDE Support** – autocompletion and inline docs help productivity  
  - **Testing** – write tests for your infrastructure code  

- **CDK Good Practices**:
  - Use and share **construct libraries**  
  - Design stacks that are **environment-agnostic** when possible  
  - Keep **logical IDs** stable to avoid unnecessary replacements  
  - Use **context values** for per-environment configuration  

- **Live Demo**:
  - Build and deploy a small serverless app using AWS CDK  

---

#### 2:15 PM – 2:30 PM: Coffee Break

- Short break and more networking  

---

#### 2:30 PM – 3:45 PM: Container Services on AWS

**Speaker: Le Huynh Nghiem**

- **Container Basics**:
  - What containers are and why they’re popular  
  - Benefits: consistent environments, portability, resource efficiency  
  - Quick review of Docker concepts: images, containers, registries  

- **Amazon Elastic Container Registry (ECR)**:
  - Private container image registry managed by AWS  
  - Built-in **image scanning** for vulnerabilities  
  - **Lifecycle policies** to auto-delete old images  
  - Cross-region replication to speed up deployments globally  

- **Amazon Elastic Container Service (ECS)**:
  - AWS-native container orchestration service  
  - **Task Definitions** – recipe for running containers  
  - **Services** – define desired count and keep tasks running  
  - **Fargate** – run containers without managing servers  
  - **EC2 Launch Type** – full control of the underlying instances  

- **Amazon Elastic Kubernetes Service (EKS)**:
  - Managed control plane for Kubernetes clusters  
  - Use standard Kubernetes APIs and tools  
  - Flexible enough for complex microservice architectures  
  - Integration with AWS components like ALB, EBS, EFS  

- **AWS App Runner**:
  - Simplest way to go from source code or container image to a running service  
  - Handles scaling automatically  
  - Integrates with CI/CD flows  
  - Ideal for web apps and APIs that don’t need complex orchestration  

- **Choosing the Right Container Service**:
  - **ECS** – good default choice for AWS-focused teams  
  - **EKS** – for teams already familiar with Kubernetes  
  - **App Runner** – when speed and simplicity are top priority  

- **Live Demo**:
  - Deploy a container-based application to ECS and EKS  

---

#### 3:45 PM – 4:45 PM: Monitoring and Observability

**Speaker: Huynh Hoang Long**

- **Monitoring vs Observability**:
  - **Monitoring** – collecting metrics and checking if things are OK  
  - **Observability** – being able to understand internal behavior from external outputs  
  - Focus on the three pillars: **logs, metrics, traces**  

- **Amazon CloudWatch**:
  - **Metrics** – track CPU, memory (custom), and app metrics  
  - **Logs** – central place to store and search logs  
  - **Alarms** – trigger alerts or actions based on thresholds  
  - **Dashboards** – custom views for system health  
  - **Logs Insights** – query logs with a SQL-like syntax  
  - **Events** – react to changes in your AWS environment  

- **AWS X-Ray**:
  - **Distributed tracing** – follow a request across multiple services  
  - **Service map** – visual view of how services talk to each other  
  - **Trace analysis** – identify slow parts and bottlenecks  
  - **Error analysis** – pinpoint where failures happen  
  - Works with Lambda, ECS, EKS, API Gateway, and more  

- **Good Practices for Observability**:
  - Use **structured logging** (JSON or consistent formats)  
  - Add **custom metrics** for business-level KPIs  
  - Configure **alerts** before users notice issues  
  - Correlate logs, metrics, and traces for faster debugging  
  - Apply **retention policies** to balance visibility and cost  

- **Live Demo**:
  - Set up dashboards, alarms and tracing for a small microservices system  

---

#### 4:45 PM – 5:00 PM: DevOps Best Practices & Q&A

**Speaker: Pham Hoang Quy**

- **DevOps Best Practices**:
  - **Automate as much as possible**: tests, builds, deployments, checks  
  - **Fail fast and learn**: treat incidents as learning opportunities  
  - **Blameless postmortems**: focus on process, not on blaming people  
  - **Progressive delivery**: feature flags, canary, blue/green releases  
  - **Continuous learning**: DevOps is an ongoing improvement cycle  

- **Case Studies**:
  - **Startup** – use serverless and CI/CD to deliver features quickly  
  - **Enterprise** – multi-account setups with CloudFormation StackSets  
  - **E-commerce** – high-availability deployments using blue/green  

- **Q&A Session**:
  - Open discussion with participants about tools, culture, and real problems  

---

### Key Takeaways

#### DevOps Culture and Mindset

- DevOps is about people, collaboration, and shared goals, not just tools  
- Automation is key to reducing manual work and mistakes  
- DORA metrics give a concrete way to see how the team is improving  
- Continuous improvement is at the heart of DevOps  
- Quality and reliability are shared responsibilities across the team  

#### CI/CD Pipeline Automation

- CodeCommit, CodeBuild, CodeDeploy, and CodePipeline work well together  
- End-to-end automation improves speed and reduces human error  
- Multiple deployment patterns (blue/green, canary, rolling) support safer releases  
- CI/CD can integrate with both AWS-native and third-party services  
- A good pipeline becomes the backbone of the delivery process  

#### Infrastructure as Code

- CloudFormation templates provide a clear and repeatable infrastructure definition  
- CDK adds a more developer-friendly way to define the same resources  
- IaC improves consistency, traceability, and collaboration  
- Drift detection helps catch manual edits that break the IaC model  
- Choosing between CloudFormation and CDK depends on team skills and preference  

#### Container Services

- ECR secures and manages container images with scanning and policies  
- ECS is a strong default for many AWS-based container workloads  
- EKS is powerful for teams already invested in Kubernetes  
- App Runner is ideal when you want “code → service” with minimal steps  
- The right container platform depends on complexity, control, and team experience  

#### Monitoring and Observability

- CloudWatch and X-Ray provide a complete toolkit for visibility on AWS  
- Observability helps understand **why** something went wrong, not just **that** it did  
- Proactive alerts are essential for minimizing downtime  
- Logs, metrics, and traces together give a full picture of system health  
- Data from monitoring can guide performance tuning and cost optimizations  

#### DevOps Best Practices

- Automation + culture = effective DevOps, tools alone are not enough  
- Learning from incidents is more important than avoiding them at all costs  
- Progressive delivery reduces risk for every release  
- Regularly reviewing processes and metrics keeps the team moving forward  

---

### Applying to Work

- Start with a simple **CI/CD pipeline** using CodePipeline and expand from there  
- Migrate manual setups into **CloudFormation** or **CDK** for consistency  
- Gradually **containerize applications** and choose ECS/EKS/App Runner where appropriate  
- Strengthen **monitoring and observability** with CloudWatch dashboards and X-Ray  
- Encourage a **DevOps culture** of transparency, ownership, and continuous learning  
- Use **DORA metrics** to track improvement instead of gut feeling  
- Consider aiming for the **AWS DevOps Engineer** certification as a longer-term goal  

---

### Event Experience

The **“DevOps on AWS Workshop”** was a full-day, very packed but valuable experience. It covered not only the technical tools, but also the mindset and real-world practices behind DevOps.

#### Learning from AWS Experts

- The speakers provided both high-level concepts and concrete examples  
- Live demos made the theory easier to follow and remember  
- Real case studies helped connect the tools to realistic use cases  
- There was plenty of time to ask specific questions about real problems  

#### Hands-on Demonstrations

- Saw a complete CI/CD pipeline being assembled step by step  
- Watched how IaC with CloudFormation and CDK works in practice  
- Learned how to deploy containers on ECS and EKS  
- Understood what proper monitoring and tracing look like in a microservices setup  

#### Understanding DevOps in Practice

- DevOps was presented as a combination of **culture + process + tools**  
- DORA metrics provided a clear way to talk about performance and improvement  
- Observability was highlighted as a core requirement for modern systems  
- Examples of incident handling and postmortems were particularly useful  

#### Networking and Community

- Met many engineers who are on the same DevOps journey  
- Shared common struggles like legacy systems, manual processes, and resistance to change  
- Got connected to the AWS DevOps community for future events and learning  

#### Personal Takeaways

- Good DevOps requires both mindset change and technical skills  
- Automation frees teams from “busy work” and lets them focus on real problems  
- Having IaC and proper monitoring in place makes scaling much easier  
- AWS provides almost everything needed to implement DevOps end-to-end  

---

#### Next Steps

- Build or improve an internal CI/CD pipeline using the ideas from the workshop  
- Refactor existing infrastructure into CloudFormation/CDK where possible  
- Plan a gradual move towards containers for suitable workloads  
- Invest time in setting up meaningful dashboards and alerts  
- Keep learning from AWS documentation, workshops, and the community  

