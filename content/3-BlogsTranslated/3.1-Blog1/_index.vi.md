---
title: "Sử dụng Large Language Models trên Amazon Bedrock cho Thực thi Tác vụ Đa bước"
date: 2025-10-16
weight: 1
chapter: false
pre: "<b> 3.1. </b>"
---

Trong bài viết này, chúng ta sẽ tìm hiểu cách sử dụng **Large Language Models (LLMs)** trên **Amazon Bedrock** để thực hiện các tác vụ phân tích gồm nhiều bước, cần suy luận và sử dụng API bên ngoài. Mục tiêu là biến các truy vấn phức tạp thành chuỗi các bước **Plan → Execute** rõ ràng, dễ kiểm soát và dễ mở rộng.

---

## 1. Bối cảnh

Các câu hỏi phân tích dữ liệu trong doanh nghiệp thường phức tạp, ví dụ:

- “Thời gian nằm viện trung bình của bệnh nhân mắc bệnh X tại các bệnh viện khác nhau là bao lâu?”
- “Xu hướng kê đơn thuốc Y thay đổi như thế nào giữa các khu vực?”

Trước đây, việc trả lời yêu cầu:

- Chuyên gia BI  
- Kỹ sư dữ liệu  
- Quy trình nhiều bước, tốn thời gian  

Với **LLM + công cụ (tools/API)**, ta có thể:

- Chia nhỏ nhiệm vụ thành nhiều bước rõ ràng
- Gọi API để truy xuất và xử lý dữ liệu
- Ghép kết quả thành câu trả lời cuối cùng có giải thích

---

## 2. Tool trong bối cảnh LLM

**Tool** là khả năng bên ngoài mà LLM có thể gọi:

- API truy xuất dữ liệu  
- Hàm chạy Python/SQL  
- Lọc, nhóm, join dữ liệu  
- Duyệt web hoặc xử lý file  

Nhờ tool, LLM không chỉ trả lời bằng văn bản mà thực sự **thực thi logic**, giúp kết quả chính xác hơn.

---

## 3. Ví dụ tương tác với agent

**User:** “Ai là bệnh nhân có số vaccine ít nhất?”  
**AI:** “Bệnh nhân Sharleen176 Kulas532 có 1 vaccine.”

Các bước agent thực hiện:

1. Lấy danh sách bệnh nhân  
2. Lấy hồ sơ tiêm chủng  
3. Nhóm theo bệnh nhân  
4. Đếm số vaccine  
5. Sắp xếp tăng dần  
6. Lấy bản ghi đầu tiên  
7. Join để lấy tên đầy đủ  
8. Trả về kết quả

---

## 4. Dataset & thiết lập

Giải pháp dùng **Synthetic Patient Generation Dataset**, một dataset y tế mô phỏng.

Tải và giải nén:

- Tải file dataset
- Giải nén
- Chuyển thư mục về `dataset/`

---

## 5. Kiến trúc Plan → Execute

Kiến trúc gồm 2 giai đoạn:

- **Plan**: LLM lập kế hoạch từng bước  
- **Execute**: Engine chạy từng bước  

Luồng xử lý:

User → LLM tạo kế hoạch → JSON Plan → Engine Execute → Kết quả cuối

---

## 6. Giai đoạn Plan

### 6.1. Lý do cần Plan

- LLM suy luận tuần tự  
- Tạo chuỗi hành động có cấu trúc  
- Giảm lỗi bịa API  

Tách Plan & Execute giúp dễ debug và mở rộng.

### 6.2. Tool signatures

LLM được cung cấp danh sách hàm hợp lệ (toolbox):

- Lấy bệnh nhân  
- Lấy hồ sơ tiêm chủng  
- Lọc dữ liệu  
- Join dữ liệu  
- Nhóm và sắp xếp dữ liệu  

LLM **không được tự tạo hàm mới**.

---

## 6.3. Dùng RAG để lọc tool phù hợp

RAG giúp:

- Hiển thị đúng tool liên quan  
- Giảm độ phức tạp của prompt  
- Tránh LLM chọn sai hàm  

---

## 6.4. Kế hoạch ví dụ

Truy vấn: “Tìm bệnh nhân có số vaccine ít nhất.”

Kế hoạch gồm:

1. Lấy bệnh nhân  
2. Lấy tiêm chủng  
3. Nhóm theo bệnh nhân và đếm  
4. Sắp xếp tăng dần  
5. Lấy bản ghi đầu  
6. Join  
7. Select các trường cần thiết  

---

## 7. Giai đoạn Execute

Engine sẽ:

- Parse JSON  
- Thực thi từng bước  
- Lưu kết quả trung gian  
- Trả kết quả cuối  

Pipeline:

Lấy tiêm chủng → Nhóm → Sắp xếp → Giới hạn → Join → Select

LLM sau đó diễn giải kết quả thành câu trả lời tự nhiên.

---

## 8. Xử lý lỗi

Lỗi có thể gồm:

- Dataset rỗng  
- Tham số sai  
- Kiểu dữ liệu không khớp khi join/filter  

Engine cần:

- Kiểm tra tham số  
- Kiểm tra input/output  
- Trả thông tin lỗi  

LLM có thể **tự tạo lại kế hoạch**.

---

## 9. Kết luận

Chúng ta đã hiểu cách:

- LLM dùng API để trả lời truy vấn phức tạp  
- Kiến trúc Plan → Execute hoạt động  
- RAG và function signatures giúp LLM lập kế hoạch chính xác  
- Error handling giúp hệ thống ổn định  

LLM giờ đây có thể trở thành **bộ não điều phối** quy trình phân tích dữ liệu, không chỉ sinh văn bản.

---

## 10. Hướng phát triển

Có thể mở rộng:

- Thêm truy vấn phân tích nâng cao  
- Thêm tool signatures mới  
- Xây dựng UI để nhập câu hỏi và xem plan/log  

Giải pháp vừa mang tính học thuật vừa gần thực tế doanh nghiệp.
