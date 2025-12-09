---
title : "Pipline-flow"
date :  2025-12-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---
### CodePipeline Flow (GitLab → AWS)

### 1. Source Stage
- CodePipeline is configured to listen for commits from GitLab (branch: main).

- When there is a new commit, the pipeline is automatically activated.

- Output: source artifact to transfer to the build step.

### 2. Build Stage (CodeBuild)
- Run the build environment according to buildspec.yml.

- Execute:
- Install Sonar Scanner.
- Scan all source code.
- Send results to SonarQube Server.
- If the build fails → the pipeline stops.

### 3. Post-Build Actions
- CodeBuild pushes build metadata (log, status) to CodePipeline.

- Notify optional: Amazon EventBridge / SNS / Slack.
