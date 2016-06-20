from Tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import conf

# class for login using selenium webdrivers
class Login:

    def __init__(self):
        """
        #location of chromedriver needed for running selenium on chrome browser. SPECIFY IT IN CONF FILE
        driver = webdriver.Chrome(conf.CHROME_DRIVER_PATH) #FOR CHROME

        driver = webdriver.Firefox() #FOR FIREFOX
        """
        driver = webdriver.Firefox() #working with firefox. see above comment and edit it to change the browser

        self.driver.get("https://moodle.niituniversity.in")
        self.tLogin()

    def tLogin(self):
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

class gui:
    def fetch(self):
        global username
        global password
        username =  str(self.usernameIn.get())
        password =  str(self.passwordIn.get())
        if len(username) & len(password):
                root.quit()
                l = Login()
        else:
            print 'both fields required'

    def __init__(self, master):
        frame1 = Frame(master)
        frame1.grid(row=1)

        frame2 = Frame(master)
        frame2.grid(row=2)

        frame1_1 = Frame(master)
        frame1_1.grid(row=1, column=1)

        frame1_2 = Frame(master)
        frame1_2.grid(row=1, column=2)

        frame2_1 = Frame(master)
        frame2_1.grid(row=2, column=1)

        frame2_2 = Frame(master)
        frame2_2.grid(row=2, column=2)

        frame3 = Frame(master)
        frame3.grid(row=3)

        self.usernameL = Label(frame1_1, text="Username")
        self.passwordL = Label(frame2_1, text="Password")
        self.usernameIn = Entry(frame1_2)
        self.passwordIn = Entry(frame2_2, show='*')

        self.loginbutton = Button(frame3, text="apply", command=self.fetch)
        self.usernameL.pack()
        self.passwordL.pack()
        self.usernameIn.pack()
        self.passwordIn.pack()
        self.loginbutton.pack(side=RIGHT)

root = Tk()
obj = gui(root)
root.mainloop()

