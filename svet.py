import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка веб-драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
driver.get('https://www.divan.ru/')

# Дайте странице время загрузиться
time.sleep(3)

# Соберите данные
products = driver.find_elements(By.CSS_SELECTOR, ' > div.lsooF > span')
data = []

for product in products:
    name = product.find_element(By.CSS_SELECTOR, 'h2.product-title').text
    price = product.find_element(By.CSS_SELECTOR, 'span.product-price').text
    data.append({'name': name, 'price': price})

# Закройте браузер
driver.quit()

# Сохраните данные в CSV
with open('divan_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in data:
        writer.writerow(entry)