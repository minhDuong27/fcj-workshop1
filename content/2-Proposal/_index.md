---
title: "Proposal"
date: 2025-09-11
weight: 2
chapter: false
pre: " <b> 2. </b> "
---


# Security Scan Pipeline on AWS Cloud 
## Automated solution for source code security analysis in the DevSecOps pipeline

### 1. BACKGROUND AND PROJECT DRIVERS
#### 1.1 EXECUTIVE SUMMARY
The client is developing an application and wants to adopt a DevSecOps model to automate the build–scan–deploy workflow, improve security, and shorten release cycles.

System objectives:

- Detect security vulnerabilities and code smells early in the source code using Amazon CodeGuru Reviewer.
- Automatically build and create artifacts when new commits occur.
- Store artifacts securely in Amazon S3.
- Automatically deploy the application to Amazon EC2 via AWS CodeDeploy.

Use cases:

- Automatic security scanning on new commits.
- Automated build and artifact creation.
- Secure artifact storage.
- Automatic EC2 deployment.
- Centralized alerts and process monitoring.

Professional services provided:

- Implement CodePipeline integrated with GitHub, include CodeBuild + CodeGuru Reviewer, configure S3 artifact storage, deploy to EC2 with CodeDeploy, and enable security monitoring and logging (CloudWatch, CloudTrail, GuardDuty, Security Hub).

#### 1.2 PROJECT SUCCESS CRITERIA

- The client provides a GitHub repository with appropriate permissions.
- IAM Roles have sufficient permissions for CodeBuild, CodeDeploy, S3, and CloudWatch.
- EC2 instances are provisioned and ready for deployment.
- The application supports deployment via appspec.yml.
- Multiple environments (dev/stg/prod) are not required at this time.
- AWS Free Tier is used to reduce costs where possible.
- Potential risks: timeouts, webhook failures, corrupted artifacts, insufficient IAM permissions.

#### 1.3 ASSUMPTIONS

- The customer provides a GitHub repository with appropriate permissions.
- IAM Roles have sufficient permissions for CodeBuild, CodeDeploy, S3, and CloudWatch.
- EC2 instances are valid and ready for deployment.
- The application supports deployment via appspec.yml.
- Multiple environments (dev/stg/prod) are not required at this time.
- AWS Free Tier is used to minimize costs.
- Potential risks include: timeouts, webhook failures, corrupted artifacts, insufficient IAM permissions.

### 2. SOLUTION ARCHITECTURE / ARCHITECTURAL DIAGRAM
#### 2.1 TECHNICAL ARCHITECTURE DIAGRAM
Architecture diagram: ![DevOps / Pipeline Engineer](/images/2-Proposal/z7163899093605_61ed75e700147e145be9ee71415522bc.jpg)

AWS services used:

- AWS CodePipeline
- AWS CodeBuild
- Amazon CodeGuru Reviewer
- Amazon S3
- AWS CodeDeploy
- Amazon EC2
- Amazon SNS
- CloudWatch, CloudTrail, GuardDuty, Detective, Security Hub

#### 2.2 TECHNICAL PLAN
Includes:

- Configure GitHub connection (OIDC or Personal Access Token).
- Create CodeBuild project and provide buildspec.yml.
- Integrate Amazon CodeGuru Reviewer.
- Configure CodeDeploy and appspec.yml.
- Enable monitoring and security logging following AWS Well-Architected best practices.

#### 2.3 PROJECT PLAN
We will follow Agile Scrum with two sprints (2 weeks per sprint).

Team responsibilities:

- DevOps Engineer: design and implement the pipeline
- Developer: support testing and provide the repository
- Security Analyst: review alerts from CodeGuru & GuardDuty

Meeting cadence:

- Daily Standup
- Weekly Review
- Bi-weekly Retrospective

Knowledge transfer: one training session on using the pipeline and one session on viewing logs & reports.

#### 2.4 SECURITY CONSIDERATIONS

1. Access
- Enable MFA
- Use IAM Roles instead of long-term Access Keys

2. Infrastructure
- Security Groups with IP restrictions

3. Data
- S3 encryption (SSE-S3)

4. Detection
- GuardDuty, Detective, CloudTrail

5. Incident Management
- SNS alerts for failed builds/deployments

