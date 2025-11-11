---
title: "Proposal"
date: 2025-10-11
weight: 2
chapter: false
pre: " <b> 2. </b> "
---


# AWS Security Scan Project – Project Plan  
## [Team DevSecOps FCJ] – [FPT University / Internship Program] – [AWS Security Scan Project]
Date: 2025-10-11
### TABLE OF CONTENTS
1.BACKGROUND AND MOTIVATION
 1.1 EXECUTIVE SUMMARY
 1.2 PROJECT SUCCESS CRITERIA
 1.3 ASSUMPTIONS

2.SOLUTION ARCHITECTURE / ARCHITECTURAL DIAGRAM
 2.1 TECHNICAL ARCHITECTURE DIAGRAM
 2.2 TECHNICAL PLAN
 2.3 PROJECT PLAN
 2.4 SECURITY CONSIDERATIONS

3.ACTIVITIES AND DELIVERABLES
 3.1 ACTIVITIES AND DELIVERABLES
 3.2 OUT OF SCOPE
 3.3 PATH TO PRODUCTION

4.EXPECTED AWS COST BREAKDOWN BY SERVICES

5.TEAM

6.RESOURCES & COST ESTIMATES

7.ACCEPTANCE
### 1. BACKGROUND AND MOTIVATION
### 1.1 EXECUTIVE SUMMARY  
The AWS Security Scan Project aims to automate the security inspection process across the software development lifecycle by integrating AWS services such as CodePipeline, CodeBuild, CodeGuru Reviewer, and AWS Security Hub.
This initiative enhances the security posture of continuous integration and deployment pipelines by embedding automated vulnerability scanning, AI-powered code analysis, and centralized incident monitoring.
Use cases include:

Continuous integration with built-in security validation.

Automated alerts and compliance reporting.

Real-time visibility into vulnerabilities and code quality.

Partner services focus on designing, implementing, and optimizing a DevSecOps pipeline that ensures secure, compliant, and efficient software delivery.

### 1.2 PROJECT SUCCESS CRITERIA  
≥95% of code commits pass automated security scans before deployment.

Real-time alerts are sent within 2 minutes of anomaly detection.

Security Hub compliance score ≥90%.

Successful integration between CodePipeline, CodeBuild, and Security Hub with zero manual intervention.

### 1.3 ASSUMPTIONS  
All AWS accounts are pre-configured with IAM roles and permissions for CodePipeline and CodeBuild.

GitLab repository access and webhooks are enabled.

Security tools (e.g., Trivy, Bandit, SonarQube) are available in CodeBuild environment.

The organization follows AWS Well-Architected and Security best practices.

### 2. SOLUTION ARCHITECTURE / ARCHITECTURAL DIAGRAM
### 2.1 TECHNICAL ARCHITECTURE DIAGRAM

The proposed solution integrates multiple AWS services for CI/CD, automated security analysis, and monitoring.
It includes components for source control (GitLab), build and test automation (CodeBuild), pipeline orchestration (CodePipeline), AI-based code review (CodeGuru Reviewer), and centralized alerting (Security Hub + SNS).

(Insert Diagram: /images/2-Proposal/Security Scan project AWS.drawio.png)

# Tools used: #

GitLab

AWS CodePipeline

AWS CodeBuild

AWS CodeGuru Reviewer

AWS Security Hub, GuardDuty, Detective

SonarQube, Trivy, Bandit

### 2.2 TECHNICAL PLAN

The partner will develop buildspec scripts in YAML for CodeBuild to automate:

Source code scanning (Trivy, Bandit)

Static code analysis (CodeGuru Reviewer)

Build packaging and deployment triggers

All deployments will be version-controlled via GitLab CI triggers.
Configuration files will follow Infrastructure as Code principles using AWS CloudFormation.

### 2.3 PROJECT PLAN

The team will adopt Agile Scrum methodology over 4 sprints (2 weeks each).
Stakeholders will participate in Sprint Reviews and Retrospectives.

Roles and responsibilities:

