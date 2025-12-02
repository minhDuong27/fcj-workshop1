---
title: "Event 2"
date: 2025-11-17
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Báo Cáo Workshop: "DevOps on AWS"

### Mục Tiêu Sự Kiện

- Hiểu rõ văn hóa DevOps, giá trị cốt lõi và các thực hành tốt nhất  
- Làm quen với các dịch vụ AWS hỗ trợ xây dựng CI/CD  
- Thực hành Infrastructure as Code bằng CloudFormation và AWS CDK  
- Tìm hiểu các nền tảng container trên AWS: ECR, ECS, EKS và App Runner  
- Nắm cách giám sát – quan sát hệ thống bằng CloudWatch và AWS X-Ray  
- Áp dụng DevOps vào các bài toán thực tế trong doanh nghiệp  

### Thông Tin Sự Kiện

- **Địa điểm:** Văn phòng AWS Vietnam  
- **Thời gian:** 8:30 AM – 5:00 PM, Thứ Hai, 17/11/2025  

### Diễn Giả & Ban Tổ Chức

**Diễn giả chính:**

- **Trương Quang Tĩnh** – AWS Community Builder  
  - Giới thiệu văn hoá DevOps và nền tảng CI/CD  
- **Văn Hoàng Kha** – AWS Community Builder  
  - Trình bày Infrastructure as Code với CloudFormation  
- **Nguyễn Khánh Phúc Thịnh** – AWS Community Builder  
  - Hướng dẫn chuyên sâu AWS CDK  
- **Lê Huỳnh Nghiêm** – AWS Community Builder  
  - Giới thiệu dịch vụ container trên AWS  
- **Huỳnh Hoàng Long** – AWS Community Builder  
  - Giám sát và quan sát hệ thống với AWS  
- **Phạm Hoàng Quý** – AWS Community Builder  
  - Văn hoá DevOps và chia sẻ case study thực tế  

**Hỗ trợ tổ chức:**

- **Đội ngũ AWS Vietnam**  
- **Cộng đồng AWS Community Builders Vietnam**  

---

### Agenda Chi Tiết

#### 8:30 – 9:00 AM: Đón Tiếp & Khởi Động

- Check-in, giao lưu  
- Giới thiệu nội dung buổi workshop  
- Tổng quan các dịch vụ DevOps trên AWS  

---

#### 9:00 – 10:30 AM: Văn Hóa DevOps & Quy Trình CI/CD

**Diễn giả: Trương Quang Tĩnh**

- **Tư duy DevOps**:
  - Xoá bỏ rào cản giữa Dev và Ops  
  - Tự động hóa để giảm công việc lặp lại  
  - Cải tiến liên tục  
  - Trách nhiệm chung về chất lượng và an toàn  

- **DORA Metrics** – các chỉ số đo hiệu quả DevOps:
  - Deployment Frequency  
  - Lead Time for Changes  
  - Mean Time to Recovery  
  - Change Failure Rate  

- **Các dịch vụ CI/CD trên AWS**:
  - **CodeCommit** – kho Git trên AWS  
  - **CodeBuild** – build/test tự động  
  - **CodeDeploy** – triển khai ứng dụng  
  - **CodePipeline** – pipeline CI/CD tổng thể  

- **Chiến lược triển khai**:
  - Blue/Green  
  - Canary  
  - Rolling update  

- **Demo**:
  - Xây dựng pipeline CI/CD hoàn chỉnh ngay trong buổi học  

---

#### 10:30 – 10:45 AM: Nghỉ Giải Lao

---

#### 10:45 AM – 12:00 PM: Infrastructure as Code với CloudFormation

**Diễn giả: Văn Hoàng Kha**

- **Nguyên lý của IaC**:
  - Quản lý bằng version control  
  - Môi trường triển khai luôn đồng nhất  
  - Documentation nằm ngay trong template  
  - Test trước khi áp dụng  

- **CloudFormation cơ bản**:
  - Template (YAML/JSON)  
  - Stack  
  - Change Set  
  - Drift Detection  

- **Thực hành tốt**:
  - Tách template theo mô-đun  
  - Dùng Parameter và Output  
  - Cross-stack reference  

- **Tính năng nâng cao**:
  - Stack Policy  
  - Rollback Trigger  
  - StackSets  

- **Demo**:
  - Triển khai ứng dụng 2–3 tầng bằng CloudFormation  

---

#### 12:00 – 1:00 PM: Nghỉ Trưa

---

#### 1:00 – 2:15 PM: Chuyên Sâu AWS CDK

**Diễn giả: Nguyễn Khánh Phúc Thịnh**

