from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
driver.get("https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin")
driver.find_element_by_id("username").send_keys("SAxxxxxxxx")
time.sleep(2)
driver.find_element_by_id("password").send_keys("xxxxxxxxx")
time.sleep(2)
driver.find_element_by_id("login").click()
time.sleep(2)
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(2)
driver.find_element_by_id("report-submit-btn").click()
time.sleep(2)
driver.quit()



