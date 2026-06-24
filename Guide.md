# 📌 HƯỚNG DẪN LÀM BÀI CHO THÀNH VIÊN

**1. Clone repo và chuyển nhánh:**

```bash
git clone https://<username>:<token>@github.com/yourteam/AI_Project3.git
cd AI_Project3
git checkout feature/mnist   # (A) hoặc fashion (B), food (C)
```

**2. Tạo Kaggle Notebook và gắn dataset:**

- Đăng nhập Kaggle, tạo Notebook mới.
- Ở bên phải chọn "Add Data" -> nhập tên dataset đã được share (ví dụ: mnist-lab3).

**3. Clone repo và cài đặt trong Notebook:**

Trong cell đầu tiên của Notebook, chạy đoạn mã sau:

```python
# Clone repo (thay token của bạn)
!git clone https://<username>:<token>@github.com/yourteam/AI_Project3.git
%cd AI_Project3
!git checkout feature/mnist   # (A)

# Cài Graphviz
!apt-get install graphviz -y
!pip install graphviz
```

Viết code trong file `notebooks/mnist.ipynb` (hoặc `fashion`/`food`). Sử dụng các hàm trong `utils/helpers.py`.

**4. Commit và push sau mỗi task:**

```bash
!git add notebooks/mnist.ipynb
!git commit -m "Hoàn thành Task 2.1"
!git push origin feature/mnist
```

Cập nhật tiến độ: Trong file `PROGRESS.md`, đánh dấu `[x]` vào checklist của mình.

**5. 📈 Tạo file PROGRESS.md ở root repo**

Nội dung tham khảo:

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
...

## Food-MNIST (Thành viên C)
- [ ] 2.1 Prepare dataset
...
```

**6. ⏰ Lịch họp và điểm danh**

- Họp nhanh lúc 8h sáng mai (hoặc giờ bạn chọn) qua Zoom/Google Meet để review tiến độ và giải đáp.
- **Deadline commit lần 1:** Trước 20h tối ngày đầu tiên, mỗi người commit ít nhất hoàn thành Task 2.1 và 2.2.

**✅ Checklist việc bạn cần làm NGAY**

| Hạng mục | Đã làm? | Ghi chú |
| :--- | :---: | :--- |
| Lấy link 3 dataset và cập nhật `README.md` | ☐ | |
| Viết hàm load data mẫu trong `utils/load_data.py` | ☐ | |
| Push code skeleton lên GitHub (`README.md`, helpers, requirements, `PROGRESS.md`) | ☐ | |
| Tạo 3 nhánh và push lên GitHub | ☐ | |
| Gửi hướng dẫn chi tiết cho nhóm qua tin nhắn/nhóm chat | ☐ | |
| Tổ chức họp nhanh 15 phút để thống nhất | ☐ | |

**💡 Lưu ý quan trọng**

- **Cấu trúc dataset:** Các thành viên cần kiểm tra cấu trúc thực tế của dataset trên Kaggle (bằng cách xem tab "Data" của dataset). Có thể tùy chỉnh hàm load phù hợp.
- **Xử lý Food-MNIST:** Do ảnh `512x512`, thành viên C nên resize về `64x64` hoặc dùng PCA để tránh quá tải. Nhắc họ trong buổi họp.
- **Conflict khi merge:** Khi các nhánh hoàn thành, bạn sẽ merge từng nhánh vào `main` và giải quyết conflict (nếu có) để tạo code cuối cùng.