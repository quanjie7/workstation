#encoding:utf-8
import time
from selenium import webdriver
count = 0
while count < 50:
    driver =  webdriver.Chrome()#executable_path="路径"
    driver.get("https://buluo.qq.com/index.html")
    time.sleep(1)
    login = driver.find_element_by_xpath('//*[@id="userInfo"]/p/a')
    login.click()
    time.sleep(1)
    driver.switch_to_frame("login_frame")
    driver.find_element_by_xpath("//a[@id='switcher_plogin']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='u']").clear()
    driver.find_element_by_xpath("//input[@id='u']").send_keys("3071388565")
    driver.find_element_by_xpath("//input[@id='p']").clear()
    driver.find_element_by_xpath("//input[@id='p']").send_keys("lcountry@7")
    driver.find_element_by_xpath("//input[@id='login_button']").click()
    driver.close()
    count = count + 1
