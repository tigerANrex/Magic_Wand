# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Enter Username and Password
usr = ""
pwd = ""
URL = "https://prowand.pro-unlimited.com/login.html"

# Initialize Web Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options = options)
driver.implicitly_wait(10)
driver.get(URL)

# Login
usr_pwd_input = driver.find_elements_by_tag_name('input')
usr_pwd_input[0].send_keys(usr)
usr_pwd_input[1].send_keys(pwd)
driver.find_element_by_name("loginButton").click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "selectedBillingType")))

# Selecting the latest date range
bill_type = Select(driver.find_element_by_id("selectedBillingType"))
bill_type.select_by_value("Time")
date_range = Select(driver.find_element_by_id("dateRangeString"))
date_range.select_by_index(1)
driver.execute_script('confirmDNW();')
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "billingDetailItems1.billingTimeSpans0.startHourM")))

# Fills in Time Card
for i in range(5):
    for j in range(2):
        driver.execute_script("javascript:addNew({}, 'timeEntry');".format(i+1))

    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans0.startHourM".format(i+1))).select_by_value("8")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans0.endHourM".format(i+1))).select_by_value("12")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans0.endMeridiem".format(i+1))).select_by_value("1")

    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans1.startHourM".format(i+1))).select_by_value("12")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans1.startMeridiem".format(i+1))).select_by_value("1")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans1.endHourM".format(i+1))).select_by_value("1")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans1.endMeridiem".format(i+1))).select_by_value("1")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans1.timeEntrySpanType".format(i+1))).select_by_value("Lunch")

    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans2.startHourM".format(i+1))).select_by_value("1")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans2.startMeridiem".format(i+1))).select_by_value("1")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans2.endHourM".format(i+1))).select_by_value("5")
    Select(driver.find_element_by_id("billingDetailItems{}.billingTimeSpans2.endMeridiem".format(i+1))).select_by_value("1")

    driver.find_element_by_id("billingDetailItems{}.customFields0.regularHours".format(i+1)).clear()
    driver.find_element_by_id("billingDetailItems{}.customFields0.regularHours".format(i+1)).send_keys("8")
    Select(driver.find_element_by_id("cf_0_{}_0_0".format(i+1))).select_by_index(1)

# Submit Time Card
driver.find_element_by_name("image").click()

print("DONE!!!")
