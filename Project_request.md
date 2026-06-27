CSC14003 _|_ **Introduction to Artificial Intelligence** 

Project 3 

## **Project 3** 

## **Machine Learning** 

## **1 Introduction** 

In this assignment, you are going to explore supervised machine learning by building and evaluating decision trees and neural networks on real-world datasets using `scikit-learn` library. 

The datasets you will be working on include: 

- **The MNIST Dataset** : This dataset is used for classifying handwritten digits from 0 to 9 based on grayscale pixel values of images. Each image has a resolution of 28 _×_ 28 pixels, where each pixel represents the intensity of the handwritten digit. This dataset includes 70,000 samples, consisting of 60,000 training images and 10,000 testing images, with labels corresponding to the digit classes from 0 to 9. 

Please visit: https://github.com/cvdfoundation/mnist 

- **The Fashion-MNIST Dataset** : This dataset is used for classifying images of fashion products into 10 categories such as T-shirt/top, trouser, pullover, dress, coat, sandal, shirt, sneaker, bag, and ankle boot. Similar to MNIST, each image is represented by grayscale pixel values with a resolution of 28 _×_ 28 pixels. This dataset includes 70,000 samples, consisting of 60,000 training images and 10,000 testing images, with labels indicating the corresponding fashion categories. 

Please visit: https://github.com/zalandoresearch/fashion-mnist 

- **The Food-MNIST Dataset** : This dataset is used for classifying food images into 10 different food categories based on visual features extracted from RGB images. The dataset contains 5,000 images in total, with 500 images per class. For each class, 375 images are provided for training and 125 images for testing. The training images were intentionally not fully cleaned and may contain noise such as strong color variations or occasional incorrect labels. All images were rescaled to have a maximum side length of 512 pixels, and labels indicate the corresponding food categories. 

Please visit: https://github.com/srohit0/food mnist 

Faculty of Information Technology, University of Science, VNU-HCM 

Page 1 

CSC14003 _|_ **Introduction to Artificial Intelligence** 

Project 3 

## **2 Specifications** 

You are required to write **Python Notebooks** (.ipynb) and use the `scikit-learn` library to complete the following tasks described for the **MNIST dataset** . For the remaining datasets ( **Fashion MNIST dataset** and **Food MNIST dataset** ), perform similar tasks. 

While there are no strict guidelines for code organization, each task must be clearly documented and fully comply with all specified requirements. 

## **2.1 Preparing the dataset** 

This task sets up the training, validation, and test datasets for the upcoming experiments. 

Note that a test set is already provided and will be used exclusively for experimental evaluation. Using the provided training dataset (include features and labels), prepare the following subsets: 

- `feature_train` : a set of training samples. 

- `label_train` : a set of labels corresponding to the samples in `feature_train` . 

- `feature_val` : a set of validation samples with the same structure as `feature_train` . 

- `label_val` : a set of labels corresponding to the samples in `feature_val` . 

The original training data must be shuffled and then split into training and validation sets using a stratified strategy, with a ratio of **80% for model training and 20% for validation** . All other parameters (if any) should remain at their default settings. 

The provided test set ( `feature_test` , `label_test` ) should not be modified and must only be used for final evaluation. 

**Visualize** the class distributions in the original dataset, the training set, the validation set, and the test set to demonstrate that the data have been appropriately prepared. 

Figure 1: Example for distribution visualization. 

Faculty of Information Technology, University of Science, VNU-HCM 

Page 2 

CSC14003 _|_ **Introduction to Artificial Intelligence** 

Project 3 

## **2.2 Building the decision tree classifier** 

You need to fit an instance of `sklearn.tree.DecisionTreeClassifier` (using information gain) to each training set and visualize the resulting decision tree with Graphviz. 

Figure 2: An example visualization of a decision tree classifier trained on the UCI Diabetes dataset. 

## **2.3 Hyperparameter tuning for decision tree classifier** 

In this task, you are required to tune the hyperparameters of the decision tree classifiers using the prepared **validation set** . 

At a minimum, the following hyperparameters of `DecisionTreeClassifier` must be tuned: 

- `max_depth` , 

- `min_samples_split` , 

- `min_samples_leaf` . 

For each hyperparameter configuration, train the model on the training set and evaluate its accuracy on the validation set. Select the model that achieves the best validation accuracy and report the corresponding hyperparameter values. 

