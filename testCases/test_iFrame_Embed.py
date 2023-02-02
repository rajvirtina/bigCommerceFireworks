import pytest
from pageObjects.CreateWidgetConfigurationPage import CreateWidgetConfigurationPage
from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_Iframe_Embed:
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

    @pytest.mark.order(4)
    @pytest.mark.regression
    def test_iframeEmbed(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.pp = PluginCreationPage(self.driver)
        self.cpp = ImportProductsIntoStorePage(self.driver)
        self.cwcp = CreateWidgetConfigurationPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailHost, self.emailId, self.emailPassword, "BigCommerceAuth", "continue")
        self.lp.selectAccount()
        self.lp.selectStore()
        self.logger.info("*** Successfully lands in the Bigcommerce DashBoard ***")
        self.pp.clickOnApps("Apps")
        self.cpp.launchPlugin()
        self.cwcp.connectPlugIn("Settings")
        self.pp.confirmUserDetails(self.userName)
        self.pp.enteringOTP(self.emailHost, "PluginCreationAuth")
        self.pp.businessDetails(self.NameId, self.emailId, self.websiteId)
        self.logger.info("*** Iframe_Embed loaded Successfully ***")
        self.cwcp.verifyProfileTabs()
        self.pp.logOut("My Profile")
