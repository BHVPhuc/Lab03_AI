Tôi sẽ sửa lại nội dung hướng dẫn, loại bỏ token trong lệnh clone và điều chỉnh một số điểm cho phù hợp với thực tế collaboration trên repository private:

---

# 📌 HƯỚNG DẪN LÀM BÀI CHO THÀNH VIÊN

## 1. Clone repository và chuyển nhánh

**Clone repo về máy tính cá nhân hoặc trên Kaggle Notebook:**

```bash
# Clone bằng HTTPS (sẽ yêu cầu nhập username/password GitHub)
git clone https://github.com/yourteam/AI_Project3.git
cd AI_Project3

# Chuyển sang nhánh của mình
git checkout feature/mnist   # (Thành viên A)
# hoặc
git checkout feature/fashion # (Thành viên B)
# hoặc
git checkout feature/food    # (Thành viên C)
# hoặc
git checkout main            # (Thành viên D - báo cáo)
```

> 💡 **Lưu ý:** Nếu bạn dùng 2FA trên GitHub, hãy dùng **Personal Access Token** làm mật khẩu khi được yêu cầu. Token tạo ở: GitHub Settings → Developer settings → Personal access tokens → Generate new token (tick `repo`).

---

## 2. Tạo Kaggle Notebook và gắn dataset