DevOps Engineer: CI/CD pipeline setup

Security Engineer: Security integration and analysis

Project Lead: Coordination, reporting, documentation

Weekly sync-up meetings will be held via Slack and AWS Chime.

### 2.4 SECURITY CONSIDERATIONS

Access – IAM least privilege, MFA for admin accounts

Infrastructure – Private subnets for build agents

Data – S3 encryption (SSE-KMS), CodeBuild log encryption

Detection – GuardDuty and Security Hub continuous monitoring

Incident Management – SNS notifications and CloudWatch alarms for anomalies

### 3. ACTIVITIES AND DELIVERABLES
### 3.1 ACTIVITIES AND DELIVERABLES
| Project Phase            | Timeline | Activities                          | Deliverables/Milestones        | Total Man-days |
|---------------------------|-----------|--------------------------------------|--------------------------------|----------------|
| Assessment                | Week 1–2 | Analyze existing CI/CD               | Report & Architecture Design    | 5              |
| Setup base infrastructure | Week 3–4 | Create CodePipeline & CodeBuild      | Pipeline Deployed               | 7              |
| Integrate Security Tools  | Week 5–6 | Add SonarQube, Trivy, Bandit         | Security Scan Active            | 6              |
| Monitoring Setup          | Week 7   | Connect Security Hub, CloudWatch     | Alert System Operational        | 4              |
| Testing & Go-Live         | Week 8   | Final testing, documentation         | Go-Live Report                  | 3              |
| Handover                  | Week 9   | Knowledge transfer                   | Final Project Handover          | 2              |

### 3.2 OUT OF SCOPE

On-premises application security scanning

Third-party compliance frameworks beyond AWS tools

Non-AWS CI/CD environments

### 3.3 PATH TO PRODUCTION

The Proof-of-Concept focuses on AWS-native DevSecOps integration.
For production deployment, additional steps such as multi-account security setup, network isolation, and automated patching will be required.

### 4. EXPECTED AWS COST BREAKDOWN BY SERVICES
| Service          | Description              | Estimated Monthly Cost (USD) |
|------------------|--------------------------|-------------------------------|
| CodePipeline     | Orchestration            | 10                            |
| CodeBuild        | Build + Scan             | 30                            |
| CodeGuru Reviewer| Code analysis            | 25                            |
| Security Hub     | Aggregation + Alerts     | 15                            |
| CloudWatch       | Logs + Metrics           | 10                            |
| S3               | Artifact storage         | 5                             |
| SNS              | Notifications            | 5                             |
| **Total (approx.)** |                          | **100 USD/month**             |



### 5. TEAM
| Name             | Student ID | Email / Contact                  |
|------------------|-------------|----------------------------------|
| Lê Công Cảnh     | SE183750    | canhlcse183750@fpt.edu.vn       |
| Phùng Gia Đức    | SE183187    | ducpgse183187@fpt.edu.vn        |
| Vũ Nguyễn Bình   | SE193185    | vunguyenbinh25@gmail.com        |
| Lê Minh Dương    | SE184079    | duonglmse184079@fpt.edu.vn      |
| Nguyễn Phi Duy   | SE180529    | duynpse180529@fpt.edu.vn        |




### 6. RESOURCES & COST ESTIMATES
| Resource           | Responsibility        | Rate (USD/hr) | Total Hours | Cost (USD) |
|-------------------|---------------------|---------------|------------|------------|
| Solution Architect | Design & Review      | 60            | 40         | 2400       |
| DevOps Engineer    | Pipeline Implementation | 45         | 60         | 2700       |
| Security Engineer  | Tool Integration     | 50            | 50         | 2500       |
| **Total**          |                     |               | 150        | **7600**   |




### 7. ACCEPTANCE

Upon completion of each phase, the provider will submit deliverables to the customer with an Acceptance Form.
The customer will review within 8 business days and provide either:

Written acceptance confirmation, or

Rejection notice with feedback.

If no response is received within the acceptance period, the deliverable is deemed accepted.
---


