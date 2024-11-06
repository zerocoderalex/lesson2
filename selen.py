
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def search_wikipedia(query):
    browser.get("https://ru.wikipedia.org/wiki/Главная_страница")
    search_box = browser.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Ждем загрузки страницы

def display_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph.text}")
    print("\n")

def choose_related_page():
    links = browser.find_elements(By.XPATH, "//a[@href]")
    related_links = [link for link in links if link.get_attribute("href").startswith("https://ru.wikipedia.org/wiki/")]

    if not related_links:
        print("Нет связанных страниц.")
        return None

    print("Связанные страницы:")
    for i, link in enumerate(related_links[:5]):  # Ограничим количество показываемых ссылок
        print(f"{i + 1}: {link.text} ({link.get_attribute('href')})")

    choice = int(input("Выберите номер страницы для перехода (или 0 для возврата): ")) - 1
    if 0 <= choice < len(related_links):
        return related_links[choice].get_attribute("href")
    return None

def main():
    initial_query = input("Введите первоначальный запрос: ")
    search_wikipedia(initial_query)

    while True:
        print("\nВыберите действие:")
        print("1: Листать параграфы текущей статьи")
        print("2: Перейти на одну из связанных страниц")
        print("3: Выйти из программы")
        action = input("Введите номер действия: ")

        if action == '1':
            display_paragraphs()
        elif action == '2':
            related_page = choose_related_page()
            if related_page:
                browser.get(related_page)
                time.sleep(2)  # Ждем загрузки страницы
            else:
                print("Возврат к текущей статье.")
        elif action == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    main()