1. Đăng nhập [Kaggle.com](https://www.kaggle.com/), tạo **New Notebook**.
2. Ở bên phải màn hình, chọn **"Add Data"** → tìm dataset tương ứng đã được tạo:
   - Thành viên A: Tìm `mnist-lab3`
   - Thành viên B: Tìm `fashion-lab3`
   - Thành viên C: Tìm `food-lab3`
3. Đợi dataset được mount vào Notebook (xuất hiện ở phần **Input** bên phải).

---

## 3. Clone repo và cài đặt trong Kaggle Notebook

Trong cell đầu tiên của Notebook, chạy đoạn mã sau **(không cần token trong URL)**:

```python
# Clone repository (không cần token - Git sẽ hỏi username/password)
!git clone https://github.com/yourteam/AI_Project3.git
%cd AI_Project3

# Chuyển sang nhánh của bạn
!git checkout feature/mnist   # (A) hoặc fashion (B), food (C)

# Cài đặt Graphviz để vẽ cây quyết định
!apt-get install graphviz -y
!pip install graphviz

# Cài các thư viện cần thiết (nếu chưa có)
!pip install -r requirements.txt
```

> ⚠️ **Quan trọng:** Nếu bạn dùng token trong lệnh clone, token sẽ hiển thị trong notebook và có thể bị lộ. **Không khuyến khích** làm điều này. Thay vào đó, hãy clone bằng HTTPS và nhập username/password khi được yêu cầu.

**Cấu hình Git lần đầu (nếu cần):**

```python
!git config --global user.name "Tên của bạn"
!git config --global user.email "email@example.com"
```

---

## 4. Làm việc và commit code

### Viết code

- Mở file notebook của bạn trong thư mục `notebooks/`:
  - `notebooks/mnist.ipynb` (A)
  - `notebooks/fashion.ipynb` (B)
  - `notebooks/food.ipynb` (C)

- Sử dụng các hàm dùng chung trong `utils/helpers.py`:
  ```python
  from utils.helpers import stratified_split, plot_distribution, evaluate_model
  ```

- **Lưu ảnh kết quả** vào thư mục `figures/` với tên chuẩn (ví dụ: `mnist_tree.png`, `fashion_cm.png`) để thành viên D dễ lấy vào báo cáo.

### Commit và push sau mỗi task hoàn thành

Sau khi hoàn thành một task (ví dụ Task 2.1), commit và push lên nhánh của bạn:

```python
# Thêm file đã sửa
!git add notebooks/mnist.ipynb   # hoặc fashion/food

# Commit với message rõ ràng
!git commit -m "Hoàn thành Task 2.1 - Prepare dataset"

# Push lên nhánh của bạn
!git push origin feature/mnist   # hoặc feature/fashion, feature/food
```

---

## 5. Cập nhật tiến độ trong PROGRESS.md

Sau mỗi task hoàn thành, vào file `PROGRESS.md` ở root repo, đánh dấu `[x]` vào checklist của mình:

```markdown
# Progress Tracking

## MNIST (Thành viên A)
- [x] 2.1 Prepare dataset
- [ ] 2.2 Build Decision Tree + visualize
- [ ] 2.3 Hyperparameter tuning
- [ ] 2.4 Build Neural Network
- [ ] 2.5 Evaluation & insights
...
```

Commit file này sau khi cập nhật:

```python
!git add PROGRESS.md
!git commit -m "Cập nhật tiến độ: Hoàn thành Task 2.1"
!git push origin feature/mnist
```

---

## 6. 📈 Tạo file PROGRESS.md ở root repo (Đã có sẵn, chỉ cần cập nhật)

Nội dung tham khảo (trưởng nhóm đã tạo sẵn):

```markdown
# Progress Tracking

## MNIST (Thành viên A)
- [ ] 2.1 Prepare dataset
- [ ] 2.2 Build Decision Tree + visualize
- [ ] 2.3 Hyperparameter tuning
- [ ] 2.4 Build Neural Network
- [ ] 2.5 Evaluation & insights

## Fashion-MNIST (Thành viên B)
- [ ] 2.1 Prepare dataset
- [ ] 2.2 Build Decision Tree + visualize
- [ ] 2.3 Hyperparameter tuning
- [ ] 2.4 Build Neural Network
- [ ] 2.5 Evaluation & insights

## Food-MNIST (Thành viên C)
- [ ] 2.1 Prepare dataset
- [ ] 2.2 Build Decision Tree + visualize
- [ ] 2.3 Hyperparameter tuning
- [ ] 2.4 Build Neural Network
- [ ] 2.5 Evaluation & insights
```

---

## 7. ⏰ Lịch họp và điểm danh

- **Họp nhanh:** 8h sáng mai (hoặc giờ thống nhất) qua Zoom/Google Meet để review tiến độ và giải đáp thắc mắc.
- **Deadline commit lần 1:** Trước 20h tối ngày đầu tiên, mỗi người commit ít nhất hoàn thành **Task 2.1** và **Task 2.2**.
- **Deadline hoàn thành toàn bộ:** 10h sáng ngày thứ 2 (để D tổng hợp báo cáo, E kiểm tra và nộp).

---

## 📌 Lưu ý quan trọng cho từng dataset

| Dataset | Lưu ý đặc biệt |
| :--- | :--- |
| **MNIST** | Dữ liệu sạch, kích thước 28x28, chạy nhanh. |
| **Fashion-MNIST** | Tương tự MNIST, nhưng khó phân loại hơn (đặc biệt là shirt vs pullover). |
| **Food-MNIST** | **Quan trọng:** Ảnh 512x512 rất lớn! Cần **resize về 64x64** hoặc dùng **PCA** để giảm chiều ngay sau khi load data, tránh quá tải bộ nhớ và timeout. |

---

## ✅ Checklist việc bạn cần làm NGAY (Dành cho thành viên)

| Hạng mục | Đã làm? | Ghi chú |
| :--- | :---: | :--- |
| Clone repo và chuyển nhánh đúng | ☐ | |
| Tạo Kaggle Notebook và gắn dataset | ☐ | |
| Cài đặt Graphviz và dependencies | ☐ | |
| Mở file notebook của mình và bắt đầu code | ☐ | |
| Commit sau mỗi task hoàn thành | ☐ | |
| Cập nhật PROGRESS.md sau mỗi task | ☐ | |
| Tham gia họp nhóm đúng giờ | ☐ | |

---

**🔗 Link hữu ích:**

- Repository GitHub: `https://github.com/yourteam/AI_Project3`
- Kaggle Dataset MNIST: `https://www.kaggle.com/datasets/yourusername/mnist-lab3`
- Kaggle Dataset Fashion: `https://www.kaggle.com/datasets/yourusername/fashion-lab3`
- Kaggle Dataset Food: `https://www.kaggle.com/datasets/yourusername/food-lab3`

---

**Chúc các bạn làm bài hiệu quả! 🚀**