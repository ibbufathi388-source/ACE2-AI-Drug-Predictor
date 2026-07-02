# 🧬 ACEPredict AI

> AI-Powered Drug Binding Affinity Prediction using Machine Learning and Explainable AI

---

## 📖 Project Overview

ACEPredict AI is a machine learning-based web application developed to predict the binding affinity of drugs against ACE gene mutations.

This project combines **bioinformatics**, **cheminformatics**, **machine learning**, and **explainable AI (SHAP)** to identify potential drug–mutation interactions.

The prediction model uses an **Extra Trees Regressor**, optimized through hyperparameter tuning and validated using cross-validation.

---

# 🚀 Features

- 🧬 Predict drug binding affinity against ACE mutations
- 💊 Interactive drug selection
- 🤖 Extra Trees Machine Learning model
- 📊 SHAP Explainable AI
- 📈 Model comparison and evaluation
- 🎯 Hyperparameter optimization
- 📄 Prediction report generation
- 🌐 Streamlit web application

---

# 🧠 Workflow

```text
Mutation Dataset
        │
Drug Dataset
        │
Feature Engineering
        │
Dataset Preparation
        │
Machine Learning
        │
Hyperparameter Tuning
        │
Cross Validation
        │
Extra Trees Regressor
        │
SHAP Explainability
        │
Prediction Dashboard
```

---

# 📂 Project Structure

```text
ACE2_AI_Project
│
├── Data
│   ├── 01_Mutations.xlsx
│   ├── 02_AminoAcid_Properties.xlsx
│   ├── 03_Drugs.xlsx
│   └── 04_Docking_Results.xlsx
│
├── Models
│   ├── best_model.pkl
│   └── Feature_Importance.xlsx
│
├── Output
│   ├── Final_AI_Dataset.xlsx
│   ├── Prediction_Report.xlsx
│   ├── SHAP_Feature_Importance.xlsx
│   ├── Model_Comparison.xlsx
│   ├── CrossValidation_Results.xlsx
│   └── Best_Parameters.xlsx
│
├── Streamlit_App
│   ├── app.py
│   └── requirements.txt
│
└── Notebooks
```

---

# 📊 Model Performance

| Model | MAE | RMSE | R² |
|------|------|------|------|
| Random Forest | 0.637 | 0.888 | 0.974 |
| Gradient Boosting | 0.451 | 0.712 | 0.983 |
| ⭐ Extra Trees | **0.334** | **0.471** | **0.993** |

---

# 🔬 Explainable AI

This project uses **SHAP (SHapley Additive exPlanations)** to understand how different mutation and drug features influence the prediction.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SHAP
- Streamlit
- Joblib
- RDKit
- Google Colab

---

# ⚙️ Installation

```bash
git clone https://github.com/ibbufathi388-source/ACEPredict-AI.git
```

```bash
cd ACEPredict-AI
```

```bash
pip install -r ACE2_AI_Project/Streamlit_App/requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run ACE2_AI_Project/Streamlit_App/app.py
```

---

# 🔮 Future Improvements

- Deep Learning models
- Protein structure visualization
- Molecular docking integration
- Permanent cloud deployment
- Advanced SHAP dashboard
- Multi-target drug prediction
- Modern fluorescent UI

---

# 👩‍💻 Developer

**Hajeera**

B.Tech Biotechnology

AI for Drug Discovery & Bioinformatics

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
