import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config import LOGIN_DATA

def authorization(user_type):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get('https://hh.ru/')
    time.sleep(2)

    btn_entry = driver.find_element('xpath', '//*[@id="HH-React-Root"]/div/div[3]/div/div/div/div/div[5]/a')
    btn_entry.click()
    time.sleep(2)
    
    btn_password = driver.find_element('xpath', '//*[@id="HH-React-Root"]/div/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[2]/form/div[4]/button[2]')
    btn_password.click()
    time.sleep(2)

    # Получаем данные пользователя из config.py
    user_data = LOGIN_DATA.get(user_type, {})
    login = driver.find_element('xpath', '//*[@id="HH-React-Root"]/div/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/form/div[1]/fieldset/input')
    login.send_keys(user_data.get('login', ''))
    
    password = driver.find_element("xpath", '//*[@id="HH-React-Root"]/div/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/form/div[2]/fieldset/input')
    password.send_keys(user_data.get('password', ''))

    btn_entry_all = driver.find_element('xpath', '//*[@id="HH-React-Root"]/div/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/form/div[6]/button[1]')
    btn_entry_all.click()
    time.sleep(10)

