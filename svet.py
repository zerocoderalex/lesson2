import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from w3lib.url import parse_data_uri

# Настройка веб-драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver

url = 'https://tomsk.hh.ru/vacancies/programmist'
driver.get(url)
# Дайте странице время загрузиться
time.sleep(3)

# Соберите данные
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
print(vacancies)

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print("Ошибка")
        continue

    parsed_data.append([title, salary, link])


        # Закройте браузер
driver.quit()

# Сохраните данные в CSV
with open('hh.csv', 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)
    writer.writerow(['Название','зарплата','ссылка'])

    writer.writerows(parsed_data)
