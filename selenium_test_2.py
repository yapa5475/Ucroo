import os
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("https://site-staging.ucroo.org/external/login")
time.sleep(2)

def enter_credentials():
    username = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")

    username.send_keys("admin@ucroo.com")
    password.send_keys("ucroo123")

    driver.implicitly_wait(5)

    dropdown = Select(driver.find_element_by_tag_name('select'))
    #print(dir(dropdown))
    driver.implicitly_wait(5)
    dropdown.select_by_visible_text('Ucroo University')

    #xpath: query lanaguage for selecting nodes from xml document
    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[8]/button')
    login_button.click()
    #works!


def post1():
    university_group_button = driver.find_element_by_partial_link_text('University')
    university_group_button.click()
    driver.implicitly_wait(5)
    all_students_group_button = driver.find_element_by_partial_link_text('All Students')
    all_students_group_button.click()

    driver.implicitly_wait(10)
    post_text_field = driver.find_element_by_xpath('//*[@id="txt_feed_content"]')
    post_text_field.send_keys('Selenium-generated test post 1: 12/15/17')
    driver.implicitly_wait(20)
    #post_text_field.send_keys('\n')



    #post_button = driver.find_element_by_xpath('//*[@id="write-post"]/div[3]/button')
    #post_button = driver.find_element_by_css_selector('#write-post > div.holder.mb20.loader-holder > button')
    #post_button = driver.find_element_by_class_name('btn-blue')
    #driver.implicitly_wait(10)
    #post_button.click()



enter_credentials()
driver.implicitly_wait(10)
post1()

driver.implicitly_wait(10)
#driver.close()