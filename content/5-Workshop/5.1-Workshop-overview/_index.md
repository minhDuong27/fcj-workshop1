---
title : "Introduction"
date :  2025-12-01
weight : 1 
chapter : false
pre : " <b> 5.1. </b> "
---

# DevSecOps Pipeline Overview (GitLab → AWS)

### Pipeline goals:
- Automate the entire build process – security scanning – error notification.
- Detect bugs and security vulnerabilities early as soon as dev commits code.

Create a closed DevSecOps loop: Commit → Scan → Notify → Fix → Commit again.

### Flow summary:
1. Dev commits code to GitLab (main branch).
2. AWS CodePipeline receives events and triggers the pipeline.
3. CodeBuild runs Sonar Scanner to analyze the source code.
4. SonarQube on EC2 receives scan results from Scanner.
5. SonarQube sends Webhook → API Gateway → Lambda.
6. Lambda processes data → sends notification via SNS → dev email.
7. Dev receives bug report → Fix → Commit → go back to loop.

### The system ensures:
- Automate security testing.
- Improve source code quality.
- Reduce security risks and logic errors.

![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png)
