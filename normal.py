from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.serviceimport Service

s = Service("C:\Program Files\msedgedriver.exe")
browser = webdriver.Edge(service=s)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSezs9vfDnGxHrXsF52bxKXdrmlQHbHI0HsxrO6A9PGbC3K0Xw/viewform?usp=sf_link")

time.sleep(2)

Name = "Prabhu Deva"
n = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
n.send_keys(Name)

age = "25"
n = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
n.send_keys(age)

email = "prabhudeva76@gmail.com"
n = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
n.send_keys(email)

email = "India"
n = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
n.send_keys(email)

email = "Chennai"
n = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
n.send_keys(email)

email = "Teynampet"
n = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
n.send_keys(email)

submit = driver.find_element(by=By.XPATH,

value'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
submit.click()