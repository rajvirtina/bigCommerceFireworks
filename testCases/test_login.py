import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    emailHost = ReadConfig.getHostName()
    emailId = ReadConfig.getMailId()
    emailPassword = ReadConfig.getMailPassword()

    def test_login(self, setup):
        self.logger.info("****************** Verifying Login test ****************")
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailId,self.emailPassword)
        self.lp.selectAccount()
        self.lp.selectStore()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        self.driver.close()
