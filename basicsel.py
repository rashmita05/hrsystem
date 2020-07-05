import time
from selenium import webdriver

# creating object of Chrome Class
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="..//..//resources//chromedriver83.exe")
# driver = webdriver.Firefox(executable_path="../resources/geckodriver-64bit.exe")
driver = webdriver.Chrome(executable_path="..//resources//chromedriver.exe")
driver.maximize_window()
print(type(driver)) # driver represents browser

driver.get("http://selenium-examples.nichethyself.com")

driver.find_element_by_id("loginname").send_keys("stc123")
driver.find_element_by_id("loginpassword").send_keys("12345")
#driver.find_element_by_id("loginbutton").click() # method chaining
login_button = driver.find_element_by_id("loginbutton")
print(login_button.is_displayed())
print(login_button.is_enabled())
print(login_button.text)
print(login_button.get_attribute("value"))
print(login_button.value_of_css_property("color"))

# driver.find_element_by_xpath("//input[@name= 'fuel_type'][@value='Diesel']")
#this comment is added
print("test")
print(driver.title)
driver.get("http://www.google.com")
driver.back()
driver.forward()
# driver.find_element(by=By.ID, value ="username")
driver.minimize_window()
time.sleep(2)
driver.maximize_window()
print(driver.name)
time.sleep(2) # hard wait - not to be used in real life scenario
driver.refresh()
my_page_source = driver.page_source
print(driver.current_url)
# WebElement represents one element
# friendly locators
print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())

driver.quit()