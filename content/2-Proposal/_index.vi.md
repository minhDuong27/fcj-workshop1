---
title: "Đề Xuất Dự Án"
date: 2025-09-11
weight: 2
chapter: false
pre: " <b> 2. </b> "
---


## Security Scan Pipeline on AWS Cloud 
## Giải pháp tự động hoá phân tích bảo mật mã nguồn trong DevSecOps Pipeline  

### 1. BỐI CẢNH VÀ ĐỘNG LỰC DỰ ÁN
#### 1.1 TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)
Khách hàng đang phát triển ứng dụng và mong muốn tích hợp mô hình DevSecOps nhằm tự động hóa quy trình build – scan – deploy, tăng tính bảo mật và rút ngắn thời gian release.

*Mục tiêu của hệ thống* là:

- Phát hiện sớm lỗi bảo mật và code smell trong mã nguồn bằng Amazon CodeGuru Reviewer.
- Tự động build và tạo artifact khi có commit mới.
- Lưu trữ artifact an toàn trên Amazon S3.
- Triển khai tự động ứng dụng lên Amazon EC2 qua AWS CodeDeploy.

*Use cases*:

- Quét bảo mật tự động khi có commit mới.
- Build và tạo artifact tự động.
- Lưu trữ artifact an toàn.
- Deploy EC2 tự động.
- Gửi cảnh báo và theo dõi quy trình tập trung.

*Dịch vụ chuyên môn được cung cấp*:

- Triển khai CodePipeline kết nối GitHub, tích hợp CodeBuild + CodeGuru Reviewer, tạo hệ thống lưu trữ artifact trên S3, triển khai CodeDeploy lên EC2, kèm toàn bộ hệ thống giám sát bảo mật và logging (CloudWatch, CloudTrail, GuardDuty, Security Hub).

#### 1.2 TIÊU CHÍ THÀNH CÔNG DỰ ÁN (PROJECT SUCCESS CRITERIA)
 
+ Khách hàng cung cấp repo GitHub với quyền phù hợp.
+ IAM Role đủ quyền cho CodeBuild, CodeDeploy, S3, CloudWatch.
+ EC2 instance hợp lệ và sẵn sàng để triển khai.
+ Ứng dụng hỗ trợ triển khai qua appspec.yml.
+ Không yêu cầu nhiều môi trường dev/stg/prod tại thời điểm này.
+ Free Tier của AWS được sử dụng để giảm chi phí.
+ Các rủi ro có thể xảy ra: timeout, lỗi webhook, artifact lỗi, thiếu quyền IAM.

#### 1.3 GIẢ ĐỊNH VÀ RÀNG BUỘC (ASSUMPTIONS)

+ Khách hàng cung cấp repo GitHub với quyền phù hợp.
+ IAM Role đủ quyền cho CodeBuild, CodeDeploy, S3, CloudWatch.
+ EC2 instance hợp lệ và sẵn sàng để triển khai.
+ Ứng dụng hỗ trợ triển khai qua appspec.yml.
+ Không yêu cầu nhiều môi trường dev/stg/prod tại thời điểm này.
+ Free Tier của AWS được sử dụng để giảm chi phí.
+ Các rủi ro có thể xảy ra: timeout, lỗi webhook, artifact lỗi, thiếu quyền IAM.

### 2. KIẾN TRÚC GIẢI PHÁP / SƠ ĐỒ KIẾN TRÚC
#### 2.1 SƠ ĐỒ KIẾN TRÚC KỸ THUẬT (TECHNICAL ARCHITECTURE DIAGRAM)
*Sơ đồ kiến trúc*: ![DevOps / Pipeline Engineer](/images/2-Proposal/z7163899093605_61ed75e700147e145be9ee71415522bc.jpg)

*Danh sách công cụ AWS*:
+ AWS CodePipeline
+ AWS CodeBuild
+ Amazon CodeGuru Reviewer
+ Amazon S3
+ AWS CodeDeploy
+ Amazon EC2
+ Amazon SNS
+ CloudWatch, CloudTrail, GuardDuty, Detective, Security Hub

