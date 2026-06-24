import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import pandas as pd
import numpy as np

def stratified_split(X, y, val_size=0.2):
    # Thực hiện shuffle + stratified split
    return train_test_split(X, y, test_size=val_size, stratify=y, random_state=42, shuffle=True)

def plot_distribution(y, title, save_path=None):
    # Vẽ biểu đồ cột phân phối class
    plt.figure()
    # ... code vẽ ...
    if save_path: plt.savefig(save_path)

def eval_and_plot(model, X_test, y_test, model_name, save_path=None):
    # In classification report và vẽ confusion matrix
    y_pred = model.predict(X_test)
    print(f"--- {model_name} ---")
    print(classification_report(y_test, y_pred))
    # Vẽ confusion matrix bằng seaborn
    # ...

def load_data_from_kaggle(dataset_name):
    """
    Load dữ liệu từ Kaggle dataset tương ứng.
    dataset_name: 'mnist', 'fashion', 'food'
    Trả về: X_train, y_train, X_test, y_test
    """
    base_path = f"/kaggle/input/{dataset_name}-lab3/"
    
    # Kiểm tra các file có trong thư mục
    files = os.listdir(base_path)
    print("Files in dataset:", files)
    
    # --- MNIST & Fashion-MNIST (thường có train.csv, test.csv) ---
    if 'train.csv' in files and 'test.csv' in files:
        train_df = pd.read_csv(os.path.join(base_path, 'train.csv'))
        test_df = pd.read_csv(os.path.join(base_path, 'test.csv'))
        # Giả sử cột đầu tiên là label
        X_train = train_df.iloc[:, 1:].values
        y_train = train_df.iloc[:, 0].values
        X_test = test_df.iloc[:, 1:].values
        y_test = test_df.iloc[:, 0].values
        return X_train, y_train, X_test, y_test
    
    # --- Food-MNIST (có thể là các file ảnh) ---
    elif 'images' in files and 'labels.csv' in files:
        # Giả sử có thư mục images và file labels.csv
        # Code xử lý ảnh (resize, flatten)
        pass
    
    # --- Trường hợp khác: các thành viên tự implement ---
    else:
        raise NotImplementedError(f"Cấu trúc dataset {dataset_name} chưa được hỗ trợ. Vui lòng kiểm tra và tự load.")

# Hàm split validation
def stratified_split(X, y, val_size=0.2):
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=val_size, stratify=y, random_state=42, shuffle=True
    )
    return X_train, y_train, X_val, y_val

# Tương tự cho fashion và food