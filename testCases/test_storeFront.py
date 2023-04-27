import pytest
from pageObjects.CreateWidgetConfigurationPage import CreateWidgetConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_006_StoreFront:
    logger = LogGen.logger()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.order(6)
    @pytest.mark.regression
    def test_storeFront(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.cwcp = CreateWidgetConfigurationPage(self.driver)
        self.lp.setusername()
        self.lp.setpassword()
        self.lp.clickLogin()
        self.lp.mailLogin()
        self.lp.selectAccount("Virtina", "Virtina Sandbox for Multistore")
        self.logger.info("*** Successfully lands in the Bigcommerce DashBoard ***")
        self.cwcp.dragAndDrpWidgetToPageBuilder("WidgetTesting")
        self.logger.info("*** Successfully published widgets in store ***")
        self.driver.close()
