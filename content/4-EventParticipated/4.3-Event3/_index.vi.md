---
title: "Event 3"
date: 2025-11-29
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---



# Báo Cáo Workshop: "AWS Well-Architected Security Pillar"

### Thông Tin Sự Kiện

- **Ngày:** 29/11/2025 — Buổi sáng  
- **Thời gian:** 08:30 AM – 12:00 PM  
- **Địa điểm:** AWS Vietnam Office  

### Danh Sách Diễn Giả

- **Lê Vũ Xuân An** – AWS Cloud Club Captain HCMUTE  
- **Trần Đức Anh** – AWS Cloud Club Captain SGU  
- **Trần Đoàn Công Lý** – AWS Cloud Captain PTIT  
- **Danh Hoàng Hiếu Nghị** – AWS Cloud Captain HUFLIT  

---

## 8:30 – 8:50 AM | Opening & Security Foundation

- Vai trò của Security Pillar trong mô hình Well-Architected  
- Các nguyên tắc quan trọng: Least Privilege, Zero Trust, Defense in Depth  
- Shared Responsibility Model  
- Các mối đe dọa phổ biến trong môi trường cloud tại Việt Nam  

---

## Pillar 1 — Identity & Access Management

### 8:50 – 9:30 AM | Modern IAM Architecture

- IAM: Users, Roles, Policies – hạn chế dùng long-term credentials  
- IAM Identity Center: SSO, permission sets  
- SCP và permission boundaries cho multi-account  
- MFA, credential rotation, Access Analyzer  
- Mini Demo: Validate IAM Policy + simulate access  

---

## Pillar 2 — Detection

### 9:30 – 9:55 AM | Detection & Continuous Monitoring

- CloudTrail (cấp tổ chức), GuardDuty, Security Hub  
- Logging toàn hệ thống: VPC Flow Logs, ALB Logs, S3 Access Logs  
- Alerting và automation với EventBridge  
- Detection-as-Code (quản lý rule + hạ tầng bằng code)  

---

## 9:55 – 10:10 AM | Coffee Break

---

## Pillar 3 — Infrastructure Protection

### 10:10 – 10:40 AM | Network & Workload Security

- VPC segmentation: private vs public placement  
- Security Groups vs NACLs – mô hình áp dụng  
- WAF, Shield, Network Firewall  
- Bảo vệ workload: EC2, ECS/EKS, security basics  

---

## Pillar 4 — Data Protection

### 10:40 – 11:10 AM | Encryption, Keys & Secrets

- KMS: key policies, grants, rotation  
- Encryption at-rest & in-transit: S3, EBS, RDS, DynamoDB  
- Secrets Manager & Parameter Store – best practices & rotation  
- Data classification & access guardrails  

---

## Pillar 5 — Incident Response

### 11:10 – 11:40 AM | IR Playbook & Automation

- Vòng đời Incident Response theo AWS  
- Playbooks mẫu:
  - Compromised IAM key  
  - S3 public exposure  
  - EC2 malware detection  
- Snapshot, isolation, evidence collection  
- Auto-response bằng Lambda / Step Functions  

---

## 11:40 AM – 12:00 PM | Wrap-Up & Q&A

- Tổng kết 5 pillars  
- Sai sót thường gặp & ví dụ thực tế tại doanh nghiệp Việt Nam  
- Roadmap security learning (Security Specialty, SA Pro)  