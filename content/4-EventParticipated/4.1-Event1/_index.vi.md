---
title: "Event 1"
date: 2025-11-15
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---


# Workshop Report: "AI/ML/GenAI on AWS"

### Workshop Goals

- Nắm được bức tranh tổng quan về AI/ML và hệ sinh thái dịch vụ AWS tại Việt Nam  
- Tìm hiểu quy trình xây dựng mô hình machine learning end-to-end với Amazon SageMaker  
- Khám phá khả năng Generative AI trên Amazon Bedrock  
- Hiểu và thực hành các kỹ thuật prompt engineering và RAG (Retrieval-Augmented Generation)  
- Xây dựng các bài toán AI/ML thực tế dựa trên dịch vụ AWS  

### Event Information

- **Địa điểm**: Văn phòng AWS Vietnam  
- **Thời gian**: 8:30 AM – 12:00 PM, Thứ Bảy, ngày 15/11/2025  

### Instructors & Organizing Team

**Giảng viên:**

- **Lâm Tuấn Kiệt** – Senior DevOps Engineer, FPT Software  
  - Phụ trách phần tổng quan Amazon SageMaker và các dịch vụ ML trên AWS  
- **Đinh Lê Hoàng Anh** – Cloud Engineer Trainee, FCAJ, Swinburne University of Technology  
  - Trình bày về Amazon Bedrock và hệ sinh thái AWS AI/ML  
- **Danh Hoàng Hiếu Nghị** – Fresher AI Engineer, Renova Cloud  
  - Hướng dẫn phần Amazon Bedrock Agent Core, demo live và hỗ trợ thực hành  

**Đơn vị điều phối:**

- **AWS Vietnam Community Team**  
- **Đội ngũ chương trình FCJ (First Cloud Journey)**  

---

### Agenda Chi Tiết

#### 8:30 – 9:00 AM: Đón tiếp & Giới thiệu chung

- Check-in người tham dự, giao lưu ban đầu  
- Giới thiệu mục tiêu của workshop và nội dung chính trong buổi  
- Hoạt động ice-breaker làm quen  
- Lướt qua bối cảnh và xu hướng AI/ML tại Việt Nam  

---

#### 9:00 – 10:30 AM: Tổng quan AWS AI/ML – Amazon SageMaker

**Amazon SageMaker – Nền tảng ML end-to-end**

- **Chuẩn bị và xử lý dữ liệu:**
  - Sử dụng SageMaker Data Wrangler để xử lý, làm sạch dữ liệu  
  - Dùng Ground Truth cho việc gán nhãn và annotate dữ liệu  
  - Quản lý feature tập trung với Feature Store  

- **Huấn luyện, tinh chỉnh và triển khai mô hình:**
  - Tận dụng các built-in algorithm hoặc script custom  
  - Tối ưu mô hình bằng hyperparameter tuning  
  - Nhiều lựa chọn triển khai: real-time, batch, serverless inference  
  - Thử nghiệm A/B và multi-model endpoints cho so sánh mô hình  

- **Tính năng MLOps tích hợp:**
  - SageMaker Pipelines để tự động hóa pipeline ML  
  - Model Registry hỗ trợ quản lý version và governance  
  - Model Monitor theo dõi data drift, chất lượng mô hình  
  - Kết hợp với CI/CD để triển khai mô hình liên tục  

- **Demo trực quan – SageMaker Studio:**
  - Tạo và sử dụng notebook instance  
  - Train một mô hình ML mẫu  
  - Deploy endpoint và gọi thử dự đoán  

---

#### 10:30 – 10:45 AM: Nghỉ giải lao

- Nghỉ ngơi, dùng nước/coffee  
- Trao đổi tự do, hỏi nhanh với các anh/chị AWS  

---

#### 10:45 AM – 12:00 PM: Generative AI với Amazon Bedrock & AWS AI/ML

**Tổng quan các dịch vụ AI/ML trên AWS**

- **Amazon Rekognition**: Phân tích hình ảnh/video, nhận diện đối tượng  
- **Amazon Translate**: Dịch ngôn ngữ tự động với mô hình NMT  
- **Amazon Textract**: Trích xuất text và dữ liệu từ tài liệu, form  
- **Amazon Transcribe**: Chuyển giọng nói thành văn bản  
- **Amazon Polly**: TTS – đọc văn bản với giọng tự nhiên  
- **Amazon Comprehend**: Xử lý ngôn ngữ tự nhiên, phân tích cảm xúc/chủ đề  
- **Amazon Kendra**: Search engine thông minh dựa trên ML  
- **Amazon Lookout**: Phát hiện bất thường từ dữ liệu vận hành  
- **Amazon Personalize**: Gợi ý cá nhân hóa dựa trên ML  

---

**Foundation Models: Claude, Llama, Titan**

- **So sánh và cách chọn mô hình:**
  - **Claude (Anthropic)**: Mạnh ở hội thoại, lý luận phức tạp  
  - **Llama (Meta)**: Linh hoạt, phù hợp tùy biến, mã nguồn mở  
  - **Titan (Amazon)**: Tích hợp sâu với AWS, tối ưu cho hệ sinh thái AWS  
  - Cách cân nhắc chọn model theo bài toán thực tế  

