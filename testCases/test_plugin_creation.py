import string
import random

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Creation:
    userName = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()
    emailHost = ReadConfig.getHostName()
    emailId = ReadConfig.getMailId()
    emailPassword = ReadConfig.getMailPassword()
    NameId = ReadConfig.getnameID()
    websiteId = ReadConfig.getWebsite()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.order1
    @pytest.mark.regression
    def testlogin(self, setup):
        log = self.logger
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        log.info("******************Logging to the Application****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailHost, self.emailId, self.emailPassword, "BigCommerceAuth")
        self.lp.selectAccount()
        self.lp.selectStore()
        self.driver.save_screenshot(".\\Screenshots\\" + res + "test_login.png")
        self.logger.info("****************** Verifying Navigating to the Plugin Side ****************")
        self.cp = PluginCreationPage(self.driver)
        self.cp.clickOnApps("Apps")
        self.cp.selectApp("Fireworks")
        self.driver.save_screenshot(".\\Screenshots\\" + res + "test_navigate_app.png")
        self.cp.installApp()
        self.driver.save_screenshot(".\\Screenshots\\" + res + "test_installing_app.png")
        self.cp.confirmUserDetails(self.userName)
        self.cp.enteringOTP(self.emailHost, self.emailId, self.emailPassword, "PluginCreationAuth")
        self.cp.businessDetails(self.NameId, self.emailId, self.websiteId)
        self.cp.verifyPlugInCreated()
        self.cp.myApps()
        self.cp.uninstallPlugin()
        self.cp.logOut("My Profile")
