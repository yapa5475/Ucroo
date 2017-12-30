import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

'''
binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
'''

#binary = FirefoxBinary('/usr/bin/geckodriver.exe')
#driver = webdriver.Firefox(firefox_binary=binary)
driver = webdriver.Firefox()
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