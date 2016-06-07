# progrm to login to GMail
global password
global username

password = " " #put password
username = " " #insert username

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://accounts.google.com")

    def test_Login(self):
        driver = self.driver
        EmailBoxXpath="/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div/input[1]"
        NextButtonXpath="/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/input"
        PasswordBoxXpath = "/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div/input[2]"
        SignInButtonXpath = "/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/input[1]"

        EmailElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(EmailBoxXpath))
        NextButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(NextButtonXpath))

        EmailElement.clear()
        EmailElement.send_keys(username)
        NextButtonElement.click()

        PasswordBoxElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PasswordBoxXpath))
        SignInButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(SignInButtonXpath))

        PasswordBoxElement.clear()
        PasswordBoxElement.send_keys(password)
        SignInButtonElement.click()



if __name__ == '__main__':
    unittest.main()
