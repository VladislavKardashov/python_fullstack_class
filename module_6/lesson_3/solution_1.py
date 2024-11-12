from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие сайта
driver.get('https://shashkiplay.ru/')

time.sleep(5)

# Нажатие кнопки 'Играть'
enter_button = driver.find_element(By.CLASS_NAME, 'alone-button')
enter_button.click()

time.sleep(5)

# Прокрутка страницы вниз
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

time.sleep(5)

# Переход по ссылке 'Правила'
enter_link = driver.find_element(By.LINK_TEXT, 'Правила')
enter_link.click()

time.sleep(5)

# Закрытие браузера
driver.quit()