- **AWS CDK là gì?**
  - Viết hạ tầng bằng các ngôn ngữ quen thuộc (TS, Python, Java, C#, Go)  
  - Abstraction theo 3 tầng: L1, L2, L3  

- **Khái niệm cốt lõi trong CDK**:
  - Construct  
  - Stack  
  - App  
  - Synthesis  

- **CDK so với CloudFormation**:
  - Có vòng lặp, điều kiện, function  
  - An toàn kiểu dữ liệu  
  - Hỗ trợ IDE tốt hơn  
  - Test được bằng unit test  

- **Thực hành tốt CDK**:
  - Tái sử dụng construct  
  - Tách cấu hình theo môi trường  
  - Giữ Logical ID ổn định  

- **Demo**:
  - Build serverless app bằng CDK  

---

#### 2:15 – 2:30 PM: Nghỉ Ngắn

---

#### 2:30 – 3:45 PM: Container trên AWS

**Diễn giả: Lê Huỳnh Nghiêm**

- **Kiến thức container nền tảng**:
  - Container là gì, ưu điểm của container  
  - Docker image, container, registry  

- **ECR**:
  - Private registry  
  - Image scanning  
  - Lifecycle policy  
  - Multi-region replication  

- **ECS**:
  - Orchestration gọn nhẹ, thuần AWS  
  - Task Definition  
  - Service  
  - Fargate vs EC2 launch type  

- **EKS**:
  - Managed Kubernetes  
  - Dùng kubectl, helm bình thường  
  - Tích hợp tốt với ALB, EBS, EFS  

- **App Runner**:
  - Từ source code → service chỉ với vài bước  
  - Tự động scale  
  - Dùng cho app nhỏ, API, web service  

- **Chọn dịch vụ nào?**
  - ECS → đơn giản, AWS-native  
  - EKS → cần Kubernetes chuyên sâu  
  - App Runner → siêu nhanh, ít cấu hình  

- **Demo**:
  - Deploy app container lên ECS và EKS  

---

#### 3:45 – 4:45 PM: Monitoring & Observability

**Diễn giả: Huỳnh Hoàng Long**

- **Monitoring vs Observability**:
  - Monitoring → thu thập thông số  
  - Observability → hiểu hệ thống qua hành vi đầu ra  

- **CloudWatch**:
  - Metrics  
  - Logs  
  - Alarms  
  - Dashboard  
  - Logs Insights  
  - Events  

- **AWS X-Ray**:
  - Distributed tracing  
  - Service Map  
  - Trace analysis  
  - Error root cause detection  

- **Best Practice**:
  - Structured log  
  - Custom metric  
  - Alert chủ động  
  - Correlate log – metric – trace  
  - Quản lý retention hợp lý  

- **Demo**:
  - Thiết lập giám sát cho ứng dụng microservices  

---

#### 4:45 – 5:00 PM: DevOps Best Practices & Q&A

**Diễn giả: Phạm Hoàng Quý**

- **Best Practice trong DevOps**:
  - Tự động hóa tối đa  
  - Fail fast – học nhanh  
  - Postmortem không đổ lỗi  
  - Progressive delivery  
  - Học hỏi liên tục  

- **Case Study thực tế**:
  - Startup → CI/CD + serverless  
  - Enterprise → Multi-account bằng StackSets  
  - E-commerce → Blue/Green cho high-availability  

---

### Những Điểm Chính Rút Ra

#### Văn Hóa DevOps

- DevOps chú trọng con người và quy trình hơn công cụ  
- Automation giúp giảm sai sót  
- DORA Metrics là nền tảng để đo hiệu quả  
- Cải tiến liên tục là yếu tố bắt buộc  

#### CI/CD

- CodePipeline kết hợp tốt với CodeCommit, CodeBuild, CodeDeploy  
- Giảm manual work, tăng tốc độ release  
- Triển khai đa chiến lược phù hợp từng môi trường  

#### Infrastructure as Code

- CloudFormation → rõ ràng, quản lý tập trung  
- CDK → linh hoạt, thân thiện dev  
- IaC giúp nhất quán và dễ mở rộng  

#### Container

- ECR lưu trữ image an toàn  
- ECS phù hợp team dùng AWS  
- EKS dành cho team rành Kubernetes  
- App Runner dành cho app nhỏ, cần triển khai nhanh  

#### Monitoring

- CloudWatch + X-Ray tạo hệ thống quan sát đầy đủ  
- Logs, metrics, traces cần được kết hợp  
- Cảnh báo sớm giúp giảm downtime  

#### DevOps Best Practices

- Tự động hóa, đo lường, cải tiến  
- Postmortem tập trung vào quy trình  
- Progressive delivery giảm rủi ro  

---

### Ứng Dụng Vào Công Việc

- Bắt đầu xây pipeline CI/CD nhỏ với CodePipeline  
- Chuyển hạ tầng sang IaC bằng CloudFormation/CDK  
- Containerize ứng dụng và thử ECS/EKS  
- Thiết lập dashboard CloudWatch + tracing  
- Thúc đẩy văn hóa DevOps trong team  
- Lên kế hoạch học chứng chỉ AWS DevOps Engineer  

---

### Trải Nghiệm Tại Sự Kiện

- Buổi workshop rất chi tiết và dễ hiểu  
- Demo thực tế giúp nắm bắt nhanh hơn phần lý thuyết  
- Tìm hiểu được nhiều case study thực tế từ doanh nghiệp Việt Nam  
- Cơ hội giao lưu với cộng đồng DevOps trên AWS  

---

### Bước Tiếp Theo

- Thực hành CI/CD trên dự án nhỏ  
- Dùng CloudFormation/CDK cho các môi trường dev/test  
- Dùng ECS hoặc EKS cho các ứng dụng container sẵn có  
- Cải thiện hệ thống quan sát bằng dashboard và alert  
- Tiếp tục học từ cộng đồng AWS DevOps  

