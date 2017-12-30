import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
#to ignore chrome popup

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")

def enter_credentials():
    #username = driver.find_element_by_name("email")
    #password = driver.find_element_by_name("pass")

    #username.send_keys("yash.parekh223@gmail.com")
    #password.send_keys("Winter09")

    print('Hello World')
    #trying to do dropdowns
    #select = Select(driver.find_element_by_id("month"))
    #select.select_by_visible_text("Feb")

    #login_button = driver.find_element_by_class_name("uiButtonConfirm")
    #login_button.click()


enter_credentials()
