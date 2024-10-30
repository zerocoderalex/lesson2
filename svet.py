import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = 'https://www.divan.ru/kazan/category/svet"/'
driver.get(url)


time.sleep(10)


cvets = driver.find_elements(By.CLASS_NAME, "div._Ud0k")


parsed_data = []

for cvet in cvets:
    try:
        title = cvet.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = cvet.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        link = cvet.find_element(By.CSS_SELECTOR, value='a.ui-GPFV8.qUioe.ProductName').get_attribute('href')
    except:
        print("Ошибка")
        continue

    parsed_data.append([title, price, link])



driver.quit()

# Сохраните данные в CSV
with open('cvet.csv', 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)
    writer.writerow(['Название','цена','ссылка'])

    writer.writerows(parsed_data)
