from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime
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

def clean_text(text):
    output = text.split(": ")[1]
    return output

# Save text in new file
def save_text(text):
    time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    file = open(f"{time}.txt", "w")
    file.write(text)
    file.close()

def main():
    driver = get_driver()
    # Find username and password inputs, input username, wait 2 seconds, enter password and press enter
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    
    # After 2 seconds press "Home" link in nav
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

    # Find and clean temperature, save it in new file
    x = 0
    while x < 10:
        time.sleep(2)
        temp = (driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]"))
        temp = clean_text(temp.text)
        save_text(temp)
        x += 1
    

print(main())