import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
parsed_data = []
url = 'https://www.divan.ru/kazan/category/svet"/'
driver.get(url)

def append_parsed_data(url):
    print("Start parsing")
    driver.get(url)

time.sleep(30)


cvets = driver.find_elements(By.CLASS_NAME, "div._Ud0k")
print(cvets)



for cvet in cvets:
    try:
        title = cvet.find_element(By.CSS_SELECTOR, "div.lsooF").find_element(By.TAG_NAME, 'span').text
        price =cvet.find_element(By.CSS_SELECTOR, "div.q5Uds").find_element(By.TAG_NAME, "span").text
        link = cvet.find_element(By.TAG_NAME, 'a').get_attribute("href")
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
