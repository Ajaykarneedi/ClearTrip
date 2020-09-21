from selenium import webdriver


driver= webdriver.Chrome(executable_path=r"E:\\Selenium Drivers\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)
wait(5)
driver.close()