This model will be compared with the neural network model in the subsequent section using a final evaluation on the test set. 

Faculty of Information Technology, University of Science, VNU-HCM 

Page 3 

CSC14003 _|_ **Introduction to Artificial Intelligence** 

Project 3 

## **2.4 Building the neural network classifier** 

You need to fit an instance of `sklearn.neural_network.MLPClassifier` to prepared training set and evaluate its accuracy on the validation set. 

The neural network must contain at least one hidden layer, a nonlinear activation function, and a suitable optimization algorithm for training. All other parameters can be kept at their default unless otherwise specified. 

You must explicitly state the chosen architecture and key hyperparameters, such as the number of hidden layers, the number of neurons per layer, the activation function, the learning rate strategy, and the maximum number of training iterations in the report. 

The trained neural network model will be used for comparison with the decision tree classifier in the final evaluation on the test set. 

## **2.5 Performance evaluation and comparison** 

Predict the labels of the samples in the test set using the decision tree classifier and neural network. Generate evaluation results with `classification_report` and `confusion_matrix` . 

Figure 3: An example of the classification report and confusion matrix for a decision tree model trained on the UCI Diabetes dataset. 

How do you interpret the classification report and the confusion matrix? Based on the results, compare the performance of these models and provide detailed insights. 

Faculty of Information Technology, University of Science, VNU-HCM 

Page 4 

CSC14003 _|_ **Introduction to Artificial Intelligence** 

Project 3 

## **3 Requirements** 

## **3.1 Report** 

The report must include the following sections: 

- Member information (Student ID, full name, etc.). 

- Work assignment table, which includes information on each task assigned to team members, along with the completion rate of each member compared to the assigned tasks. For example, student A has a percentage of completion 90% and the group work has a total score of 9.0, then A receives a score of 9 _._ 0 _∗_ 90% = 8 _._ 1. 

- All visualizations must be presented in the .ipynb file, while statistical results and insights must be presented in the report. 

- The report needs to be well-formatted and exported to PDF. If there are figures cut off by the page break, etc., points will be deducted. 

- References (if any). 

## **3.2 Submission** 

Please follow to the following submission guidelines: 

- All reports, code, etc., must be contributed in the form of a compressed file (.zip, .rar, .7z) and named according to the format: `StudentID1_StudentID2_etc.zip/.rar/.7z` . 

- If the compressed file is larger than 25MB, upload it to Google Drive and share it via a link. **Absolutely no modifications are allowed after the deadline** . 

Example details of the directory organization: 

```
StudentID1StudentID2...
```

```
Source
MNIST.ipynb
FashionMNIST.ipynb
FoodMNIST.ipynb
...
```

```
Report.pdf
```

Faculty of Information Technology, University of Science, VNU-HCM 

Page 5 

CSC14003 _|_ **Introduction to Artificial Intelligence** 

Project 3 

## **4 Assessment** 

The detailed assessment criteria for this project are outlined as follows: 

|**No.**|**Criteria**|**Score**|
|---|---|---|
|1|Analysis of the MNIST dataset.|30%|
|2|Analysis of the Fashion MNIST dataset.|30%|
|3|Analysis of the Food MNIST dataset.|30%|
|4|Well-structured and formatted notebooks.|10%|
||**Total**|**100%**|



The detailed assessment criteria for each dataset are outlined as follows: 

|**No.**|**Criteria**|**Score**|
|---|---|---|
|1|Prepare the dataset.|20%|
|2|Building the decision tree classifer.|20%|
|3|Hyperparameter tuning for decision tree classifer.|20%|
|4|Building the neural network classifer.|20%|
|5|Performance evaluation and comparison.||
||- Classifcation report and confusion matrix.|10%|
||- Insights.|10%|
||**Total**|**100%**|



## **5 Notices** 

Please pay attention to the following notices: 

- This is a **GROUP** assignment. 

- Duration: about 3 weeks. 

- AI tools are **not restricted** ; however, students should use them wisely. Lab instructors have the right to conduct additional oral interviews to assess their knowledge of the project. 

- Any form of plagiarism, dishonesty, or misconduct will result in a grade of zero for the course. 

The end. 

Faculty of Information Technology, University of Science, VNU-HCM 

Page 6 

