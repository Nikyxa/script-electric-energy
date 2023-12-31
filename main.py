from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector

driver = webdriver.Chrome(ChromeDriverManager().install())

db = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql123",
    database="electricity_market_data",
)
cursor = db.cursor()

url = "https://www.oree.com.ua/index.php/control/results_mo/DAM"
driver.get(url)

button = driver.find_element(By.XPATH, "//*[@id='trade_res_type']/div[3]")
button.click()

items = driver.find_elements(
    By.XPATH, "/html/body/div[4]/div[1]/div[3]/div[3]/div/div[2]/table/tbody/tr"
)

for item in items:
    item_text = item.text
    data = item_text.split(" ")
    hour = data[0]
    price = data[1]
    volume = data[2]

    date = datetime.now()
    market_close_time = datetime(date.year, date.month, date.day, 13, 0)
    tomorrow = datetime.now() + timedelta(days=1)

    if date >= market_close_time:
        date = tomorrow
        insert_query = """INSERT INTO electricity_market_data (date, hour, price, volume) VALUES (%s, %s, %s, %s)"""
        values = (date, hour, price, volume)
        try:
            cursor.execute(insert_query, values)
        except mysql.connector.Error as error:
            print("Error while inserting data:", error)

    db.commit()

driver.quit()
cursor.close()
db.close()
