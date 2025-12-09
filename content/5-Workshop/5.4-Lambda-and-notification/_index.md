---
title : "Lambda-and-notification"
date : 2025-12-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

### Lambda Processing + Notification

### API Gateway → Lambda
API Gateway receives webhook from SonarQube and passes payload to Lambda.

Lambda does:
1. Parse data from SonarQube.
2. Format message (project, error type, severity).
3. Send content to SNS topic.

### SNS Notifications
SNS sends email to dev team:
- Report security errors.
- Report code errors.
- Report Quality Gate failures.
- Link directly to SonarQube dashboard.

Benefits:
- Dev knows errors immediately.
- Reduced debugging time.
- Increase software quality and safety.
