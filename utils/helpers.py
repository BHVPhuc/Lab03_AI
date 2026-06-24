import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

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