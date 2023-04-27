import string
import random

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Creation:
    logger = LogGen.logger()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.order(2)
    @pytest.mark.regression
    def testPlugInInstall(self, setup):
        log = self.logger
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        log.info("******************Logging to the Application****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername()
        self.lp.setpassword()
        self.lp.clickLogin()
        self.lp.mailLogin()
        self.lp.selectAccount("Virtina", "Virtina Sandbox for Multistore")
        self.logger.info("****************** Verifying Installing the Plugin ****************")
        self.cp = PluginCreationPage(self.driver)
        self.cp.clickOnApps("Apps")
        self.cp.selectApp("Firework")
        self.cp.installApp("Virtina Sandbox for Multistore")
        self.driver.save_screenshot(".\\Screenshots\\" + res + "test_installing_app.png")
        self.cp.confirmUserDetails()
        self.cp.enteringOTP()
        self.driver.save_screenshot(".\\Screenshots\\" + res + "test_businessDetails_app.png")
        self.cp.businessDetails()
        self.cp.verifyPlugInCreated("Apps")
        self.logger.info("*** Firework application is Installed successfully ***")
        self.driver.save_screenshot(".\\Screenshots\\" + res + "test_pluginInstallation_app.png")
        self.cp.logOut("My Profile")
