import time
import pytest
from pageObjects.CreateWidgetConfigurationPage import CreateWidgetConfigurationPage
from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PluginCreationPage import PluginCreationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_Widget_Creation:
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

    @pytest.mark.order(5)
    @pytest.mark.regression
    def test_widgetCreation(self, setup):
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
        self.cwcp.resetPlugIn("Settings")
        self.logger.info("*** Resetting the existed settings ***")
        self.pp.confirmUserDetails(self.userName)
        self.pp.enteringOTP(self.emailHost, "PluginCreationAuth")
        self.pp.businessDetails(self.NameId, self.emailId, self.websiteId)
        self.logger.info("*** Business Details Selected Successfully ***")
        self.cwcp.addWidget("Widget Configuration")
        #WidgetName, channelName, playListName, videoName, displayPositionOfVideo, positionOfVideo, videoOpenIn
        self.cwcp.saveWidget("WidgetTesting", "Zen Channel", "play one", "V2", "Infinite", "Bottom Right", "New Tab")
        self.cwcp.VerifyWidget("WidgetTesting")
        self.logger.info("*** All Widgets Created & Verified Successfully ***")
        self.cwcp.editPlaylistWidget("Qa-Playlist-2")
        time.sleep(2)
        self.logger.info("*** All Widgets edited Playlist Successfully ***")
        self.cwcp.searchWidget("WidgetTesting")
        self.pp.logOut("My Profile")