#### 2.2 KẾ HOẠCH KỸ THUẬT (TECHNICAL PLAN) 
Bao gồm:
+ Thiết lập kết nối GitHub (OIDC/PAT).
+ Tạo dự án CodeBuild + buildspec.yml.
+ Tích hợp CodeGuru Reviewer.
+ Tạo CodeDeploy + appspec.yml.
+ Bật monitoring và security logging theo chuẩn AWS Well-Architected.

#### 2.3 KẾ HOẠCH DỰ ÁN (PROJECT PLAN)
Áp dụng Agile Scrum với 2 sprint (2 tuần/sprint).

*Trách nhiệm nhóm*: 
+ DevOps Engineer: thiết kế và cài đặt pipeline
+ Developer: hỗ trợ test, cung cấp repo
+ Security Analyst: đánh giá cảnh báo CodeGuru & GuardDuty

*Tần suất họp và trao đổi*: 
+ Daily Standup
+ Weekly Review
+ Bi-weekly Retrospective

*Chuyển giao kiến thức*: 1 buổi training sử dụng pipeline và 1 buổi hướng dẫn xem log & báo cáo.

#### 2.4 CÁC YẾU TỐ AN NINH (SECURITY CONSIDERATIONS) 

1. Truy cập (Access)
+ Bật MFA
+ Dùng IAM Role thay vì Access Key

2. Hạ tầng (Infrastructure): Security Group giới hạn IP

3. Dữ liệu (Data): S3 encryption SSE-S3

4. Phát hiện (Detection): GuardDuty, Detective, CloudTrail

5. Quản lý sự cố (Incident Management): SNS cảnh báo build/deploy thất bại


### 3. HOẠT ĐỘNG & SẢN PHẨM BÀN GIAO
#### 3.1 HOẠT ĐỘNG VÀ DELIVERABLES (ACTIVITIES & DELIVERABLES)
| Giai đoạn            | Thời gian | Hoạt động                   | Sản phẩm bàn giao   | Man-day |
| -------------------- | --------- | --------------------------- | ------------------- | ------- |
| Đánh giá             | Tuần 1    | Thu thập yêu cầu            | Kiến trúc ban đầu   | X       |
| Thiết lập hạ tầng    | Tuần 1–2  | S3, IAM, EC2, GitHub        | Hạ tầng             | X       |
| Thiết lập Pipeline   | Tuần 2–3  | CodePipeline + Build + Scan | Pipeline hoàn chỉnh | X       |
| Thiết lập Deployment | Tuần 3    | CodeDeploy                  | Deploy tự động      | X       |
| Kiểm thử & Go-live   | Tuần 4    | Test pipeline               | Báo cáo test        | X       |
| Bàn giao             | Tuần 4    | Training + tài liệu         | KT hoàn chỉnh       | X       |

#### 3.2 PHẠM VI NGOÀI DỰ ÁN (OUT OF SCOPE)
- Không triển khai thêm môi trường staging/production. 
- Không tích hợp SonarQube/Trivy/Checkov. 
- Không thiết kế dashboard nâng cao. 
- Không triển khai autoscaling hoặc load balancer. 

#### 3.3 LỘ TRÌNH LÊN SẢN XUẤT (PATH TO PRODUCTION)
POC chỉ dùng cho demo ban đầu.
Để đưa vào production cần thêm: Unit test tự động, Monitoring nâng cao, Error handling chi tiết, Multi-environment CI/CD

### 4. DỰ TRÙ CHI PHÍ AWS  
*Chi phí ước tính*  
- CodePipeline: 0.40 USD/tháng
- CodeBuild: 0.35 USD/tháng
- S3: 0.10 USD/tháng
- CodeDeploy: 0.20 USD/tháng  
- EC2 t2.micro: 0.10 USD/tháng
- CloudWatch + SNS: 0.05 USD/tháng

