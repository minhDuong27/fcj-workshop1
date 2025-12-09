---
title: "Cập nhật phương pháp Carbon cho Công cụ Dấu Chân Carbon của Khách Hàng AWS (CCFT)"
date: 2025-10-16
weight: 2
chapter: false
pre: "<b> 3.2. </b>"
---

# Cập nhật Phương pháp Carbon cho Công cụ Dấu chân Carbon của Khách hàng AWS  
*(Theo tài liệu gốc AWS, cập nhật ngày 23/04/2025)*

Để hỗ trợ hành trình bền vững của khách hàng, AWS đã ra mắt Công cụ Dấu chân Carbon của Khách hàng (Customer Carbon Footprint Tool – CCFT) vào năm 2022. CCFT giúp khách hàng theo dõi, đo lường và xem xét lượng khí thải carbon phát sinh từ việc sử dụng AWS, bao gồm khí thải Scope 1 và Scope 2 theo chuẩn Greenhouse Gas Protocol. Các số liệu được tính cho toàn bộ dải dịch vụ AWS như Amazon EC2, Amazon S3, AWS Lambda và nhiều dịch vụ khác.

Hôm nay, AWS công bố ba cập nhật mới cho CCFT:

1. Dễ dàng truy cập dữ liệu hơn thông qua dịch vụ Billing and Cost Management Data Exports.  
2. Thông tin carbon chi tiết hơn theo từng vùng AWS (Regional Granularity).  
3. Phương pháp phân bổ mới (Methodology v2.0), có xác minh độc lập từ APEX.

Từ tháng 1 năm 2025 trở về sau, CCFT sẽ sử dụng phương pháp v2.0. Dữ liệu trước tháng 12/2024 vẫn dùng phương pháp v1.0.

---

# 1. Làm cho việc truy cập dữ liệu dễ hơn

Khách hàng hiện có thể xuất dữ liệu carbon từ CCFT thông qua AWS Data Exports trong Billing and Cost Management. 

Dữ liệu xuất ra:

- Bao gồm ước tính khí thải carbon cho tất cả tài khoản trong AWS Organizations.  
- Được gửi tự động mỗi tháng dưới dạng CSV hoặc Parquet vào Amazon S3.  
- Bao gồm tối đa 38 tháng dữ liệu lịch sử trong lần xuất đầu tiên.  

Các tháng trước 12/2024 dùng v1.0, từ 1/2025 trở đi dùng v2.0.

---

# 2. Chi tiết theo vùng AWS (Regional Granularity)

Khách hàng giờ có thể xem lượng khí thải carbon chia nhỏ theo từng **AWS Region**.  
Riêng Amazon CloudFront được hiển thị dưới một mục **Global Services**.

Điều này giúp khách hàng:

- Xác định vùng nào tiêu tốn nhiều carbon nhất.  
- Cân nhắc tái phân bổ workloads sang các vùng tối ưu hơn.  

---

# 3. Phương pháp phân bổ (Methodology) v2.0

Khách hàng thường sử dụng nhiều dịch vụ trải dài nhiều vùng AWS, khiến việc phân bổ khí thải trở nên phức tạp.

Phương pháp mới v2.0 tuân theo nhiều tiêu chuẩn quốc tế gồm:

- GHG Protocol Corporate Standard  
- GHG Protocol Product Standard  
- ISO 14040/44 (Life Cycle Assessment)  
- ISO 14067 (Carbon footprint of products)  
- ICT Sector Guidance  

Một số điểm chính:

---

## Phân bổ Scope 1 (Trực tiếp)

Scope 1 bao gồm khí thải trực tiếp từ các nguồn AWS sở hữu hoặc kiểm soát, ví dụ:

- Máy phát dự phòng tại data centers  
- Nhiên liệu sử dụng phục vụ vận hành  

AWS thu thập dữ liệu Scope 1 hàng năm, cấp site, rồi tổng hợp lên cấp cluster (vùng AWS hoặc CloudFront edge cluster).

---

## Phân bổ Scope 2 (Gián tiếp)

Scope 2 bao gồm khí thải gián tiếp từ điện mua từ lưới.

CCFT sử dụng phương pháp:

- **Market-based**  
- Hệ số phát thải dựa trên vị trí địa lý  
- Theo thứ tự ưu tiên của GHG Protocol  

Nguồn dữ liệu về năng lượng tái tạo, grid mix và hệ số phát thải được xác minh hàng năm.

---

## Tổng quan phân bổ v2.0

Quy trình phân bổ gồm 3 bước:

1. Phân bổ khí thải cấp cluster cho từng giá đỡ máy chủ (server rack).  
2. Ánh xạ khí thải từ các giá đỡ đến từng dịch vụ AWS dựa vào mức sử dụng tài nguyên.  
3. Phân bổ khí thải từ dịch vụ AWS đến từng tài khoản khách hàng.

Một số khách hàng có thể thấy số liệu thay đổi vì v2.0 phản ánh chính xác hơn việc sử dụng thực tế.

---

## Ba cập nhật chính trong phương pháp v2.0

1. **Phân bổ phần công suất chưa dùng (unused capacity) cho tất cả khách hàng.**  
   AWS luôn phải xây dựng dư công suất, và phần carbon liên quan đến công suất này giờ sẽ được phân bổ đều theo quy định của GHG Protocol & ISO.

2. **Cải thiện logic phân bổ cho dịch vụ không có phần cứng riêng** (như AWS Lambda, Amazon Redshift).  
   Phân bổ rõ ràng giữa khách hàng AWS và đội ngũ nội bộ Amazon.

3. **Cập nhật phân bổ chi phí chung (overhead)** như:  
   - Giá đỡ mạng  
   - Chi phí mở rộng AWS Regions mới  

---

# Tương lai

AWS sẽ tiếp tục cải thiện CCFT dựa trên dữ liệu mới, khoa học khí hậu và nhu cầu khách hàng.

---

# Cam kết The Climate Pledge

AWS tiếp tục cam kết hướng tới **net-zero carbon vào năm 2040**.  
Để tìm hiểu thêm, khách hàng có thể truy cập trang bền vững của AWS.