### 3. ACTIVITIES & DELIVERABLES
#### 3.1 ACTIVITIES & DELIVERABLES
| Phase                | Duration  | Activity                    | Deliverable         | Man-day |
| -------------------- | --------- | --------------------------- | ------------------- | ------- |
| Assessment           | Week 1    | Requirements gathering      | Initial architecture | X      |
| Infrastructure setup | Week 1–2  | S3, IAM, EC2, GitHub        | Infrastructure      | X      |
| Pipeline setup       | Week 2–3  | CodePipeline + Build + Scan | Complete pipeline   | X      |
| Deployment setup     | Week 3    | CodeDeploy                  | Automated deploy    | X      |
| Testing & Go-live    | Week 4    | Test the pipeline           | Test report         | X      |
| Handover             | Week 4    | Training + documentation    | Final handover      | X      |

#### 3.2 OUT OF SCOPE
- No additional staging/production environments will be provisioned.
- No integration with SonarQube / Trivy / Checkov.
- No advanced dashboard design.
- No autoscaling or load balancer configuration.

#### 3.3 PATH TO PRODUCTION
The POC is intended for the initial demo only.
To move to production, additional work is required: automated unit tests, enhanced monitoring, detailed error handling, and multi-environment CI/CD.

### 4. AWS COST ESTIMATE
Estimated monthly costs:

- CodePipeline: $0.40 / month
- CodeBuild: $0.35 / month
- S3: $0.10 / month
- CodeDeploy: $0.20 / month
- EC2 t2.micro: $0.10 / month
- CloudWatch + SNS: $0.05 / month

Total: ~ $1.2 / month (~ $14.4 / year)

### 5. PROJECT TEAM
Executive Sponsor & Stakeholders

Team: First Cloud Journey

Project Team
| Name             | Student ID | Email / Contact                  |
|------------------|-------------|----------------------------------|
| Lê Công Cảnh     | SE183750    | canhlcse183750@fpt.edu.vn       |
| Phùng Gia Đức    | SE183187    | ducpgse183187@fpt.edu.vn        |
| Vũ Nguyễn Bình   | SE193185    | vunguyenbinh25@gmail.com        |
| Lê Minh Dương    | SE184079    | duonglmse184079@fpt.edu.vn      |
| Nguyễn Phi Duy   | SE180529    | duynpse180529@fpt.edu.vn        |

### 6. RESOURCES & COST ESTIMATES
See the cost estimate on the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01) or download the [budget estimation file](../attachments/budget_estimation.pdf).

#### 6.1 Resource Allocation & Hourly Rates

| **Resource**                   | **Responsibility**                                                                                       | **Rate (USD) / Hour** | **Headcount** |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | --------------------- | ------------- |
| **Solution Architects**        | Architecture design, security review, AWS service integration, oversight of CI/CD & scanning pipeline    | 6 – 9               | 1             |
| **Engineers (DevOps / Cloud)** | Implement CI/CD pipeline, configure CodePipeline/CodeBuild/CodeDeploy, IAM setup, testing, documentation | 4 – 7              | 1–2           |
| **Other (Security Engineer)**  | Integrate code scanning tools (SonarQube, Trivy, CodeGuru Security), analyze reports                     | 5 – 8               | 1             |

#### 6.2 Estimated Project Hours by Phase

| **Project Phase**                           | **Solution Architects (Hours)** | **Engineers (Hours)** | **Other (Hours)** | **Total Hours** |
| ------------------------------------------- | ------------------------------- | --------------------- | ----------------- | --------------- |
| **Phase 1 – Discovery & Requirements**      | 4                               | 4                     | 0                 | 8               |
| **Phase 2 – Architecture Design**           | 6                               | 2                     | 0                 | 8               |
| **Phase 3 – Pipeline Implementation**       | 4                               | 20                    | 6                 | 30              |
| **Phase 4 – Security Scanning Integration** | 2                               | 6                     | 8                 | 16              |
| **Phase 5 – Testing & Validation**          | 2                               | 8                     | 4                 | 14              |
| **Phase 6 – Documentation & Handover**      | 2                               | 6                     | 2                 | 10              |
| **Total Hours**                             | **20**                          | **46**                | **20**            | **86 Hours**    |


### 7. ACCEPTANCE

- The client has 8 days to review the deliverables.
- If no response is received, the deliverables will be considered accepted.
- If defects are found, the provider will fix and resubmit according to the Rejection Notice process.