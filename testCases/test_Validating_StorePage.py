import pytest
from pageObjects.StoreValidationPage import StoreValidationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_009_StoreLogin:
    storeUrl = ReadConfig.getStoreURL()
    logger = LogGen.logger()

    @pytest.mark.order(9)
    @pytest.mark.regression
    def test_storeLogin_validation(self, setup):
        self.logger.info("****************** Verifying Login to the BigCommerce ****************")
        self.driver = setup  # webdriver.Chrome()
        self.sp = StoreValidationPage(self.driver)
        self.driver.get(self.storeUrl)
        self.sp.enterPreviewCode("au71a147ge")
        self.sp.validateStoreTitlePage()
        self.driver.close()