---

**Prompt Engineering**

- **Các nguyên tắc prompt hiệu quả:**
  - Viết prompt rõ ràng, đưa đủ bối cảnh  
  - Sử dụng ví dụ (few-shot) để định hướng output  
  - Dùng chain-of-thought cho các tác vụ phức tạp  
  - Đặt vai trò cho model (persona, role-based prompting)  

- **Kỹ thuật nâng cao:**
  - Điều chỉnh temperature, max tokens  
  - Phân biệt giữa system prompt và user prompt  
  - Dùng template để tái sử dụng prompt cho nhiều bài toán  

---

**Retrieval-Augmented Generation (RAG)**

- **Kiến trúc RAG:**
  - Dùng vector database và embeddings để biểu diễn tài liệu  
  - Semantic search để tìm ngữ nghĩa gần nhất  
  - Đưa context tài liệu tìm được vào prompt LLM  

- **Tích hợp Knowledge Base:**
  - Sử dụng Amazon Bedrock Knowledge Bases  
  - Lưu trữ tài liệu/tri thức trên **Amazon S3**  
  - Kết nối tới nhiều nguồn dữ liệu (S3, DB, API)  
  - Thiết kế cách chunk tài liệu và gắn metadata  
  - Cấu hình bucket policy và phân quyền truy cập S3 an toàn  

---

**Amazon Bedrock Agent Core**

- **Xây dựng AI Agent:**
  - Bedrock Agent Core giúp điều phối các bước tác vụ  
  - Hỗ trợ multi-step reasoning và lập kế hoạch hành động  
  - Cấu hình action groups, tích hợp API bên ngoài  
  - Quản lý memory và trạng thái hội thoại  

- **Tích hợp với công cụ bên ngoài:**
  - Gọi **AWS Lambda** để xử lý logic tùy biến  
  - Sử dụng Lambda cho xử lý dữ liệu thời gian thực  
  - Kết nối API của hệ thống khác thông qua Lambda  
  - Thực thi truy vấn DB, lấy dữ liệu để agent sử dụng  
  - Mô hình serverless với Lambda + Bedrock giúp dễ mở rộng và quản lý  

---

**Guardrails: An Toàn & Lọc Nội Dung**

- Thiết lập lọc nội dung nhạy cảm, độc hại  
- Ẩn hoặc xử lý PII (thông tin nhận dạng cá nhân)  
- Giới hạn chủ đề, block các topic không được phép  
- Tùy biến guardrails theo yêu cầu tuân thủ của doanh nghiệp  

---

**Demo: Xây dựng Chatbot Generative AI với Bedrock**

- Cấu hình quyền truy cập foundation model trong Bedrock  
- Tạo chatbot đơn giản với prompt engineering  
- Bổ sung RAG bằng Knowledge Bases  
- Thêm guardrails đảm bảo phản hồi an toàn  
- Thử nghiệm, điều chỉnh prompt và luồng xử lý  

---

### Những Điều Rút Ra Được

#### Về Amazon SageMaker

- **Nền tảng ML đầy đủ**: Từ chuẩn bị dữ liệu, training, đến deploy đều có tool hỗ trợ  
- **Hỗ trợ MLOps**: Pipelines, Model Registry và Monitor giúp quy trình ML ổn định hơn  
- **Dễ mở rộng**: Từ test nhỏ trong notebook đến production quy mô lớn  
- **Tối ưu chi phí**: Có spot, serverless inference và nhiều lựa chọn cấu hình tài nguyên  

#### Về Generative AI với Bedrock

- **Nhiều lựa chọn model**: Có thể thử và chuyển đổi giữa các foundation model mà không cần tự quản lý hạ tầng  
- **Prompt engineering là chìa khóa**: Output tốt hay không phụ thuộc rất nhiều vào prompt  
- **RAG**: Giải quyết bài toán đưa dữ liệu nội bộ vào LLM mà vẫn đảm bảo cập nhật và kiểm soát được  
- **Guardrails**: Cực quan trọng để triển khai AI một cách an toàn, đúng quy định  
- **Agent**: Cho phép xây dựng các luồng xử lý phức tạp, nhiều bước thay vì chỉ chat Q&A đơn giản  

#### Ứng Dụng Thực Tế

- **Bắt đầu từ use case cụ thể**: Không làm AI chung chung mà gắn với bài toán thật  
- **Prototype nhanh**: Dùng SageMaker Studio để thử nghiệm trước khi đầu tư lớn  
- **Tận dụng foundation models**: Thử model sẵn có rồi mới tính đến training custom nếu cần  
- **Luôn có guardrails**: Đặc biệt với sản phẩm tiếp xúc người dùng cuối  
- **Theo dõi và tối ưu liên tục**: Về chất lượng mô hình lẫn chi phí vận hành  

---

### Cách Áp Dụng Vào Công Việc

