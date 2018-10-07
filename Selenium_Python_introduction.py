__author__="ME"
import time
from selenium import webdriver
driver=webdriver.Chrome("G:\\chromedriver_win32\\chromedriver.exe") #location of the fail
driver.set_page_load_timeout(30)
driver.get("https://www.youtestme.com/")
driver.implicitly_wait(20)
time.sleep(3)
driver.get_screenshot_as_file("youtestme.png")
time.sleep(3)
driver.quit()
