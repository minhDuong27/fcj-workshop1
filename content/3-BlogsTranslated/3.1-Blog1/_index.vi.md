---
title: "Blog 1"
date: 2025-10-16
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Sử dụng Mô hình Ngôn ngữ Lớn (LLM) trên Amazon Bedrock cho thực thi tác vụ đa bước

**Bởi Bruno Klein, Mohammad Arbabshirani, và Rushabh Lokhande vào 02 Tháng 4 2025**  
**Chủ đề:** Amazon Bedrock, Generative AI, Intermediate (200)

Mục tiêu của bài viết này là cho bạn thấy cách sử dụng mô hình ngôn ngữ lớn (LLM) để thực hiện các tác vụ đòi hỏi suy luận và thực thi động nhiều bước. Ví dụ về các tác vụ này bao gồm: 

- “Thời gian nằm viện trung bình của bệnh nhân mắc [bệnh cụ thể] tại các bệnh viện khác nhau là bao lâu?”  
- “Xu hướng kê đơn [thuốc cụ thể] khác nhau như thế nào giữa các khu vực khác nhau?”  

Truy xuất những thông tin này truyền thống cần chuyên môn của các chuyên gia trí tuệ kinh doanh và kỹ sư dữ liệu, dẫn đến quy trình tốn thời gian và tiềm ẩn nhiều điểm nghẽn.

Tuy nhiên, tiến bộ trong LLM mở ra khả năng chia nhỏ các nhiệm vụ phức tạp thành một loạt các bước, sử dụng các công cụ để hoàn thành từng bước và đưa ra giải pháp cuối cùng.

## Công cụ và khả năng mở rộng

Thuật ngữ *công cụ* ở đây đề cập đến các khả năng bên ngoài hoặc API mà mô hình có thể truy cập để mở rộng chức năng của nó. Các công cụ này cho phép LLM:

- Truy xuất thông tin thời gian thực  
- Chạy mã  
- Duyệt web  
- Tạo hình ảnh  

Bằng cách sử dụng các công cụ, LLM có thể đưa ra kết quả chính xác hơn, nhận biết ngữ cảnh và hành động, hỗ trợ hiệu quả các truy vấn phức tạp.

## Ví dụ giải pháp: truy xuất hồ sơ bệnh nhân

Chúng tôi sử dụng **Synthetic Patient Generation dataset** và chỉ dùng API thay vì text-to-SQL. Mã nguồn có sẵn trên GitHub.

### Tổng quan giải pháp

Mục tiêu: trả lời chính xác câu hỏi phân tích đòi hỏi suy luận đa bước. Ví dụ tương tác:

User: Cho tôi tên đầu và tên cuối của bệnh nhân có ít vaccine nhất và số lượng vaccine của họ.
AI: Bệnh nhân ít vaccine nhất là Sharleen176 Kulas532, số vaccine là 1.


Các bước:

1. Lấy danh sách bệnh nhân và hồ sơ tiêm chủng.  
2. Nhóm hồ sơ tiêm chủng theo `patient_id` và đếm số vaccine mỗi bệnh nhân.  
3. Sắp xếp theo số vaccine tăng dần.  
4. Giới hạn kết quả 1 bản ghi (bệnh nhân ít vaccine nhất).  
5. Ghép với thông tin bệnh nhân để lấy tên đầu và tên cuối.  
6. Chọn ra thông tin cần (tên đầu, tên cuối, số vaccine).
   
### Thiết lập dữ liệu

curl https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip > dataset.zip
unzip dataset.zip
mv csv dataset

Giải pháp được cấu trúc từ hai bước lõi: lập kế hoạch (plan) và thực thi (execute). Ở dạng đơn giản nhất, có thể biểu diễn như sơ đồ sau. 
![image](/images/Ảnh 1 (2).png)

Trong kịch bản phức tạp hơn, bạn có thể thêm nhiều lớp xác thực và cung cấp các API phù hợp để nâng cao tỷ lệ thành công của LLM.

![image](/images/Ảnh 2 (1).png)

### Lập kế hoạch (Plan)

Trong giai đoạn Plan, LLM được cung cấp một tập các **chữ ký hàm (function signatures)** đã định nghĩa sẵn cùng mô tả ngắn gọn công dụng của mỗi hàm. Những chữ ký hàm này được xem như các công cụ mà LLM có thể sử dụng để xây dựng kế hoạch trả lời truy vấn của người dùng. Mục tiêu là để LLM suy luận tuần tự các bước cần thiết để đạt được câu trả lời, giống như cách một con người thực hiện.

#### Tại sao giai đoạn lập kế hoạch quan trọng

Giai đoạn Plan rất quan trọng vì nó cho phép LLM tạo ra một chuỗi hành động có cấu trúc và logic để thực thi ở bước tiếp theo. Bằng việc lập kế hoạch, LLM có thể chia nhỏ các câu hỏi phức tạp thành các bước dễ quản lý, đảm bảo các API được gọi đúng thứ tự. Cách tiếp cận có cấu trúc này giúp giảm thiểu lỗi và tăng khả năng tạo ra kết quả chính xác.

