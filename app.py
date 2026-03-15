from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import sqlite3

# Database setup function
def init_db():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  location TEXT, area REAL, price REAL)''')
    conn.commit()
    conn.close()

init_db() # create table as the app starts 
app = Flask(__name__)

# 1. Data aur Model Loading
df = pd.read_csv('final_cleaned.csv') 

with open('RandomForestModel2.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    #  FOR Dropdowns sorted unique values
    locations = sorted(df['location_final'].unique())
    bedrooms = sorted(df['bedrooms'].unique())
    bathrooms = sorted(df['bathrooms'].unique())
    
    return render_template('index.html', 
                           locations=locations, 
                           bedrooms=bedrooms, 
                           bathrooms=bathrooms)

@app.route('/predict', methods=['POST'])
def predict():
             
    # data recieving from  teh form
    location = request.form.get('location')
    bedrooms = int(request.form.get('bedrooms'))
    bathrooms = int(request.form.get('bathrooms'))
    area = float(request.form.get('area_sqft'))

    # DataFrame creation for prediction in same order as model training
    input_df = pd.DataFrame([[area, bedrooms, bathrooms, location]], 
                            columns=['area_sqft', 'bedrooms', 'bathrooms', 'location_final'])

    # Prediction 
    prediction = model.predict(input_df)[0]
    
    # Negative value handling (jsut in case)
    result = max(0, prediction)
    # Price format then return (e.g., 15,000,000)

    try:
         # save data after prediction in database
        conn = sqlite3.connect('predictions.db')
        c = conn.cursor()
        c.execute("INSERT INTO history (location, area, price) VALUES (?, ?, ?)", 
                (location, area, int(result)))
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Database error: {e}")
    return f"{int(result):,}"

if __name__ == "__main__":
    app.run(debug=True)