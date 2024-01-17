from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the driver 
s = Service(r'chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service = s)

# SimplyHired
driver.get("https://www.simplyhired.com/search?q=entry+level+software+engineer&s=d")


driver.close()