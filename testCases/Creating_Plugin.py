from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.CreatePluginPage import CreatePluginPage


class Test_001_Creation_Plugin:
    userName = ReadConfig.getUseremail()
    logger = LogGen.loggen()
    emailHost = ReadConfig.getHostName()
    emailId = ReadConfig.getMailId()
    emailPassword = ReadConfig.getMailPassword()
    NameId = ReadConfig.getnameID()
    websiteId = ReadConfig.getwebsite()
    baseURL = ReadConfig.getApplicationURL()

    def Navigate_To_Plugin(self, setup):
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.logger.info("****************** Verifying Navigating to the Plugin Side ****************")
        self.cp = CreatePluginPage(self.driver)
        self.cp.clickOnApps("Apps")
        self.cp.selectApp()
        self.cp.installApp()
        self.cp.confirmUserDetails(self.userName)
        self.cp.enteringOTP(self.emailHost, self.emailId, self.emailPassword, "PluginCreationAuth")
        self.cp.businessDetails(self.NameId, self.emailId, self.websiteId)
        self.cp.verifyPlugInCreated()
        self.cp.myApps()
        self.cp.uninstallPlugin()
        self.cp.logOut("My Profile")
