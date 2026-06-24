Dưới đây là nội dung **README.md** tổng thể dành cho dự án. Bạn (trưởng nhóm) hãy copy nội dung này vào file `README.md` ở root của repository GitHub.

---

# 📘 AI Project 3 - Supervised Learning on MNIST Variants

**Nhóm:** [Điền tên nhóm]  
**Thời gian dự kiến:** 1.5 ngày (48 giờ tập trung)  
**Công nghệ:** `Python`, `scikit-learn`, `Kaggle (Free Tier)`, `GitHub`

---

## 📋 1. PHÂN CÔNG CÔNG VIỆC (JOB ASSIGNMENT)

*Áp dụng chiến lược chia tách theo dataset để tối đa song song hóa.*

| Thành viên | Dataset phụ trách | Vai trò & Nhiệm vụ chi tiết | Sản phẩm bàn giao |
| :--- | :--- | :--- | :--- |
| **A** *(Tên)* | **MNIST** | - Chuẩn bị data, vẽ phân phối (2.1). <br>- Xây dựng Decision Tree + Graphviz (2.2). <br>- Tuning `max_depth`, `min_samples_split`, `min_samples_leaf` (2.3). <br>- Xây dựng MLP (ít nhất 1 hidden layer) (2.4). <br>- Đánh giá test set (Classification Report + Confusion Matrix) (2.5). | `notebooks/mnist.ipynb` <br>Kết quả số (Accuracy/Report) |
| **B** *(Tên)* | **Fashion-MNIST** | *(Tương tự như A)* | `notebooks/fashion.ipynb` <br>Kết quả số |
| **C** *(Tên)* | **Food-MNIST** | *(Tương tự như A, nhưng lưu ý xử lý ảnh 512x512 để tránh OOM - khuyến nghị Resize về 64x64 hoặc PCA)* | `notebooks/food.ipynb` <br>Kết quả số |
| **D** *(Tên)* | **Tổng hợp & Báo cáo** | - Tổng hợp bảng accuracy so sánh giữa 3 dataset và 2 models. <br>- Viết báo cáo PDF (theo mục 3.1: Member info, Work assignment table, Insights). <br>- Đảm bảo hình ảnh không bị cắt khỏi trang. <br>- Viết phần giới thiệu chung và kết luận. | `report/AI_Project3_Report.pdf` <br>Bảng phân công hoàn thành |
| **E** *(Tên)* | **Kỹ thuật & Tổng hợp Source** | - Tạo Dataset tổng hợp trên Kaggle (để A, B, C không cần tải data). <br>- Viết `utils.py` chung (hàm vẽ, split, evaluation). <br>- Hỗ trợ fix lỗi Git, cài Graphviz trên Kaggle. <br>- Merge code từ 3 nhánh vào `main`. <br>- Kiểm tra file nén cuối cùng (dung lượng <25MB hoặc link GDrive). | `utils.py` <br>`requirements.txt` <br>File nén `StudentID1_StudentID2.zip` |

---

## ✅ 2. CHECKLIST ĐÁP ỨNG REQUIREMENTS

*Checklist này bám sát từng tiêu chí chấm điểm (Section 4 của đề bài). Đánh dấu `[x]` khi hoàn thành.*

### Yêu cầu chung cho **CẢ 3 DATASET** (MNIST, Fashion, Food)
*(Mỗi thành viên A, B, C tự kiểm tra dataset của mình)*

| Task ID | Yêu cầu chi tiết | Đã làm? | Ghi chú |
| :--- | :--- | :---: | :--- |
| **2.1** | **Preparing the dataset** <br>- Shuffle & Split stratified (80% train, 20% val). <br>- Giữ nguyên test set có sẵn. <br>- Vẽ biểu đồ class distribution cho Train/Val/Test. | ☐ | Ví dụ biểu đồ cột/tròn |
| **2.2** | **Building Decision Tree** <br>- Dùng `criterion='entropy'` (information gain). <br>- Trực quan hóa cây bằng Graphviz (xuất file .png hoặc render trực tiếp). | ☐ | Lưu ảnh vào thư mục `figures/` |
| **2.3** | **Hyperparameter Tuning (DT)** <br>- Tối thiểu tune 3 tham số: `max_depth`, `min_samples_split`, `min_samples_leaf`. <br>- In ra giá trị tham số tốt nhất (best_params). <br>- Báo cáo Validation Accuracy tốt nhất. | ☐ | Dùng vòng lặp for hoặc GridSearchCV |
| **2.4** | **Building Neural Network (MLP)** <br>- Khai báo rõ: Số hidden layers, số neurons, activation (non-linear), solver (adam/sgd). <br>- Đánh giá trên Validation set. | ☐ | Ghi rõ `hidden_layer_sizes=(100,)` hoặc `(64,32)` |
| **2.5** | **Performance Evaluation** <br>- Dự đoán trên **Test Set**. <br>- In ra `classification_report` (precision, recall, f1). <br>- In/ Vẽ `confusion_matrix`. <br>- So sánh DT vs MLP và đưa ra insights. | ☐ | Phần insights viết ngay cuối notebook |

### Yêu cầu chung cho **TOÀN BỘ DỰ ÁN** (Do D và E đảm nhiệm)

| Task ID | Yêu cầu | Đã làm? | Ghi chú |
| :--- | :--- | :---: | :--- |
| **3.1** | **Report** <br>- Có Member Information (ID, Full name). <br>- Có Work assignment table (kèm % completion của từng người). <br>- Trình bày thống kê (bảng số) trong PDF. <br>- Xuất file PDF, ko lỗi cắt hình. | ☐ | Dùng Markdown export hoặc Google Docs |
| **3.2** | **Submission** <br>- Nén file đúng format: `StudentID1_StudentID2_etc.zip`. <br>- Nếu >25MB, upload Google Drive (view only). <br>- Code được tổ chức sạch sẽ, Notebook chạy từ A-Z. | ☐ | E chịu trách nhiệm file cuối |

---
