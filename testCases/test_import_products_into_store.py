import pytest

from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_007_Importing:
    logger = LogGen.logger()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.order(7)
    @pytest.mark.regression
    def test_importProducts(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername()
        self.lp.setpassword()
        self.lp.clickLogin()
        self.lp.mailLogin()
        self.lp.selectAccount("Virtina", "Virtina Sandbox for Multistore")
        self.logger.info("*** Successfully lands in the Bigcommerce DashBoard ***")
        self.cp = PluginCreationPage(self.driver)
        self.cp.clickOnApps("Apps")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_PlugInCreated.png")
        self.cpp = ImportProductsIntoStorePage(self.driver)
        self.cpp.launchPlugin()
        self.cp.selectStore("Virtina Sandbox for Multistore")
        self.cpp.verifyAndNavigateTab("Virtina Sandbox", "Import products")
        self.cpp.selectProduct("[Sample] Orbit Terrarium - Small")
        self.logger.info("*** Product selected from the Import Tab ***")
        self.cpp.verifyAddedProductInProductsTab("Products", "[Sample] Orbit Terrarium - Small")
        self.logger.info("*** Product available in the Product Tab ***")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_ProductAvailable_ProductTab.png")
        self.cpp.searchProductInProductTab("[Sample] Orbit Terrarium - Small")
        self.logger.info("*** Product available via searching Product Tab ***")
        self.driver.save_screenshot(".\\Screenshots\\" + "ProductPageDisplay.png")
        self.cp.logOut("My Profile")
