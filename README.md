# Bank Customer Churn Prediction (MLP)

A Multilayer Perceptron (MLP) neural network built with TensorFlow/Keras to predict bank customer churn, including data exploration, preprocessing, class imbalance handling (SMOTE), architecture and hyperparameter experimentation, model evaluation, and a business-oriented risk segmentation.

## Project Overview

The notebook walks through the full pipeline:

1. **Phase 1 -- Exploratory Data Analysis (EDA):** structure, missing values, duplicates, descriptive statistics, univariate/bivariate analysis, correlations, and outlier detection.
2. **Phase 2 -- Data Preprocessing:** encoding categorical variables, winsorization of outliers, feature/target split, stratified train/test split, and feature scaling.
3. **Phase 3 -- Class Imbalance:** analysis of the churn class imbalance and oversampling with SMOTE (67/33 ratio, `sampling_strategy=0.5`).
4. **Phase 4 -- MLP Design:** building, compiling, and configuring the network, including regularization checks.
5. **Phase 5 -- Training and Hyperparameter Tuning:** architecture experiments, learning curves, and hyperparameter search.
6. **Phase 6 -- Final Evaluation:** confusion matrix, ROC curve, AUC-ROC, and decision-threshold analysis.
7. **Phase 7 -- Risk Analysis:** segmenting customers into Low/Medium/High churn-risk categories for business use.

## Results Summary

- **AUC-ROC:** 84.43%
- **Accuracy:** 82.25%
- **Precision:** 55.70%
- **Recall:** 62.41%
- The High Risk segment (probability >= 0.60) concentrates **63.9% of actual churn**, about 3x the dataset's base churn rate (20.37%).

## Dataset

This project uses the **"Churn Modelling"** dataset (Bank Customer Churn, 10,000 rows / 14 columns), originally published as part of the "Deep Learning A-Z" course by SuperDataScience / filippoo on Kaggle:

- https://www.kaggle.com/datasets/filippoo/deep-learning-az-ann

To run the notebook locally:

1. Download `Churn_Modelling.csv` from the link above.
2. Place it inside the `data/` folder, so the path matches:
   ```
   data/Churn_Modelling.csv
   ```

The dataset is **not included** in this repository.

## Setup

```bash
pip install -r requirements.txt
```

Then open `churn-bancario-mlp.ipynb` in Jupyter Notebook / JupyterLab / VS Code.

## References

- Bhuria et al. (2025)
- Suguna et al. (2025)
- Li (2024)
- Rahman & Kumar (2020)
