import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()
    emailHost = ReadConfig.getHostName()
    emailId = ReadConfig.getMailId()
    emailPassword = ReadConfig.getMailPassword()

    @pytest.mark.order(1)
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************** Verifying Login to the BigCommerce ****************")
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.lp.mailLogIn(self.emailHost, self.emailId, self.emailPassword, "BigCommerceAuth", "continue")
        self.lp.selectAccount()
        self.lp.selectStore()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")

        act_title = self.driver.title
        exp_title = "LatitudeFin BigCommerce Control Panel"

        if act_title == exp_title:
            self.logger.info("*** Successfully lands in the Bigcommerce DashBoard ***")
        elif act_title != exp_title:
            self.logger.info("**** Successfully not lands in the Bigcommerce DashBoard ****")
        self.driver.close()
        self.logger.info("******* End of Login to the BigCommerce **********")
