---
title: "Workshop"
date: 2025-12-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# DevSecOps Security Scan Pipeline on AWS

#### Overview

In this workshop, we build a DevSecOps pipeline on AWS to integrate security right into the CI/CD process instead of manually handling it at the end of the project. Each time a developer pushes code to the repository, the system will automatically trigger security and source code quality checks.

#### Main objectives

Automatically scan for security vulnerabilities after each commit/push of code. Perform container image and dependency scanning using Trivy, helping to detect vulnerabilities in libraries and base images. Run Bandit to check for security issues in Python/JavaScript code. Integrate SonarQube to evaluate code quality (code smells, duplication, coverage, maintainability...). Push important findings to AWS Security Hub to centrally manage security alerts. Send real-time notifications (via Email/SNS/Chat...) when detecting serious problems for the development team to handle promptly.

#### Content

1. [Workshop overview](5.1-Workshop-overview/)
2. [Pipline flow](5.2-Pipline-flow/)
3. [Sonarqube analysis](5.3-Sonarqube-analysis/)
4. [Lambda and notification](5.4-Lambda-and-notification/)
5. [Close loop devsecops](5.5-Close-loop-devsecops/)
