# utils/helpers.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# --------------------------------------------
# 1. HÀM TẢI DỮ LIỆU TỪ KAGGLE (có thể tùy chỉnh)
# --------------------------------------------

def load_mnist_data(base_path="/kaggle/input/mnist-lab3"):
    """
    Tải dữ liệu MNIST từ thư mục Kaggle.
    Giả định có 2 file: train.csv và test.csv, cột đầu tiên là 'label'.
    """
    train_df = pd.read_csv(os.path.join(base_path, 'train.csv'))
    test_df = pd.read_csv(os.path.join(base_path, 'test.csv'))
    
    # Tách features và labels
    X_train = train_df.drop('label', axis=1).values
    y_train = train_df['label'].values
    X_test = test_df.drop('label', axis=1).values
    y_test = test_df['label'].values
    
    return X_train, y_train, X_test, y_test


def load_fashion_data(base_path="/kaggle/input/fashion-lab3"):
    """
    Tải dữ liệu Fashion-MNIST từ thư mục Kaggle.
    Cấu trúc tương tự MNIST.
    """
    train_df = pd.read_csv(os.path.join(base_path, 'train.csv'))
    test_df = pd.read_csv(os.path.join(base_path, 'test.csv'))
    
    X_train = train_df.drop('label', axis=1).values
    y_train = train_df['label'].values
    X_test = test_df.drop('label', axis=1).values
    y_test = test_df['label'].values
    
    return X_train, y_train, X_test, y_test


def load_food_data(base_path="/kaggle/input/food-lab3"):
    """
    Tải dữ liệu Food-MNIST từ thư mục Kaggle.
    Lưu ý: Ảnh 512x512 có thể gây OOM, cần resize hoặc PCA sau khi tải.
    Giả định có file train.csv và test.csv (hoặc tên khác).
    """
    train_df = pd.read_csv(os.path.join(base_path, 'train.csv'))
    test_df = pd.read_csv(os.path.join(base_path, 'test.csv'))
    
    X_train = train_df.drop('label', axis=1).values
    y_train = train_df['label'].values
    X_test = test_df.drop('label', axis=1).values
    y_test = test_df['label'].values
    
    return X_train, y_train, X_test, y_test


def load_data_generic(dataset_name, base_path=None):
    """
    Hàm tổng quát dùng để load bất kỳ dataset nào.
    Nếu base_path không được cung cấp, tự tạo theo tên.
    """
    if base_path is None:
        base_path = f"/kaggle/input/{dataset_name}-lab3"
    
    # Tự động phát hiện file CSV (có thể là train.csv, test.csv)
    train_file = os.path.join(base_path, 'train.csv')
    test_file = os.path.join(base_path, 'test.csv')
    
    if os.path.exists(train_file) and os.path.exists(test_file):
        train_df = pd.read_csv(train_file)
        test_df = pd.read_csv(test_file)
        # Giả định cột label là 'label' hoặc cột cuối cùng
        if 'label' in train_df.columns:
            y_train = train_df['label'].values
            X_train = train_df.drop('label', axis=1).values
        else:
            # Nếu không có cột label, giả định cột cuối là label
            y_train = train_df.iloc[:, -1].values
            X_train = train_df.iloc[:, :-1].values
        
        if 'label' in test_df.columns:
            y_test = test_df['label'].values
            X_test = test_df.drop('label', axis=1).values
        else:
            y_test = test_df.iloc[:, -1].values
            X_test = test_df.iloc[:, :-1].values
        
        return X_train, y_train, X_test, y_test
    else:
        raise FileNotFoundError(f"Không tìm thấy train.csv hoặc test.csv trong {base_path}")


# --------------------------------------------
# 2. HÀM CHIA DỮ LIỆU THEO PHÂN TẦNG
# --------------------------------------------

def stratified_split(X, y, val_size=0.2, random_state=42):
    """
    Chia dữ liệu thành tập train và validation theo chiến lược phân tầng (stratified).
    Giữ nguyên tỉ lệ các lớp trong cả hai tập.
    
    Parameters:
        X, y: features và labels
        val_size: tỉ lệ validation (mặc định 0.2)
        random_state: seed cho reproducible
    
    Returns:
        X_train, y_train, X_val, y_val
    """
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, 
        test_size=val_size, 
        stratify=y, 
        random_state=random_state,
        shuffle=True
    )
    return X_train, y_train, X_val, y_val


# --------------------------------------------
# 3. HÀM VẼ PHÂN PHỐI LỚP
# --------------------------------------------

def plot_class_distribution(y, title="Class Distribution", save_path=None, figsize=(8,5)):
    """
    Vẽ biểu đồ cột thể hiện phân phối số lượng mẫu theo từng lớp.
    
    Parameters:
        y: nhãn (array-like)
        title: tiêu đề của biểu đồ
        save_path: đường dẫn để lưu ảnh (nếu None thì không lưu)
        figsize: kích thước figure
    """
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
# 4. HÀM ĐÁNH GIÁ MÔ HÌNH (CHUNG)
# --------------------------------------------

def evaluate_model(model, X_test, y_test, model_name="Model", save_cm_path=None, class_names=None):
    """
    In ra Classification Report và vẽ Confusion Matrix cho mô hình đã train.
    
    Parameters:
        model: mô hình đã fit (có method .predict)
        X_test, y_test: dữ liệu test
        model_name: tên mô hình (để in ra tiêu đề)
        save_cm_path: đường dẫn để lưu ảnh confusion matrix (nếu None thì không lưu)
        class_names: danh sách tên các lớp (nếu None thì dùng số 0..n-1)
    
    Returns:
        y_pred: dự đoán của mô hình
        accuracy: độ chính xác trên test
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n{'='*50}")
    print(f"📊 KẾT QUẢ ĐÁNH GIÁ - {model_name}")
    print(f"{'='*50}")
    print(f"Độ chính xác (Accuracy): {accuracy:.4f}")
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))
    
    # Vẽ confusion matrix
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
    """
    Vẽ nhiều biểu đồ phân phối lớp trên cùng một figure (dạng lưới).
    
    Parameters:
        datasets: list của các y (nhãn)
        titles: list tiêu đề tương ứng
        save_path: đường dẫn lưu ảnh
    """
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


# --------------------------------------------
# 6. HÀM LƯU KẾT QUẢ (DÙNG CHO BÁO CÁO)
# --------------------------------------------

def save_results_to_csv(results, filename="results.csv"):
    """
    Lưu bảng so sánh kết quả (accuracy, params...) vào CSV để D tổng hợp.
    """
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Đã lưu kết quả vào {filename}")