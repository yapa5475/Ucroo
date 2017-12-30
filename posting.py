import os
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://site-staging.ucroo.org/external/login")
time.sleep(2)

def enter_credentials(user_email, user_password):
    username = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")

    username.send_keys(user_email)
    password.send_keys(user_password)

    driver.implicitly_wait(5)

    #dropdown = Select(driver.find_element_by_tag_name('select'))
    #print(dir(dropdown))
    #driver.implicitly_wait(5)
    #dropdown.select_by_visible_text('Ucroo University')

    #xpath: query lanaguage for selecting nodes from xml document
    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[7]/button')
    login_button.click()

#works
def create_post(post_text):
    wait = WebDriverWait(driver, 10)
    university_group_button = driver.find_element_by_xpath('//*[@id="groups-menu-container"]/li[1]/a/span/span')
    driver.implicitly_wait(2)
    #university_group_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="groups-menu-container"]/li[1]/a/span/span'))
    university_group_button.click()
    driver.implicitly_wait(2)
    all_students_button = driver.find_element_by_xpath('//*[@id="groups-menu-container"]/li[1]/ul/li[1]/a/span/span')
    all_students_button.click()
    text_area = driver.find_element_by_xpath('//*[@id="txt_feed_content"]')
    text_area.send_keys(post_text)
    driver.implicitly_wait(2)
    #post_button = driver.find_element_by_xpath('//*[@id="write-post"]/div[3]/button')
    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="write-post"]/div[3]/button')))
    post_button.click()

#works
def create_poll(poll_question, option_1, option_2):
    university_group_button = driver.find_element_by_xpath('//*[@id="groups-menu-container"]/li[1]/a/span/span')
    university_group_button.click()
    driver.implicitly_wait(2)
    all_students_button = driver.find_element_by_xpath('//*[@id="groups-menu-container"]/li[1]/ul/li[1]/a/span/span')
    all_students_button.click()

    #poll_text_area = driver.find_element_by_xpath('//*[@id="write-post"]/div[3]/button')
    poll_text_area = driver.find_element_by_xpath('//*[@id="txt_feed_content"]')
    poll_text_area.send_keys(poll_question)

    poll_create_button = driver.find_element_by_xpath('//*[@id="write-post"]/div[1]/ul/li[1]/a')
    poll_create_button.click()

    poll_option_1 = driver.find_element_by_xpath('//*[@id="write-post"]/poll-options/div/ul/li[1]/ng-form/div/textarea')
    poll_option_1.send_keys(option_1)
    poll_option_2 = driver.find_element_by_xpath('//*[@id="write-post"]/poll-options/div/ul/li[2]/ng-form/div/textarea')
    poll_option_2.send_keys(option_2)

    wait = WebDriverWait(driver, 10)

    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="write-post"]/div[3]/button')))
    post_button.click()



#def deleting_post():
    #post_to_delete = driver.find_element_by_


#def report_post():


def main():
    user = 'admin@ucroo.com'
    password = 'ucroo123'

    enter_credentials(user, password)
    driver.implicitly_wait(5)
    post_text = 'This post in the test group was automated through Selenium. Potatoes are the most versatile vegetable.'

    create_post(post_text)
    #create post works

    #driver.implicitly_wait(10)
    poll1_text = 'What is your favorite fruit?'
    poll1_option1 = 'Apples'
    poll1_option2 = 'Bananas'
    create_poll(poll1_text, poll1_option1, poll1_option2)
    #create poll works

main()