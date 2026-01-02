# EV-Charging-Analysis-Prediction-
An end-to-end Data Science project that analyzes EV charging session data, builds predictive machine learning models, and deploys them through an interactive Streamlit web application.


## 📌 Project Overview

With the growing adoption of Electric Vehicles (EVs), understanding charging behavior is essential for both users and operators.
This project focuses on analyzing EV charging session data and predicting:

* 💰 Estimated cost to fully charge an EV
* ⏱ Time required to fully charge
* 🛣 Predicted driving distance after charging

The project covers the **entire data science lifecycle**, from data preprocessing to model deployment.

---

## 🧠 Key Features

* Cleaned and preprocessed real-world EV charging data
* Removed outliers using statistical techniques
* Feature engineering on charging and vehicle attributes
* Built **three separate machine learning models**:

  * Charging cost prediction
  * Charging time prediction
  * Driving distance prediction
* Deployed predictions via a **Streamlit-based UI**
* Simple and user-friendly input workflow

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Visualization:** Matplotlib, Seaborn
* **Web App / UI:** Streamlit

---

## 📂 Project Structure

```
ev-charging-app/
│
├── data/
│   └── ev_charging_data.csv
│
├── training/
│   └── train_models.py
│
├── models/
│   ├── cost_model.pkl
│   ├── time_model.pkl
│   └── distance_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

1. **Data Extraction & Exploration**

   * Loaded EV charging session data
   * Performed exploratory data analysis (EDA)

2. **Data Cleaning**

   * Handled missing values
   * Removed outliers using IQR-based methods

3. **Feature Engineering**

   * Derived features such as SOC delta, energy per %, and charging efficiency
   * Encoded categorical variables (vehicle model, charger type, user type)

4. **Model Building**

   * Trained individual regression models for:

     * Charging cost
     * Charging duration
     * Driving distance
   * Evaluated performance using appropriate metrics
   * Saved trained models as `.pkl` files

5. **Deployment**

   * Built an interactive UI using Streamlit
   * Users input EV details and receive predictions instantly

---

## 🖥 Streamlit Application

The web app allows users to:

* Select **Vehicle Model**
* Select **Charger Type**
* Select **User Type**
* Enter current **State of Charge (SOC)**
* Choose a prediction type:

  * Cost
  * Time
  * Driving Distance

Predictions are displayed dynamically based on user selection.

---

## 🎨 UI Note

> The UI is intentionally kept simple as I continue learning Streamlit.
> Future iterations will focus on improved design, interactivity, and enhanced user experience.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ev-charging-app.git
cd ev-charging-app
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train models (optional)

```bash
python training/train_models.py
```

### 4️⃣ Run Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Improve UI/UX with advanced Streamlit components
* Add model performance visualization
* Deploy application on cloud (Streamlit Cloud / AWS)
* Add real-time charging data integration

---

## 👤 Author

**Manjunath**
Aspiring Data Analyst / Data Scientist
📫 LinkedIn: www.linkedin.com/in/mohith-manjunath-684550373




