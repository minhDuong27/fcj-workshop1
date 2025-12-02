---
title: "Event 3"
date: 2025-11-29
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---


# Summary Report: "AWS Well-Architected Security Pillar Workshop"

### Event Details

- **Date:** November 29, 2025 — Morning Only  
- **Time:** 08:30 AM – 12:00 PM  
- **Location:** AWS Vietnam Office  

### Speakers

- **Le Vu Xuan An** – AWS Cloud Club Captain HCMUTE  
- **Tran Duc Anh** – AWS Cloud Club Captain SGU  
- **Tran Doan Cong Ly** – AWS Cloud Club Captain PTIT  
- **Danh Hoang Hieu Nghi** – AWS Cloud Club Captain HUFLIT  

---

## 8:30 – 8:50 AM | Opening & Security Foundation

- Role of the Security Pillar within the Well-Architected Framework  
- Core principles: Least Privilege, Zero Trust, Defense in Depth  
- Shared Responsibility Model  
- Common cloud threats in Vietnam  

---

## Pillar 1 — Identity & Access Management

### 8:50 – 9:30 AM | Modern IAM Architecture

- IAM basics: Users, Roles, Policies – avoiding long-term credentials  
- IAM Identity Center: SSO and permission sets  
- SCPs and permission boundaries for multi-account setups  
- MFA, credential rotation, Access Analyzer  
- Mini Demo: Validate IAM Policy + simulate access  

---

## Pillar 2 — Detection

### 9:30 – 9:55 AM | Detection & Continuous Monitoring

- Organization-level CloudTrail, GuardDuty, Security Hub  
- Logging across all layers: VPC Flow Logs, ALB Logs, S3 Access Logs  
- Alerting & automation with EventBridge  
- Detection-as-Code (infrastructure + rules as code)  

---

## 9:55 – 10:10 AM | Coffee Break

---

## Pillar 3 — Infrastructure Protection

### 10:10 – 10:40 AM | Network & Workload Security

- VPC segmentation: private vs public placement  
- Security Groups vs NACLs and when to use each  
- WAF, Shield, Network Firewall  
- Workload protection fundamentals: EC2, ECS/EKS  

---

## Pillar 4 — Data Protection

### 10:40 – 11:10 AM | Encryption, Keys & Secrets

- KMS: key policies, grants, rotation  
- Encryption at-rest & in-transit for S3, EBS, RDS, DynamoDB  
- Secrets Manager & Parameter Store best practices  
- Data classification and access guardrails  

---

## Pillar 5 — Incident Response

### 11:10 – 11:40 AM | IR Playbook & Automation

- AWS Incident Response lifecycle  
- Example playbooks:
  - Compromised IAM key  
  - Public S3 exposure  
  - EC2 malware detection  
- Snapshotting, isolation & evidence collection  
- Automated response with Lambda / Step Functions  

---

## 11:40 AM – 12:00 PM | Wrap-Up & Q&A

- Summary of all 5 pillars  
- Common pitfalls & real examples from Vietnamese companies  
- Recommended learning path (Security Specialty, SA Pro)