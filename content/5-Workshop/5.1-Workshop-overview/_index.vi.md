---
title : "Giới thiệu"
date :  2025-12-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---
# DevSecOps Pipeline Overview (GitLab → AWS)

### Mục tiêu pipeline:
- Tự động hóa toàn bộ quy trình build – quét bảo mật – thông báo lỗi.
- Phát hiện sớm bug, lỗ hổng bảo mật ngay khi dev commit code.
- Tạo vòng lặp DevSecOps khép kín: Commit → Scan → Notify → Fix → Commit lại.

### Tóm tắt luồng:
1. Dev commit code vào GitLab (nhánh main).
2. AWS CodePipeline nhận sự kiện và kích hoạt pipeline.
3. CodeBuild chạy Sonar Scanner để phân tích mã nguồn.
4. SonarQube trên EC2 nhận kết quả quét từ Scanner.
5. SonarQube gửi Webhook → API Gateway → Lambda.
6. Lambda xử lý dữ liệu → gửi thông báo qua SNS → email dev.
7. Dev nhận báo cáo lỗi → Fix → Commit lại → quay lại vòng lặp.

### Hệ thống đảm bảo:
- Tự động hóa kiểm thử bảo mật.
- Cải thiện chất lượng mã nguồn.
- Giảm rủi ro bảo mật và lỗi logic.

![overview](/images/5-Workshop/5.1-Workshop-overview/diagram1.png)
