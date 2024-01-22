from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

# Set up the driver 
s = Service(r'chromedriver-win6\chromedriver.exe')
driver = webdriver.Chrome(service = s)

# SimplyHired
driver.get('https://www.simplyhired.com/search?q=entry+level+software+engineer&s=d&t=1')

job_container = []
url = []

jobs_list = driver.find_element(By.ID, 'job-list')
job_posting_elements = jobs_list.find_elements(By.TAG_NAME, 'li')

for job_elem in job_posting_elements:
    link_elem = job_elem.find_element(By.CSS_SELECTOR, 'a.css-1djbb1k')
    url.append(link_elem.get_attribute('href'))

for entry in url:
    
    driver.get(entry)
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.css-yvgnf2')))
    except:
        continue

    title = driver.find_element(By.CSS_SELECTOR, 'h1.css-yvgnf2').text
    location = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="viewJobCompanyLocation"]').text
    company = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="viewJobCompanyName"]').text
    description = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="viewJobBodyJobFullDescriptionContent"]').text
    
    try:
        salary = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="viewJobBodyJobCompensation"]').text
    except:
        salary = 'Unknown'

    try:
        link = driver.find_element(By.CSS_SELECTOR, 'a.css-24yw96').get_attribute('href')
    except:
        link = driver.find_element(By.CSS_SELECTOR, 'a.css-1wzc2gy').get_attribute('href')


    job_container.append ({
        'title' : title,
        'company' : company,
        'location' : location,
        'link': link,
        'Estimated Salary': salary,
        'description': description
    })

driver.close()

#json encoder
with open('simplyhired_json/simplyhired.json', 'w', encoding='utf-8') as f:
    json.dump(job_container, f, ensure_ascii=False, indent=4)