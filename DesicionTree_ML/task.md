# Machine Learning: Diabetes Prediction Using Decision Trees

## Overview
This project focuses on building a binary classification model using **Scikit-learn** to predict whether a patient has diabetes based on diagnostic measurements. 

The dataset (`diabetes.csv`) consists of several medical features (such as pregnancy count, BMI, insulin levels, and age) and a target variable (`Outcome`). The goal is to construct a **Decision Tree Classifier**, experiment with hyperparameter tuning, analyze model stability across train/test splits, and optimize overall predictive accuracy beyond baseline benchmarks (~74–75%).

---

## Technical Approach & Analysis

The project evaluates key decision tree mechanics and validation strategies to ensure the model generalizes well to unseen data rather than overfitting to a specific random seed:

### 1. Hyperparameter Tuning & Sensitivity Analysis
* Evaluates the impact of core `DecisionTreeClassifier` parameters (e.g., `max_depth`, `min_samples_split`, `min_samples_leaf`, and `criterion`).
* Identifies which parameters have the strongest influence on model performance versus those with minimal impact.

### 2. Validation & Data Splitting
* Analyzes how varying the train/test split ratio affects evaluation metrics, specifically tracking the relationship between **Accuracy** and **Precision**.
* Plots metric trends across different data proportions to identify the optimal split for model evaluation.

### 3. Feature Selection & Tree Visualization
* Tests feature subsets to determine the most informative diagnostic combination for prediction.
* Extracts and visualizes the final decision tree structure to interpret the decision boundaries learned by the model.

---

## Technical Stack & Libraries
* **Language:** Python 3.x
* **Machine Learning:** `scikit-learn` (`DecisionTreeClassifier`, `train_test_split`, `metrics`)
* **Data Processing:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `seaborn`

---

## Repository Structure

```text
decision_tree_diabetes/
├── README.md                   # Setup, execution instructions, and summary of findings
├── task.md                     # Project scope and analysis guidelines (This file)
├── diabetes.csv                # Medical diagnostic dataset
├── diabetes_prediction.py      # Python script for training, tuning, and evaluation
