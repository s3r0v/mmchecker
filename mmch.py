from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
import sys, os

file = input("Введите путь к файлу с сидами: ")

def check_settings():
    try:
        with open('settings.txt', 'r') as f:
            settings = f.readline()
            return settings
    except:
        with open('settings.txt', 'w') as f:
            f.write(input("Введите ссылку на расширение (это одноразовая настройка): "))

def file_to_array(file):
    arr = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            arr.append(line.strip())
    return arr

def check(link, seeds):
    result = []
    main_directory = os.path.join(sys.path[0])
    profile = webdriver.FirefoxProfile(main_directory+'/firefox_profile')
    driver = webdriver.Firefox(profile)

    for seed in seeds:
        driver.get(link+"/home.html#restore-vault")

        seed_fields = driver.find_element_by_xpath("//input[@class='MuiInputBase-input MuiInput-input']")
        new_pass = driver.find_element_by_id("password")
        confirm_pass = driver.find_element_by_id("confirm-password")
        confirm_button = driver.find_element_by_xpath("//button[@class='button btn--rounded btn-primary first-time-flow__button']")

        seed_fields.send_keys(seed)
        new_pass.send_keys("oooooooo")
        confirm_pass.send_keys("oooooooo")
        confirm_button.click()

if __name__ == "__main__":
    check("moz-extension://9596f96a-5eea-994c-92b1-1c6351b28c78", check_settings())