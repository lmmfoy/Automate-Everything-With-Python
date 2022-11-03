from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    driver.get("https://automated.pythonanywhere.com/")
    return driver

# Extract only temperature from text
def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    # Wait for 2 seconds to allow element to appear
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())