#group creation test
#Items to test:
#create group
#post in group
#create event



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

def enter_credentials():
    username = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")

    user_email = "admin@ucroo.com"
    user_password = "ucroo123"

    username.send_keys(user_email)
    password.send_keys(user_password)

    driver.implicitly_wait(5)

    #dropdown = Select(driver.find_element_by_tag_name('select'))
    #print(dir(dropdown))
    driver.implicitly_wait(5)
    #dropdown.select_by_visible_text('Ucroo University')

    #xpath: query lanaguage for selecting nodes from xml document
    #login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[8]/button')
    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[7]/button')
    login_button.click()

#works
def create_study_group(group_name, group_description):
    print('Group creation')

    university_button = driver.find_element_by_xpath('//*[@id="groups-menu-container"]/li[1]/a')
    university_button.click()
    extracirricular_button = driver.find_element_by_xpath('//*[@id="groups-menu-container"]/li[2]/a/span/span')

    extracirricular_button.click()
    create_group_button = driver.find_element_by_xpath('//*[@id="clubs"]/div[1]/span/button')
    create_group_button.click()

    study_option = driver.find_element_by_xpath('//*[@id="form-custom-group"]/div[2]/div/ui-view/select-type/fieldset/select/option[1]')
    study_option.click()

    next_button = driver.find_element_by_xpath('//*[@id="form-custom-group"]/div[2]/div/ui-view/select-type/fieldset/progress-navigation/div/div[2]/button')
    next_button.click()
    group_name_field = driver.find_element_by_xpath('//*[@id="form-custom-group"]/div[2]/div/ui-view/basic-info/fieldset/div[1]/div/div/div[3]/input')
    group_name_field.send_keys(group_name)
    group_description_field = driver.find_element_by_xpath('//*[@id="group-description"]')
    group_description_field.send_keys(group_description)
    next_button = driver.find_element_by_xpath('//*[@id="form-custom-group"]/div[2]/div/ui-view/basic-info/fieldset/progress-navigation/div/div[2]/button[2]')
    next_button.click()
    next_button2 = driver.find_element_by_xpath('//*[@id="form-custom-group"]/div[2]/div/ui-view/extra-info/fieldset/progress-navigation/div/div[2]/button[2]')
    next_button2.click()

    submit_button = driver.find_element_by_xpath('//*[@id="form-custom-group"]/div[2]/div/ui-view/user-management/fieldset/progress-navigation/div/div[2]/div/button')
    submit_button.click()

#above works to create a study group. now trying to generalize to create any type of group
def create_group(group_type):
    #create_group_button = driver.find_element_by_xpath('//*[@id="clubs"]/div[1]/span/button')
    #create_group_button = driver.find_element_by_xpath('//*[@id="clubs"]/div[1]/span/button')
    #create_group_button = driver.find_element_by_xpath('//*[@id="icon-create-group"]/path[2]')
    create_group_button = driver.find_element_by_xpath('//*[@id="lhs"]/section[2]/h6/a')
    create_group_button.click()



#works
def post_in_group():
    text_area = driver.find_element_by_xpath('//*[@id="txt_feed_content"]')
    text_area.send_keys('This post in the test group was automated through Selenium. Potatoes are the most versatile vegetable.')

    wait = WebDriverWait(driver, 5)
    #post_button = driver.find_element_by_xpath('//*[@id="write-post"]/div[3]/button')
    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="write-post"]/div[3]/button')))
    post_button.click()

def join_event(group_name, group_type, event_name):
    #university groups button = //*[@id="groups-menu-container"]/li[1]/a
    #ec groups button = //*[@id="groups-menu-container"]/li[2]/a
    #mentoring groups button = //*[@id="groups-menu-container"]/li[3]/a
    group_type_id = 0
    if group_type == "University":
        group_type_id = 1
    elif group_type == "Extracurricular":
        group_type_id = 2
    elif group_type == "Mentoring":
        group_type_id = 3
    elif group_type == "Study":
        group_type_id = 4
    elif group_type ==  "Student Services":
        group_type_id = 5
    elif group_type == "Subjects":
        group_type_id = 6

    group_type_button = "//*[@id=\"groups-menu-container\"]/li[" + str(group_type_id) + "]/a"
    group_type_button.click()

    group_type_button = driver.find_element_by_link_text(group_name)
    group_type_button.click()
    #for testing: Selenium Exam Study Group

    events_button = driver.find_element_by_xpath('//*[@id="main-content"]/div/section[3]/div/div[3]/ul/li[2]/a')
    events_button.click()
    #Get a warning



#for testing: grouptype: Extracirruicular, groupname: Commerce Society, event


enter_credentials()
driver.implicitly_wait(5)
join_event('Manual QA Exam Study Group', 'Study', 'Test Event for Selenium 1')
#create_group('Extracurricular')
#create_study_group('Test study group - 2', 'This group was created using Selenium testing')
#driver.implicitly_wait(5)
#post_in_group()

