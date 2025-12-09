---
title: "Workshop"
date: 2025-12-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# DevSecOps Security Scan Pipeline trên AWS

#### Tổng quan

Trong workshop này, chúng em xây dựng một pipeline DevSecOps trên AWS nhằm tích hợp bảo mật vào ngay trong quy trình CI/CD thay vì xử lý thủ công ở cuối dự án. Mỗi lần developer đẩy code lên repository, hệ thống sẽ tự động kích hoạt các bước kiểm tra bảo mật và chất lượng mã nguồn.

#### Mục tiêu chính

Tự động quét lỗ hổng bảo mật sau mỗi lần commit/push code.Thực hiện quét container image và dependency bằng Trivy, giúp phát hiện lỗ hổng trong thư viện và base image.Chạy Bandit để kiểm tra các vấn đề bảo mật trong code Python/JavaScript.Tích hợp SonarQube để đánh giá chất lượng code (code smells, duplication, coverage, maintainability…).Đẩy các phát hiện quan trọng lên AWS Security Hub để tập trung quản lý cảnh báo bảo mật.Gửi thông báo real-time (qua Email/SNS/Chat…) khi phát hiện vấn đề nghiêm trọng để đội phát triển xử lý kịp thời.

#### Nội dung

1. [Tổng quan về workshop](5.1-Workshop-overview/)
2. [Pipline flow](5.2-Pipline-flow/)
3. [Sonarqube analysis](5.3-Sonarqube-analysis/)
4. [Lambda and notification](5.4-Lambda-and-notification/)
5. [Close loop devsecops](5.5-Close-loop-devsecops/)
