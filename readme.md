# 🏠 Karachi House Price Predictor

A professional web application that predicts house prices in Karachi using Machine Learning. This project uses a **Random Forest Regressor** model trained on olx scrapped data to provide accurate price estimates based on area, location, and room counts.

# simplified explaination of project
data scraping from olx -> data cleaning  -> model training -> flask app html,(AJAX) javascript and sqlite 3 integration 

## ⚙️ Installation & Setup
1. Clone the repo: `git clone https://github.com/Abdullahalam379/karachi-house-price.git`
2. Create venv: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`

## 🚀 Features
* **Interactive UI:** Modern Glassmorphism design with a clean user experience.
* **Dynamic Dropdowns:** Locations and room details are fetched directly from the dataset.
* **Real-time Prediction:** Uses AJAX (JavaScript) to show results without refreshing the page.
* **Virtual Environment:** Fully isolated setup for easy deployment.

## 🛠️ Tech Stack
* **webscrapping:** webdriver , stealth , beautiful soup
* **Backend:** Flask (Python)
* **Frontend:** HTML, JavaScript (AJAX)
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Category Encoders
* **Model:** Random Forest (Saved via Pickle)
* **sql integration:** sqlite3