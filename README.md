# **Customer Churn Prediction**

## **📜 Project Overview**

Predicting **customer churn** using machine learning to help businesses retain customers and prevent revenue loss.

## **🎯 Goal**

- Identify **high-risk customers** who are likely to churn.
- Provide **data-driven insights** for retention strategies.

---

## **📊 Dataset**

- **Source:** [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Size:** 7,043 customers, 21 features
- **Target Variable:** `Churn` (0 = No, 1 = Yes)

---

## **🛠️ Model Development**

### **Preprocessing Steps**

- 🔹 **One-Hot Encoding** for categorical features.
- 🔹 **Feature Scaling** (Min-Max Normalization).
- 🔹 **Feature Engineering** (tenure category, churn risk score, etc.).

### **Trained Models & Performance**

| Model                   | Accuracy | Precision  | Recall     | F1-Score   | ROC-AUC    |
| ----------------------- | -------- | ---------- | ---------- | ---------- | ---------- |
| **Logistic Regression** | 73.81%   | 50.43%     | 78.34%     | 61.36%     | 84.06%     |
| **Random Forest**       | 79.21%   | 63.73%     | 50.27%     | 56.20%     | 82.12%     |
| **XGBoost**             | 79.56%   | 63.87%     | 52.94%     | 57.89%     | 83.79%     |
| **Tuned XGBoost**       | 80.55%   | **67.48%** | 51.60%     | 58.48%     | **84.66%** |
| **Reduced XGBoost**     | 80.13%   | 66.21%     | 51.34%     | 57.83%     | 84.62%     |
| **SMOTE XGBoost**       | 78.78%   | 59.59%     | **62.30%** | **60.92%** | 84.49%     |

---

## **📌 Feature Importance**

### **Top Factors Affecting Churn:**

1️⃣ **Internet Service (Fiber Optic)** – Higher churn risk.\
2️⃣ **Contract Type (One/Two Year)** – Longer contracts reduce churn.\
3️⃣ **Payment Method (Electronic Check)** – Users paying via e-checks churn more.\
4️⃣ **Internet Service (No Service)** – Different churn behavior.\
5️⃣ **Tenure** – Longer tenure reduces churn likelihood.

---

## **📈 Key Business Insights**

📌 **Retain Fiber Optic Users** → Investigate service quality & pricing.\
📌 **Encourage Annual Contracts** → Offer perks for switching from month-to-month plans.\
📌 **Improve Payment Options** → Customers using **electronic checks churn more**—encourage auto-pay.

---

## **🚀 Model Deployment**

✅ **Best Model for Deployment:** **Tuned XGBoost** (Balanced precision & recall).\
✅ **Deployment Plan:**

- Create a **Streamlit web app** for interactive predictions.
- Host the app on **Streamlit Cloud or Hugging Face Spaces**.

---

## **📎 How to Run This Project Locally**

### **🔹 Install Dependencies**

```bash
pip install -r requirements.txt
```

### **🔹 Run the Notebook**

```bash
jupyter notebook Customer_Churn_Prediction.ipynb
```

### **🔹 Run the Streamlit App**

```bash
streamlit run app.py
```

---

## **📌 Future Improvements**

📌 Fine-tune recall using **cost-sensitive learning**.\
📌 Develop a **real-time API** for churn predictions.\
📌 Use **SHAP values** to improve feature interpretability.

---

## **📄 Credits & Contact**

**Author:** *Manusha Fernando*\
📧 Email: [romanfern@proton.me](mailto\:romanfern@proton.me)\
🔗 GitHub: [Manusha Fernando](https://github.com/ROMANFern)
