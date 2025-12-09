---
title : "Closed-loop-devsecops"
date :  2025-12-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---
### DevSecOps Feedback Loop (Closed Cycle)

Hệ thống tạo ra một vòng lặp DevSecOps khép kín:
Dev commit code → GitLab
↓
CodePipeline chạy → CodeBuild quét → SonarQube phân tích
↓
Webhook → Lambda → SNS gửi email
↓
Dev nhận lỗi → Fix → Commit lại
↓
Quay lại vòng lặp


### Lợi ích chính
- Tự động phát hiện bug và lỗ hổng bảo mật.
- Cảnh báo real-time giúp dev sửa ngay.
- Bảo đảm chất lượng code xuyên suốt vòng đời phát triển.
- Văn hóa DevSecOps được áp dụng thực tế: “Security shift-left”.

### Kết luận
Pipeline đảm bảo một quy trình phát triển hiện đại, tự động, bảo mật và bền vững. Mỗi commit đều được phân tích nghiêm ngặt, giúp đội dev luôn duy trì chuẩn chất lượng cao.

