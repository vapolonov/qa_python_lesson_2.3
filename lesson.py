"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html.
Нажать на кнопку.
Принять confirm.
На новой странице решить капчу для роботов, чтобы получить число с ответом
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(f"{y}")
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()
