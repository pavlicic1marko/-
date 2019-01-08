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


__author__="ME"
import time
from selenium import webdriver
driver=webdriver.Chrome("D:\\chromedriver.exe") #location of the fail
driver.set_page_load_timeout(30)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation")  #q is the valu for the name atribute of the search bar
time.sleep(4)
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()



__author__="ME"
import time
import re
from selenium import webdriver
driver=webdriver.Chrome("D:\\chromedriver.exe") #location of the fail
driver.set_page_load_timeout(30)
driver.get("https://google.com")
doc=driver.page_source
print(doc)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("G:\\chromedriver_win32\\chromedriver.exe") #location of the fail
driver.set_page_load_timeout(30)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
print(elem)
elem.clear()
print(elem)
elem.send_keys("pycon")
print(elem)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print(elem[1])
driver.close()
