# Guideline how to run scripts for getting price and volume during a day
This repository contains two scripts: one for data extraction from a website using Selenium and another for a Flask API endpoint to retrieve data from a MySQL table.

## 1. Data Extraction Script
This script utilizes Selenium to extract data from the website https://www.oree.com.ua/index.php/control/results_mo/DAM and stores the data in a MySQL database.

### Installing usig GitHub:
Install MySQL and create db using creds in MySQL connector or use your creds:

```
db = mysql.connector.connect(
    host="localhost",
    user=<your_username>,
    password=<your_password>,
    database="electricity_market_data",
)
```

After that in order to get and script you need to run this commands in your terminal:

```
git clone https://github.com/Nikyxa/script-electric-energy.git
```
```
python -m venv venv 
source venv/bin/activate (for Mac OS)
venv\Scripts\activate (for Windows)
```
```
pip install —r requirements.txt
```
```
python main.py
```
So, you will see the result in MySQL electricity_market_data database.

## 2. Flask API Script
After actions you have done later, you can get necessary data in json format using Flask.
You need to run such command:

```
python app.py
```
The Flask server will be started and will be available at http://localhost:5000.
To retrieve data from the MySQL table through the Flask API, open your browser or use tools to make a GET request to the following URL:

```
http://127.0.0.1:5000/data?date=2023-06-14
```