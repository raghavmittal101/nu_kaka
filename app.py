# create virtualenv before using this program

import getpass
# program to login and apply for local gatepass on moodle
global username
global password


username = raw_input("usrename:")  ## enter moodle username
password = getpass.getpass("password:")  ## enter moodle password

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        # open URL in firefox
        self.driver = webdriver.Firefox()
        self.driver.get("https://moodle.niituniversity.in")

    def test_Login(self):
        driver = self.driver

        loginButtonXpath = "/html/body/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/a"
        loginButtonElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        loginButtonElement.click()

        usernameBoxID = "username"
        passwordBoxID = "password"
        SignInButtonID = "loginbtn"

        usernameBoxElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(usernameBoxID))
        passwordBoxElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(passwordBoxID))
        SignInButtonElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id(SignInButtonID))

        usernameBoxElement.send_keys(username)
        passwordBoxElement.send_keys(password)
        SignInButtonElement.click()

        gatePassButtonID = "yui_3_13_0_2_1465199879029_67"
        gatePassButtonXpath = "/html/body/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div[1]/div/div/div/form/div/table/tbody/tr/td[1]/label[1]/input"
        gatePassButtonElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(gatePassButtonXpath))
        gatePassButtonElement.click()

        localPassButtonXpath = "/html/body/table/tbody/tr[2]/td[1]/ul/li[2]/a"
        localPassButtonElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(localPassButtonXpath))
        localPassButtonElement.click()

        gatePassRadioButtonXpath = "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr/td/table/tbody/tr/td[1]/input"
        gatePassRadioButtonElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(gatePassRadioButtonXpath))
        gatePassRadioButtonElement.click()

        applyForPassButtonXpath = "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr/td/div[1]/p[3]/label/input"
        applyForPassButtonElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(applyForPassButtonXpath))
        applyForPassButtonElement.click()

if __name__ == "__main__":
    unittest.main()