Tổng: ~1.2 USD/tháng (~14.4 USD/năm)

### 5. ĐỘI NGŨ THAM GIA DỰ ÁN
*Nhà tài trợ & các bên liên quan (Executive Sponsor & Stakeholders)*  
Team First Cloud Journey

*Đội ngũ triển khai (Project Team)* 

| Name             | Student ID | Email / Contact                  |
|------------------|-------------|----------------------------------|
| Lê Công Cảnh     | SE183750    | canhlcse183750@fpt.edu.vn       |
| Phùng Gia Đức    | SE183187    | ducpgse183187@fpt.edu.vn        |
| Vũ Nguyễn Bình   | SE193185    | vunguyenbinh25@gmail.com        |
| Lê Minh Dương    | SE184079    | duonglmse184079@fpt.edu.vn      |
| Nguyễn Phi Duy   | SE180529    | duynpse180529@fpt.edu.vn        |


### 6. NGUỒN LỰC & ƯỚC TÍNH CHI PHÍ (RESOURCES & COST ESTIMATES)
Có thể xem chi phí trên [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01) Hoặc tải [tệp ước tính ngân sách](../attachments/budget_estimation.pdf).

#### 6.1 PHÂN BỔ NGUỒN LỰC VÀ TỶ LỆ THEO GIỜ

| **Nguồn lực**                                   | **Trách nhiệm**                                                                                                      | **Đơn giá (USD) / Giờ** | **Số lượng nhân sự** |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------- | -------------------- |
| **Kiến trúc sư giải pháp (Solution Architect)** | Thiết kế kiến trúc, đánh giá bảo mật, tích hợp dịch vụ AWS, giám sát xây dựng pipeline CI/CD & hệ thống quét bảo mật | 6 – 9                 | 1                    |
| **Kỹ sư (DevOps / Cloud Engineer)**             | Triển khai CI/CD pipeline, cấu hình CodePipeline/CodeBuild/CodeDeploy, IAM, kiểm thử, viết tài liệu                  | 4 – 7                 | 1–2                  |
| **Kỹ sư bảo mật – Security Engineer**    | Tích hợp công cụ quét bảo mật (SonarQube, Trivy, CodeGuru Security), phân tích báo cáo                               | 5 – 8                 | 1                    |

#### 6.2 ƯỚC TÍNH SỐ GIỜ THEO TỪNG GIAI ĐOẠN 

| **Giai đoạn Dự án**                           | **Giờ của Kiến trúc sư** | **Giờ của Kỹ sư** | **Giờ của Nhân sự khác** | **Tổng Giờ** |
| --------------------------------------------- | ------------------------ | ----------------- | ------------------------ | ------------ |
| **Giai đoạn 1 – Khảo sát & Thu thập yêu cầu** | 4                        | 4                 | 0                        | 8            |
| **Giai đoạn 2 – Thiết kế kiến trúc**          | 6                        | 2                 | 0                        | 8            |
| **Giai đoạn 3 – Triển khai Pipeline**         | 4                        | 20                | 6                        | 30           |
| **Giai đoạn 4 – Tích hợp quét bảo mật**       | 2                        | 6                 | 8                        | 16           |
| **Giai đoạn 5 – Kiểm thử & Đánh giá**         | 2                        | 8                 | 4                        | 14           |
| **Giai đoạn 6 – Tài liệu & Bàn giao**         | 2                        | 6                 | 2                        | 10           |
| **Tổng Số Giờ**                               | **20**                   | **46**            | **20**                   | **86 giờ**   |


### 7. NGHIỆM THU (ACCEPTANCE)
+ Khách hàng có 8 ngày để đánh giá deliverable.
+ Nếu không phản hồi → Deliverable được xem là đã nghiệm thu.
+ Nếu có lỗi → Nhà cung cấp sửa và gửi lại theo quy trình Rejection Notice.