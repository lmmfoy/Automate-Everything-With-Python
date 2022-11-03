from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"C:\Users\leafo\Desktop\this&that\setup files\chromedriver.exe")

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    # Disable infobars so that they don't interfere with script 
    options.add_argument("disable-infobars")
    # Start browser as maximized 
    options.add_argument("start-maximized")
    # To avoid issues with browser on Linux
    options.add_argument("disable-dev-shm-usage")
    # In order to give script greater privileges, disable sandbox
    options.add_argument("no-sandbox")
    # Help Selenium to avoid detection from browsers
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()
    # Find username and password inputs, input username, wait 2 seconds, enter password and press enter
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    
    # After 2 seconds press "Home" link in nav
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

    # Checking url
    print(driver.current_url)

print(main())