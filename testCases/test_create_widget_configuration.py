import pytest

from pageObjects.CreateWidgetConfigurationPage import CreateWidgetConfigurationPage
from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_Widget_Creation:
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
    def test_widgetCreation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailHost, self.emailId, self.emailPassword, "BigCommerceAuth", "continue")
        self.lp.selectAccount()
        self.lp.selectStore()
        self.pp = PluginCreationPage(self.driver)
        self.pp.clickOnApps("Apps")
        self.pp.selectApp("Firework")
        self.pp.installApp(self.redirectedUrl)
        self.pp.confirmUserDetails(self.userName)
        self.pp.enteringOTP(self.emailHost, "PluginCreationAuth")
        self.pp.businessDetails(self.NameId, self.emailId, self.websiteId)
        self.pp.verifyPlugInCreated("Apps")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_PlugInCreated.png")
        self.cpp = ImportProductsIntoStorePage(self.driver)
        self.cpp.launchPlugin()
        self.cwcp = CreateWidgetConfigurationPage(self.driver)
        self.cwcp.addWidget("Widget Configuration", "Story Block")
        self.cwcp.saveWidget("Testing", "CrossFit", "Bottom Right")
        self.cwcp.VerifyWidget("Testing")
