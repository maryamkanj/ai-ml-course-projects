# Titanic Survival Classifier

This project demonstrates a **comparison of classic Machine Learning models** on the Titanic dataset to predict passenger survival.
It includes model training, hyperparameter tuning, and evaluation using multiple metrics and visualizations.

---

## Project Overview

The goal of this project is to **classify passengers as survived or not** based on their features using a variety of ML models.

Models explored:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* AdaBoost
* XGBoost

Key workflow steps:

1. Load and preprocess the dataset (`preprocessed_train.csv`)
2. Split the data into training and testing sets
3. Initialize models with default parameters
4. Perform **GridSearchCV / RandomizedSearchCV** for hyperparameter tuning
5. Train all models and select best parameters
6. Evaluate models on test data using:

   * Accuracy
   * F1-score
   * Confusion matrices
7. Compare model performance to identify the best classifier

---

## What I Implemented

* Imported and prepared the Titanic dataset with pandas and NumPy
* Split data into training and testing sets using `train_test_split`
* Initialized multiple classifiers and defined hyperparameter grids
* Used **GridSearchCV** (and RandomizedSearchCV for XGBoost) to find optimal parameters
* Trained and evaluated each model
* Printed **classification reports** and plotted **confusion matrices** for each model
* Summarized **accuracy** and **F1 scores** in a final results table

---

## Skills Demonstrated

* Tabular data preprocessing and handling
* Training multiple classical ML models
* Hyperparameter tuning using GridSearchCV and RandomizedSearchCV
* Model evaluation using accuracy, F1 score, classification reports, and confusion matrices
* Visualizing performance with seaborn heatmaps
* Comparing models for practical decision-making

---

This project is part of my hands-on **AI & Machine Learning learning path**, focusing on **classic ML algorithms and model evaluation techniques**.
