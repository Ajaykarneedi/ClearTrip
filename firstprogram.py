from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"E:\\Selenium Drivers\\chromedriver.exe")

#driver = webdriver.Chrome(executable_path="E:\\Selenium Drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cleartrip.com/")
print("Opening Page : "+driver.title)
#driver.find_element_by_id("OneWay").click()
driver.find_element_by_id("RoundTrip").click()


driver.find_element_by_id("DepartDate").clear()
driver.find_element_by_id("FromTag").send_keys("LHR")
driver.find_element_by_id("ToTag").send_keys("CDG")

# Entering input data ( in text field)
driver.find_element_by_id("DepartDate").clear()
driver.find_element_by_id("DepartDate").send_keys("28-08-2020")

driver.find_element_by_id("ReturnDate").clear()
driver.find_element_by_id("ReturnDate").send_keys("30-08-2020")





# dropdown
No_of_Adults=Select(driver.find_element_by_id("Adults"))
No_of_Adults.select_by_visible_text("2")

#Button click()
driver.find_element_by_id("SearchBtn").click()

time.sleep(30)
print("After Search: " + driver.title)

driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[7]/div[1]/div[1]/div[2]/div[4]/button').click()
                              #//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[7]/div[1]/div[1]/div[2]/div[4]/button
time.sleep(30)
New_tab = driver.window_handles[1]
driver.switch_to_window(New_tab)
print("After Book button: "+ driver.title)

driver.find_element_by_id("itineraryBtn").click()

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("test@example.com")
driver.find_element_by_id("LoginContinueBtn_1").click()
time.sleep(10)

No_of_Adults=Select(driver.find_element_by_id("AdultTitle1"))
No_of_Adults.select_by_visible_text("Mr")

driver.find_element_by_id("AdultFname1").clear()
driver.find_element_by_id("AdultFname1").send_keys("Ajay")
driver.find_element_by_id("AdultLname1").clear()
driver.find_element_by_id("AdultLname1").send_keys("kiran")

No_of_Adults=Select(driver.find_element_by_id("AdultDobDay1"))
No_of_Adults.select_by_visible_text("1")
No_of_Adults=Select(driver.find_element_by_id("AdultDobMonth1"))
No_of_Adults.select_by_visible_text("Jan")
No_of_Adults=Select(driver.find_element_by_id("AdultDobYear1"))
No_of_Adults.select_by_visible_text("1985")


No_of_Adults=Select(driver.find_element_by_id("AdultTitle2"))
No_of_Adults.select_by_visible_text("Mr")

driver.find_element_by_id("AdultFname2").clear()
driver.find_element_by_id("AdultFname2").send_keys("jay")
driver.find_element_by_id("AdultLname2").clear()
driver.find_element_by_id("AdultLname2").send_keys("iran")

No_of_Adults=Select(driver.find_element_by_id("AdultDobDay2"))
No_of_Adults.select_by_visible_text("1")
No_of_Adults=Select(driver.find_element_by_id("AdultDobMonth2"))
No_of_Adults.select_by_visible_text("Feb")
No_of_Adults=Select(driver.find_element_by_id("AdultDobYear2"))
No_of_Adults.select_by_visible_text("1983")

driver.find_element_by_id("mobileNumber").send_keys("9848539393")




time.sleep(15)
#driver.quit()