import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def TestName(self):
        driver=webdriver.Chrome(executable_path="E:\\Selenium Drivers\\chromedriver.exe")
        driver.get("https://www.Google.com/")
        titleofWebPage=driver.title
        #assertEqual
        self.assertEqual("Google",titleofWebpage,"webpage title is not same")
        #self.assertNotEqual("Google123",titleofWebpage)

if__name__"" "_name_":
    unittest.main()