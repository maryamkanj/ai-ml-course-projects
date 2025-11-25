# Titanic Survival Classifier

This project demonstrates a comprehensive comparison of Machine Learning models on the Titanic dataset to predict passenger survival. It includes model training, hyperparameter tuning, and evaluation using multiple metrics and visualizations.

## Project Overview

The goal of this project is to classify passengers as survived or not based on their features using a variety of ML models with optimized hyperparameters.

### Models Implemented:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- AdaBoost
- XGBoost

## Technical Implementation

### Workflow:
1. **Data Preparation**: Loaded preprocessed Titanic dataset (`preprocessed_train.csv`)
2. **Train-Test Split**: 80-20 split with stratified sampling to maintain class distribution
3. **Model Initialization**: Six classifiers with appropriate parameters
4. **Hyperparameter Tuning**:
   - **GridSearchCV** for KNN, Decision Tree, Random Forest, and AdaBoost
   - **RandomizedSearchCV** for XGBoost
   - 5-fold cross-validation for all models
5. **Model Evaluation**:
   - Accuracy and F1 scores
   - Classification reports
   - Confusion matrices with visualizations

## Skills Demonstrated

- **Data Preprocessing**: Handling structured data with pandas and NumPy
- **Model Training**: Implementing multiple classical ML algorithms
- **Hyperparameter Optimization**: Using GridSearchCV and RandomizedSearchCV with custom parameter grids
- **Model Evaluation**: Comprehensive assessment using accuracy, F1 score, classification reports, and confusion matrices
- **Data Visualization**: Creating confusion matrix heatmaps with seaborn
- **Comparative Analysis**: Systematic model comparison for practical decision-making
