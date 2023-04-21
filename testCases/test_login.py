import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logger()

    @pytest.mark.order(1)
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****************** Verifying Login to the BigCommerce ****************")
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername()
        self.lp.setpassword()
        self.lp.clickLogin()
        self.lp.mailLogin()
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
