import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="../resources/chromedriver.exe")
# driver = webdriver.Firefox(executable_path="../resources/geckodriver-64bit.exe")

print(type(driver)) # driver represents browser
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(3)
driver.find_element_by_css_selector("img[src='/webres_5e7b15c4882d04.47780062/orangehrmLeavePlugin/images/MyLeave.png']").click()
time.sleep(3)
approval= driver.find_element_by_id("leaveList_chkSearchFilter_1")
if approval.is_selected():
    approval.click()
time.sleep(3)

schedule= driver.find_element_by_id("leaveList_chkSearchFilter_2")

if not schedule.is_selected():
    schedule.click()
time.sleep(3)
taken= driver.find_element_by_id("leaveList_chkSearchFilter_3")

if not taken.is_selected():
    taken.click()
time.sleep(3)

Sub_Unit = driver.find_element_by_id("leaveList_cmbSubunit")

Sub_select = Select(Sub_Unit)
Sub_select.select_by_visible_text("Sales")
time.sleep(3)
Sub_select.select_by_value("5")
time.sleep(3)
Sub_select.select_by_index(4)


expected_options = ["All", "Sales", "Administration","IT", "Finance"]
actual_options = []

for one_option in Sub_select.options:
    actual_options.append(one_option.text)

current_selection = Sub_select.first_selected_option  # which option is current selected
print(current_selection.text)
print(actual_options)

assertListEqual(actual_options, expected_options)
driver.quit()


