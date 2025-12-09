---
title : "Sonarqube-analysis"
date :  2025-12-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---
### SonarQube Analysis Architecture

### Sonar Scanner → SonarQube
During the build phase, Sonar Scanner performs:
- Code quality analysis.
- Bug detection.
- Security vulnerability detection (Security Hotspots, Vulnerabilities).
- Code smell, complexity, duplication calculation.

Results are sent to:
- **SonarQube Server (EC2)**
- SonarQube processes and saves the results to its database.

### Webhook Trigger
When the analysis is complete:
- SonarQube makes an HTTP POST call to the API Gateway endpoint.
- Payload contains:
- Project name
- Quality Gate status (Pass/Fail)
- Error summary (bugs, vulnerabilities, code smells,…)

