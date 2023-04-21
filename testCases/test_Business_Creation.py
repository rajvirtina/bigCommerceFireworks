import pytest
from pageObjects.CreateWidgetConfigurationPage import CreateWidgetConfigurationPage
from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_Business_Creation:
    logger = LogGen.logger()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.order(3)
    @pytest.mark.regression
    def test_businessCreation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.pp = PluginCreationPage(self.driver)
        self.cpp = ImportProductsIntoStorePage(self.driver)
        self.cwcp = CreateWidgetConfigurationPage(self.driver)
        self.lp.setusername()
        self.lp.setpassword()
        self.lp.clickLogin()
        self.lp.mailLogin()
        self.lp.selectAccount()
        self.lp.selectStore()
        self.logger.info("*** Successfully lands in the Bigcommerce DashBoard ***")
        self.pp.clickOnApps("Apps")
        self.cpp.launchPlugin()
        self.cwcp.resetPlugIn("Settings")
        self.logger.info("*** Resetting the existed settings ***")
        self.pp.confirmUserDetails()
        self.pp.enteringOTP()
        self.pp.CreateNewBusinessDetails()
        self.logger.info("*** Business Created Successfully ***")
        self.driver.close()
