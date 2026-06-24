# 📊 Progress Tracking - AI Project 3

**Nhóm:** [Điền tên nhóm]  
**Repository:** https://github.com/yourteam/AI_Project3  
**Deadline:** [Điền ngày nộp]  
**Cập nhật lần cuối:** [Điền ngày/giờ]

---

## 🚀 TỔNG QUAN TIẾN ĐỘ

| Thành viên | Dataset / Vai trò | Nhánh Git | 2.1 | 2.2 | 2.3 | 2.4 | 2.5 | % Hoàn thành |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** | MNIST | `feature/mnist` | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | **0%** |
| **B** | Fashion-MNIST | `feature/fashion` | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | **0%** |
| **C** | Food-MNIST | `feature/food` | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | **0%** |
| **D** | Báo cáo | `main` / `feature/report` | - | - | - | - | - | **0%** |
| **E** | Kỹ thuật & Tổng hợp | `main` | - | - | - | - | - | **0%** |

---

## 📝 CHI TIẾT CÔNG VIỆC CHO TỪNG THÀNH VIÊN

### 1. Thành viên A (MNIST) - Nhánh: `feature/mnist`
- [ ] **2.1** Chuẩn bị dữ liệu: Load data, Stratified Split (80/20), vẽ phân phối class.
- [ ] **2.2** Xây dựng Decision Tree (Information Gain) và visualize bằng Graphviz.
- [ ] **2.3** Hyperparameter Tuning: `max_depth`, `min_samples_split`, `min_samples_leaf`.
- [ ] **2.4** Xây dựng Neural Network (MLPClassifier) - ít nhất 1 hidden layer.
- [ ] **2.5** Đánh giá và so sánh: Classification Report, Confusion Matrix, Insights.
- [ ] **Kết quả**:
  - Decision Tree (Test Accuracy): __________
  - Neural Network (Test Accuracy): __________

---

### 2. Thành viên B (Fashion-MNIST) - Nhánh: `feature/fashion`
- [ ] **2.1** Chuẩn bị dữ liệu: Load data, Stratified Split (80/20), vẽ phân phối class.
- [ ] **2.2** Xây dựng Decision Tree (Information Gain) và visualize bằng Graphviz.
- [ ] **2.3** Hyperparameter Tuning: `max_depth`, `min_samples_split`, `min_samples_leaf`.
- [ ] **2.4** Xây dựng Neural Network (MLPClassifier) - ít nhất 1 hidden layer.
- [ ] **2.5** Đánh giá và so sánh: Classification Report, Confusion Matrix, Insights.
- [ ] **Kết quả**:
  - Decision Tree (Test Accuracy): __________
  - Neural Network (Test Accuracy): __________

---

### 3. Thành viên C (Food-MNIST) - Nhánh: `feature/food`
*(⚠️ Lưu ý: Nhớ Resize ảnh 512x512 về 64x64 hoặc dùng PCA trước khi train để tránh quá tải RAM/Timeout)*

- [ ] **2.1** Chuẩn bị dữ liệu: Load data, Resize/PCA, Stratified Split (80/20), vẽ phân phối class.
- [ ] **2.2** Xây dựng Decision Tree (Information Gain) và visualize bằng Graphviz.
- [ ] **2.3** Hyperparameter Tuning: `max_depth`, `min_samples_split`, `min_samples_leaf`.
- [ ] **2.4** Xây dựng Neural Network (MLPClassifier) - ít nhất 1 hidden layer.
- [ ] **2.5** Đánh giá và so sánh: Classification Report, Confusion Matrix, Insights.
- [ ] **Kết quả**:
  - Decision Tree (Test Accuracy): __________
  - Neural Network (Test Accuracy): __________

---

### 4. Thành viên D (Báo cáo & Tổng hợp) - Nhánh: `main` / `feature/report`
- [ ] Tổng hợp bảng so sánh Accuracy của 3 datasets (DT vs MLP).
- [ ] Tổng hợp phần "Insights" từ A, B, C để đưa vào báo cáo.
- [ ] Viết báo cáo PDF (Member info, Work assignment table, Statistical results).
- [ ] Chèn hình ảnh (cây quyết định, confusion matrix) vào đúng vị trí, đảm bảo không bị lỗi cắt trang.
- [ ] Xuất file PDF và đặt tại `report/AI_Project3_Report.pdf`.

---

### 5. Thành viên E (Kỹ thuật & Tổng hợp Source) - Nhánh: `main`
- [ ] Tạo sẵn Kaggle Dataset cho nhóm (MNIST, Fashion, Food).
- [ ] Viết sẵn code mẫu trong `utils/helpers.py` (vẽ biểu đồ, split, đánh giá).
- [ ] Merge các nhánh `feature/mnist`, `feature/fashion`, `feature/food` vào `main`.
- [ ] Chạy kiểm tra toàn bộ Notebook từ đầu đến cuối để đảm bảo không lỗi.
- [ ] Chuẩn bị file nén cuối cùng (`StudentID1_StudentID2_etc.zip`) và upload (nếu >25MB thì tải lên Google Drive).

---

## ⚠️ LƯU Ý & RỦI RO

| Vấn đề | Giải pháp / Trạng thái |
| :--- | :--- |
| **Food-MNIST 512x512** | ✅ Đã nhắc thành viên C xử lý Resize/PCA. |
| **Graphviz trên Kaggle** | ✅ Có lệnh `!apt-get install graphviz -y` trong hướng dẫn. |
| **Kaggle Session Timeout (9h)** | ⚠️ Cần tối ưu tuning, không chạy quá nhiều params. |
| **Xung đột Git** | ⚠️ Mỗi người làm trên nhánh riêng, E sẽ giải quyết conflict khi merge. |

---

## 📅 TIẾN ĐỘ DỰ KIẾN

- **Ngày 1 (Sáng):** Hoàn thành 2.1 và 2.2.
- **Ngày 1 (Chiều):** Hoàn thành 2.3 và 2.4.
- **Ngày 2 (Sáng):** Hoàn thành 2.5, tổng hợp báo cáo, kiểm tra và nộp.