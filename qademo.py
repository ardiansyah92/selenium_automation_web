from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
# Open the Python website
driver.get("https://demoqa.com/elements")
driver.maximize_window()

# Get page title
# title = driver.title
sleep(3)
textbox = driver.find_element(By.ID, "item-0")
textbox.click()
sleep(5)

username = driver.find_element(By.ID, "userName")
username.send_keys("Software Quality Assurance")

useremail = driver.find_element(By.ID, "userEmail")
useremail.send_keys("Softwarequalityassurance@yopmail.com")

address = driver.find_element(By.ID , "currentAddress")
address.send_keys("Indigo Hub Bandung")

addreselse = driver.find_element(By.ID, "permanentAddress")
addreselse.send_keys("Sukarasa Indigo Hub Bandung Gerlong")

submit = driver.find_element(By.ID, "submit")
submit.click()
sleep(3)

checkbox = driver.find_element(By.ID, "item-1")
checkbox.click()

sleep(3)
plus = driver.find_element(By.CSS_SELECTOR, "button.rct-option:nth-child(1)")
plus.click()

sleep(3)
allhome = driver.find_element(By.CSS_SELECTOR, "#tree-node > ol:nth-child(2) > li:nth-child(1) > span:nth-child(1) > label:nth-child(2) > span:nth-child(2)")
allhome.click()

sleep(3)
minus = driver.find_element(By.CSS_SELECTOR, "button.rct-option:nth-child(2)")
minus.click()

sleep(3)