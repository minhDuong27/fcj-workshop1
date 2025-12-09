---
title: "Week 10 Worklog"
date: 2025-11-10
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Week 10 Objectives:

* Xây dựng Pipeline hoàn chỉnh.
* Tích hợp CodeGuru Reviewer để quét bảo mật.
* Tạo buildspec.yml và appspec.yml.

---

### Tasks this week:

| Day | Task | Start | End | Reference |
|-----|------|-------|------|-----------|
| 2 | <ul><li>Tạo CodePipeline các stage: Source → Build → Scan → Deploy</li></ul> | 10/11 | 10/11 | AWS CodePipeline |
| 3 | <ul><li>Cấu hình CodeBuild + buildspec.yml</li></ul> | 11/11 | 11/11 | CodeBuild Docs |
| 4 | <ul><li>Tích hợp CodeGuru Reviewer</li></ul> | 12/11 | 12/11 | CodeGuru Docs |
| 5 | <ul><li>Tạo appspec.yml</li></ul> | 13/11 | 13/11 | CodeDeploy Docs |
| 6 | <ul><li>Chạy thử Pipeline — sửa lỗi IAM</li></ul> | 14/11 | 14/11 | Troubleshooting Notes |

---

### Week 10 Achievements:

* Pipeline chạy được 3 stage đầu (Source/Build/Scan).
* CodeGuru Reviewer đã tự động quét mã và phát hiện vấn đề.
* Cấu hình CodeDeploy đã sẵn sàng.
