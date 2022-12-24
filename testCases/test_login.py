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
        self.logger.info("****************** Verifying Login to the BigCommerce ****************")
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailId,self.emailPassword,"BigCommerceAuth")
        self.lp.selectAccount()
        self.lp.selectStore()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")

        act_title = self.driver.title
        exp_title = "LatitudeFin BigCommerce Control Panel"

        if act_title == exp_title:
            self.logger.info("*** Succesfully lands in the Bigcommerce DashBorad ***")
        elif act_title != exp_title:
            if self.exp == 'Pass':
                self.logger.info("**** Succesfully not lands in the Bigcommerce DashBorad ****")
        self.driver.close()
        self.logger.info("******* End of Login to the BigCommerce **********")

