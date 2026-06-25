import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# --------------------------------------------
# 0. HÀM ĐỌC FILE IDX (MNIST)
# --------------------------------------------

def read_idx_file(filepath):
    """Đọc file IDX (định dạng MNIST) đã giải nén."""
    with open(filepath, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        if magic == 2051:  # Hình ảnh
            num_images = int.from_bytes(f.read(4), 'big')
            rows = int.from_bytes(f.read(4), 'big')
            cols = int.from_bytes(f.read(4), 'big')
            data = np.frombuffer(f.read(), dtype=np.uint8)
            data = data.reshape(num_images, rows * cols)
        elif magic == 2049:  # Nhãn
            num_labels = int.from_bytes(f.read(4), 'big')
            data = np.frombuffer(f.read(), dtype=np.uint8)
        else:
            raise ValueError(f"Magic number {magic} không hợp lệ")
        return data

# --------------------------------------------
# 1. HÀM TẢI DỮ LIỆU TỪ KAGGLE
# --------------------------------------------

def load_mnist_data(base_path="/kaggle/input/datasets/vnhphcbuhunh/the-mnist-dataset"):
    """Tải dữ liệu MNIST từ Kaggle dataset (định dạng IDX)."""
    X_train = read_idx_file(os.path.join(base_path, "train-images-idx3-ubyte", "train-images.idx3-ubyte"))
    y_train = read_idx_file(os.path.join(base_path, "train-labels-idx1-ubyte", "train-labels.idx1-ubyte"))
    X_test  = read_idx_file(os.path.join(base_path, "t10k-images-idx3-ubyte", "t10k-images.idx3-ubyte"))
    y_test  = read_idx_file(os.path.join(base_path, "t10k-labels-idx1-ubyte", "t10k-labels.idx1-ubyte"))
    return X_train, y_train, X_test, y_test

# --------------------------------------------
# 2. HÀM CHIA DỮ LIỆU THEO PHÂN TẦNG
# --------------------------------------------

def stratified_split(X, y, val_size=0.2, random_state=42):
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=val_size, stratify=y, random_state=random_state, shuffle=True
    )
    return X_train, y_train, X_val, y_val

# --------------------------------------------
# 3. HÀM VẼ PHÂN PHỐI LỚP
# --------------------------------------------

def plot_class_distribution(y, title="Class Distribution", save_path=None, figsize=(8,5)):
    plt.figure(figsize=figsize)
    sns.countplot(x=y, palette='viridis')
    plt.title(title, fontsize=14)
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Đã lưu biểu đồ vào {save_path}")
    plt.show()

# --------------------------------------------
# 4. HÀM ĐÁNH GIÁ MÔ HÌNH
# --------------------------------------------

def evaluate_model(model, X_test, y_test, model_name="Model", save_cm_path=None, class_names=None):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n{'='*50}")
    print(f"📊 KẾT QUẢ ĐÁNH GIÁ - {model_name}")
    print(f"{'='*50}")
    print(f"Độ chính xác (Accuracy): {accuracy:.4f}")
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    if save_cm_path:
        plt.savefig(save_cm_path, dpi=150, bbox_inches='tight')
        print(f"Đã lưu confusion matrix vào {save_cm_path}")
    plt.show()
    return y_pred, accuracy

# --------------------------------------------
# 5. HÀM TIỆN ÍCH BỔ SUNG
# --------------------------------------------

def plot_multiple_distributions(datasets, titles, save_path=None):
    n = len(datasets)
    fig, axes = plt.subplots(1, n, figsize=(5*n, 5))
    if n == 1:
        axes = [axes]
    for i, (y, title) in enumerate(zip(datasets, titles)):
        sns.countplot(x=y, ax=axes[i], palette='viridis')
        axes[i].set_title(title)
        axes[i].set_xlabel("Class")
        axes[i].set_ylabel("Count")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Đã lưu biểu đồ tổng hợp vào {save_path}")
    plt.show()

def save_results_to_csv(results, filename="results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Đã lưu kết quả vào {filename}")