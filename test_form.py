from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/sit.lab1/Desktop/Hospital Patient Registration Form/index.html")
time.sleep(2)

def fill_form(name, email, phone, dob, gender_id, blood):
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(phone)
    if dob: driver.find_element(By.ID, "dob").send_keys(dob)
    if gender_id: driver.find_element(By.ID, gender_id).click()
    if blood: driver.find_element(By.ID, "bloodType").send_keys(blood)

def submit_and_alert():
    driver.find_element(By.ID, "regForm").submit()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

# Test valid registration
fill_form("John Doe", "john@example.com", "1234567890", "1990-01-01", "male", "O+")
submit_and_alert()
print("Registration test: Passed")

# Test invalid name
driver.refresh()
time.sleep(1)
fill_form("John123", "", "", "", "", "")
submit_and_alert()
print("Name validation test: Passed")

# Test invalid email
driver.refresh()
time.sleep(1)
fill_form("John Doe", "john@", "", "", "", "")
submit_and_alert()
print("Email validation test: Passed")

# Test invalid phone
driver.refresh()
time.sleep(1)
fill_form("John Doe", "john@example.com", "123", "", "", "")
submit_and_alert()
print("Phone validation test: Passed")

# Test missing gender
driver.refresh()
time.sleep(1)
fill_form("John Doe", "john@example.com", "1234567890", "1990-01-01", "", "O+")
submit_and_alert()
print("Gender validation test: Passed")

driver.quit()