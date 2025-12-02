---
title: "Blog 2"
date: 2025-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---
# Kích hoạt hoạt động Đầu tiên về Quan sát ở quy mô lớn

*by Rizwan Mushtaq, Kamilo "Kam" Amir, Sunil Ramachandra, and Aswin Vasudevan on 12 SEP 2025*

Observability is no longer a “nice to have” — nó là điều kiện tiên quyết để đảm bảo hệ thống hoạt động an toàn, hiệu quả và có thể mở rộng. Với lượng log, metric và sự kiện bảo mật ngày càng lớn, việc thu thập, xử lý và trực quan hóa dữ liệu một cách có tổ chức trở thành một thách thức đối với nhiều tổ chức. AWS hợp tác với Cribl Search mang lại một pipeline observability tập trung, linh hoạt và có thể tùy chỉnh — biến dữ liệu thô thành thông tin có thể hành động để đưa ra quyết định nhanh hơn, tự tin hơn và ở quy mô lớn.

---

## Hướng dẫn kiến trúc

Dưới đây là các thành phần chính và cách hoạt động của tích hợp giữa **Cribl Search** và **Amazon Managed Grafana**:

| thành phần           | vai trò chính                                                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cribl Search           | Cho phép tìm kiếm “in-place” trên nhiều nguồn dữ liệu (ví dụ: Cribl Lake, Amazon Security Lake, các dịch vụ AWS native).<br />Không cần phải index toàn bộ dữ liệu trước khi tìm kiếm.         |
| Amazon Managed Grafana | Công cụ trực quan hóa mạnh mẽ: làm dashboards, real-time monitoring, drill-down metrics/logs để phân tích sự cố. <br />Được tích hợp plugin cho Cribl Search để lấy dữ liệu trực tiếp từ Cribl. |

---

## Use-Cases nổi bật


Một số kịch bản mà giải pháp này rất hữu dụng:

1. **Monitoring cơ sở hạ tầng đám mây**

   Bạn có thể truy vấn dữ liệu từ các dịch vụ AWS qua API, hoặc dữ liệu tại rest, rồi dùng Cribl để lọc sự kiện cần thiết, sau đó gửi tới hệ thống SIEM hoặc ngay vào dashboards Grafana để theo dõi health, hiệu suất tài nguyên, chi phí
2. **Quản lý hiệu năng ứng dụng (APM)**

   Dashboards thể hiện latency, error rate, user experience, với khả năng drill-down vào các transaction cụ thể. Grafana giúp hiển thị rõ ràng và nhanh chóng những vấn đề ứng dụng cần được xử lý. 
3. **Vận hành & bảo mật (SecOps)**

   Việc hiển thị sự kiện bảo mật trong dashboard chuyên dụng; Cribl hỗ trợ continuous monitoring, compliance reporting, threat detection, investigation workflows. Giúp đội SOC đáp ứng nhanh khi có sự cố.

## Cách thi hành (Walkthrough)


Để thiết lập và vận hành giải pháp, các bước cơ bản như sau:

1. **Chuẩn bị**
   * Có tài khoản AWS với quyền quản trị.
   * Có bucket S3 (ví dụ để lưu VPC Flow Logs), cấu hình phù hợp để các dịch vụ có thể write vào.
   * Tài khoản Cribl Cloud và IAM/credential cần thiết.
2. **Cấu hình xác thực (API Auth)**
   * Tạo token / API credentials trong Cribl để Grafana có thể kết nối an toàn. [ices, Inc.](https://aws.amazon.com/blogs/apn/enhance-data-visibility-with-cribl-search-and-amazon-managed-grafana/?utm_source=chatgpt.com)
3. **Cài đặt plugin Cribl Search trong Grafana**
   * Vào phần Plugins trong Amazon Managed Grafana, tìm plugin “Cribl Search”, thêm kết nối bằng credentials từ Cribl. [Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/enhance-data-visibility-with-cribl-search-and-amazon-managed-grafana/?utm_source=chatgpt.com)
4. **Tạo dashboard & visualization**
   * Ví dụ: xem VPC Flow Logs trong 15 phút gần nhất, nhóm theo trạng thái log mỗi phút. [Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/enhance-data-visibility-with-cribl-search-and-amazon-managed-grafana/?utm_source=chatgpt.com)
   * Chuyển sang chế độ xem bảng (table view) để phân tích log cụ thể, tìm anomaly, trace đường đi của request. [Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/enhance-data-visibility-with-cribl-search-and-amazon-managed-grafana/?utm_source=chatgpt.com)
5. **Vệ sinh & chi phí**
   * Xóa các resource không dùng: bucket S3, cấu hình Flow Logs, cấu hình tạm thời ở Cribl để hạn chế chi phí dư thừa.

---

## Front door microservice

- Cung cấp API Gateway để tương tác REST bên ngoài
- Xác thực & ủy quyền dựa trên **OIDC** thông qua **Amazon Cognito**
- Cơ chế *deduplication* tự quản lý bằng DynamoDB thay vì SNS FIFO vì:
  1. SNS deduplication TTL chỉ 5 phút
  2. SNS FIFO yêu cầu SQS FIFO
  3. Chủ động báo cho sender biết message là bản sao

---

## Staging ER7 microservice

- Lambda “trigger” đăng ký với pub/sub hub, lọc message theo attribute
- Step Functions Express Workflow để chuyển ER7 → JSON
- Hai Lambda:
  1. Sửa format ER7 (newline, carriage return)
  2. Parsing logic
- Kết quả hoặc lỗi được đẩy lại vào pub/sub hub

---

## Tính năng mới trong giải pháp

### 1. AWS CloudFormation cross-stack references

Ví dụ *outputs* trong core microservice:

```yaml
Outputs:
  Bucket:
    Value: !Ref Bucket
    Export:
      Name: !Sub ${AWS::StackName}-Bucket
  ArtifactBucket:
    Value: !Ref ArtifactBucket
    Export:
      Name: !Sub ${AWS::StackName}-ArtifactBucket
  Topic:
    Value: !Ref Topic
    Export:
      Name: !Sub ${AWS::StackName}-Topic
  Catalog:
    Value: !Ref Catalog
    Export:
      Name: !Sub ${AWS::StackName}-Catalog
  CatalogArn:
    Value: !GetAtt Catalog.Arn
    Export:
      Name: !Sub ${AWS::StackName}-CatalogArn
```
