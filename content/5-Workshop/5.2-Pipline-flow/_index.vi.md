---
title : "Pipline-flow"
date :  2025-12-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---
### CodePipeline Flow (GitLab → AWS)

### 1. Source Stage
- CodePipeline được cấu hình lắng nghe commit từ GitLab (branch: main).
- Khi có commit mới, pipeline tự động kích hoạt.
- Output: source artifact để truyền sang bước build.
  
![Codepipline](/static/images/5-Workshop/5.2-Pipline-flow/Codepipeline.png)

### 2. Build Stage (CodeBuild)
- Chạy môi trường build theo buildspec.yml.
- Thực thi:
  - Cài Sonar Scanner.
  - Quét toàn bộ source code.
  - Gửi kết quả sang SonarQube Server.
- Nếu build fail → pipeline dừng.

### 3. Post-Build Actions
- CodeBuild đẩy metadata build (log, status) về CodePipeline.
- Notify optional: Amazon EventBridge / SNS / Slack.

