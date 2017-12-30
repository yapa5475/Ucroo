import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import logging

# create new Chrome session

driver = webdriver.Chrome()

# navigate to application homepage
driver.get("https://www.google.com")


# driver.get("https://site-staging.ucroo.org/external/login")
# driver.get("https://site-dev.ucroo.org/external/login")

# login_button = driver.find_element_by_link_text('Login')
# login_button.click()


def enter_credentials():
    # works - need to do dropdown
    username = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")

    username.send_keys("admin@ucroo.com")
    password.send_keys("ucroo123")

    dropdown = Select(driver.find_element_by_tag_name('select'))
    print(dir(dropdown))
    #print(dropdown.options)
    #print(dropdown.first_selected_option)
    dropdown.select_by_index(0)
    # dropdown.select_by_visible_text("Ucroo University")


# select_dropdown_option()
enter_credentials()
