import os
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#works!
def send_message(user, message_text):
    print('Sending message')
    driver.implicitly_wait(20)
    messages_icon = driver.find_element_by_xpath('//*[@id="header-wrapper"]/header-directive/section/div/ul/li[2]/a')
    messages_icon.click()

    wait = WebDriverWait(driver, 10)
    new_message_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-wrapper"]/header-directive/section/div/ul/li[2]/messages-popup/div/div/div/div/div[1]/a[2]')))
    new_message_button.click()
    recipient_field = driver.find_element_by_xpath('//*[@id="form-select"]/select-user/div/div[1]/input')
    recipient_field.send_keys(user)

    recipient_field.click()
    selected_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-select"]/select-user/div/div[2]/div[2]/ul/li')))

    selected_user.click()

    message_text_area = driver.find_element_by_xpath('//*[@id="form-select"]/div[1]/div/textarea')
    message_text_area.send_keys(message_text)
    #driver.implicitly_wait(5)

    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-select"]/ul/li[2]/button')))
    send_button.click()

def logout():
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="user-area"]').click()
    driver.find_element_by_xpath('//*[@id="user-area"]/div[2]/div/div[4]/a').click()


message_sender_1 = "admin@ucroo.com"
mesage_sender_password_1 = "ucroo123"
message_recipient_1 = "Student"
message_1 = "Hey Student, how are you doing today?"

message_sender_2 = "student@ucroo.com"
message_sender_password_2 = "ucroo123"
message_recipient_2 = "Admin"
message_2 = "I am doing good, how are you admin?"

enter_credentials(message_sender_1, mesage_sender_password_1)
driver.implicitly_wait(5)
send_message(message_recipient_1, message_1)
driver.implicitly_wait(20)
logout()
driver.implicitly_wait(5)

driver.get("https://site-staging.ucroo.org/external/login")
time.sleep(2)

enter_credentials(message_sender_2, message_sender_password_2)
driver.implicitly_wait(5)
send_message(message_recipient_2, message_2)
driver.implicitly_wait(10)
logout()
