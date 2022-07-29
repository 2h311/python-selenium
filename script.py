'''
# this script connects an existing open browser to selenium
# this script can be used to evade cloudflare protection and other anti-bot measures put in place by websites.

https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/#:~:text=You%20just%20need%20to%20modify,http%3A%2F%2F127.0.0.1%3A9222

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver_path = r"C:\Users\DELL\Desktop\TEST_GOAT\slists\driver\chromedriver.exe"
browser = webdriver.Chrome(service=Service(driver_path), options=chrome_options)