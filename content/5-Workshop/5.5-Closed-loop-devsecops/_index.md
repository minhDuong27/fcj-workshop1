---
title : "Closed-loop-devsecops"
date : 2025-12-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---
### DevSecOps Feedback Loop (Closed Cycle)

The system creates a closed DevSecOps loop:
Dev commits code → GitLab
↓
CodePipeline runs → CodeBuild scans → SonarQube analyzes
↓
Webhook → Lambda → SNS sends email
↓
Dev receives error → Fix → Commit again
↓
Return to loop

### Main benefits
- Automatically detects bugs and security vulnerabilities.
- Real-time alerts help devs fix immediately.
- Ensures code quality throughout the development lifecycle.
- DevSecOps culture in practice: “Security shift-left”.

### Conclusion
Pipeline ensures a modern, automated, secure and sustainable development process. Each commit is rigorously analyzed, helping the dev team maintain high quality standards.