- Thử dựng các pipeline đơn giản trên **SageMaker Studio**  
- Xây dựng thử một **RAG chatbot** dùng Bedrock + S3 làm knowledge base  
- Tập trung luyện **prompt engineering** trên nhiều loại foundation model khác nhau  
- Thiết kế **MLOps pipeline** bằng SageMaker Pipelines cho các bài toán ML nội bộ  
- Nghĩ tới việc dùng **Bedrock Agents** để tự động hóa một số quy trình lặp lại  
- Kết hợp **Guardrails** để đáp ứng yêu cầu bảo mật và tuân thủ  
- Ghi chép lại kinh nghiệm, chia sẻ cho team để cùng chuẩn hóa cách làm  

---

### Trải Nghiệm Tại Sự Kiện

Tham gia **"AI/ML/GenAI on AWS Workshop"** tại văn phòng AWS Vietnam mang lại cảm giác khá “đã” vì vừa có phần lý thuyết, vừa có phần demo thực tế:

#### Học Từ Chuyên Gia AWS

- Các anh chị chuyên gia AWS giải thích khá dễ hiểu về cách SageMaker vận hành end-to-end  
- Phần demo Bedrock cho thấy rõ việc build một ứng dụng GenAI trên AWS đơn giản hơn mình tưởng  
- Nhiều ví dụ thực tế từ doanh nghiệp tại Việt Nam, giúp hình dung cách áp dụng vào bối cảnh local  
- Được gợi ý cách chọn đúng dịch vụ/ mô hình cho từng loại bài toán  

#### Demo & Thực Hành

- Thấy trực tiếp quy trình từ dữ liệu → train → deploy một mô hình trên SageMaker Studio  
- Hiểu được luồng build một GenAI app với Bedrock mà không phải lo phần hạ tầng bên dưới  
- Áp dụng ngay các kỹ thuật **prompt engineering** vào ví dụ thực tế  
- RAG demo giúp thấy rõ khác biệt giữa “LLM nói chung chung” và “LLM có kiến thức nội bộ”  
- Agent demo cho thấy tiềm năng tự động hóa nhiều công việc phức tạp  

#### Hiểu Rõ Hơn Về AI/ML Hiện Nay

- Có cái nhìn rõ hơn về sự khác biệt giữa **ML truyền thống** và **Generative AI**  
- Biết khi nào nên chọn SageMaker, khi nào nên ưu tiên Bedrock  
- Nắm được tại sao MLOps là yếu tố bắt buộc nếu muốn đưa ML vào production  

#### Kết Nối Cộng Đồng

- Làm quen thêm nhiều bạn cũng đang bắt đầu với AI/ML trên AWS  
- Trao đổi khá nhiều về khó khăn khi triển khai thực tế (dữ liệu, chi phí, nhân sự, …)  
- Có thêm kênh liên lạc với cộng đồng và các anh chị AWS để hỏi khi cần  

#### Những Ghi Chú Quan Trọng

- Foundation models giúp tiết kiệm rất nhiều thời gian và nguồn lực ban đầu  
- Prompt tốt có thể thay đổi hẳn chất lượng output mà không cần động đến kiến trúc model  
- RAG là một hướng cực kỳ hữu ích khi muốn AI hiểu tài liệu nội bộ  
- Guardrails không chỉ là “nice-to-have” mà gần như là bắt buộc  
- SageMaker là nền tảng phù hợp nếu muốn làm bài bản và đi dài hơi với ML  

---

### Bước Tiếp Theo

- Dùng thời gian rảnh để thử nghiệm thêm trên **SageMaker Studio**  
- Làm một **prototype RAG** nhỏ dùng Bedrock + S3 cho tài liệu nội bộ  
- Thử nhiều kiểu prompt khác nhau cho cùng một bài toán để rút kinh nghiệm  
- Nghiên cứu sâu hơn về Bedrock Agents cho các use case workflow phức tạp  
- Bắt đầu chuẩn hóa cách log, monitor và deploy mô hình giống MLOps chuẩn  
- Tiếp tục cập nhật kiến thức qua **cộng đồng AWS AI/ML** và các buổi meetup sau này  

#### Event Pictures

![AI/ML Workshop](/images/4-EventParticipated/images/1.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/2.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/3.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/4.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/5.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/6.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/7.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/8.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/9.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/10.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/11.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/12.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/13.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/14.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/15.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/16.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/17.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/18.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/19.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/20.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/21.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/22.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/23.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/24.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/25.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/26.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/27.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/28.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/29.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/30.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/31.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/32.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/33.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/34.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/35.jpg)

---

![AI/ML Workshop](/images/4-EventParticipated/images/36.jpg)

> Nhìn chung, workshop này cung cấp giới thiệu toàn diện về dịch vụ AWS AI/ML, từ machine learning truyền thống với SageMaker đến Generative AI tiên tiến với Bedrock. Các trình diễn thực hành và hướng dẫn chuyên gia làm cho các khái niệm phức tạp trở nên dễ tiếp cận và có thể áp dụng ngay lập tức. Điểm chính rút ra là AWS cung cấp một hệ sinh thái hoàn chỉnh để xây dựng, triển khai và mở rộng ứng dụng AI/ML, giúp việc đưa đổi mới AI vào production dễ dàng hơn bao giờ hết.