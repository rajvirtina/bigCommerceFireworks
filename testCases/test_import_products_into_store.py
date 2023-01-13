import pytest

from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_Importing:
    redirectedUrl = ReadConfig.getRedirectedURL()
    userName = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()
    emailHost = ReadConfig.getHostName()
    emailId = ReadConfig.getMailId()
    emailPassword = ReadConfig.getMailPassword()
    NameId = ReadConfig.getnameID()
    websiteId = ReadConfig.getWebsite()
    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.order3
    @pytest.mark.regression
    def test_importProducts(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailHost, self.emailId, self.emailPassword, "BigCommerceAuth", "continue")
        self.lp.selectAccount()
        self.lp.selectStore()
        self.cp = PluginCreationPage(self.driver)
        self.cp.clickOnApps("Apps")
        self.cp.selectApp("Firework")
        self.cp.installApp(self.redirectedUrl)
        self.cp.confirmUserDetails(self.userName)
        self.cp.enteringOTP(self.emailHost, "PluginCreationAuth")
        self.cp.businessDetails(self.NameId, self.emailId, self.websiteId)
        self.cp.verifyPlugInCreated("Apps")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_PlugInCreated.png")
        self.cpp = ImportProductsIntoStorePage(self.driver)
        self.cpp.launchPlugin()
        self.cpp.verifyAndNavigateTab("Business Portal", "Clothing Store", "Import products")
        self.cpp.selectProduct("[Sample] Fog Linen Chambray Towel - Beige Stripe")
        self.cpp.verifyAddedProductInProductsTab("Products", "[Sample] Fog Linen Chambray Towel - Beige Stripe")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_ProductAvailable_ProductTab.png")
        self.cpp.searchProductInProductTab("[Sample] Fog Linen Chambray Towel - Beige Stripe")
        self.cpp.navigateToProductURL("Apps")
        self.cp.logOut("My Profile")
