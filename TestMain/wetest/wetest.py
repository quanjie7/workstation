#encoding:utf8
import sys

import time
from selenium import webdriver

driver =  webdriver.Chrome()#executable_path="路径"
driver.get("http://wetest.qq.com/auth/login/?next=/")
time.sleep(3)
driver.switch_to_frame("qq_frame")
driver.find_element_by_xpath("//a[@id='switcher_plogin']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='u']").clear()
driver.find_element_by_xpath("//input[@id='u']").send_keys("3071388565")
driver.find_element_by_xpath("//input[@id='p']").clear()
driver.find_element_by_xpath("//input[@id='p']").send_keys("lcountry@7")
driver.find_element_by_xpath("//input[@id='login_button']").click()
time.sleep(7)
print(driver.get_cookies())
driver.get("http://fsight.qq.com/")
print(driver.get_cookies())
time.sleep(7)
driver.close()