import pytest
from pageObjects.StoreValidationPage import StoreValidationPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_010_AddProduct:
    storeUrl = ReadConfig.getStoreURL()
    logger = LogGen.logger()

    @pytest.mark.order(10)
    @pytest.mark.regression
    def test_addProduct(self, setup):
        self.logger.info("****************** Verifying Login to the BigCommerce ****************")
        self.driver = setup  # webdriver.Chrome()
        self.sp = StoreValidationPage(self.driver)
        self.driver.get(self.storeUrl)
        self.sp.enterPreviewCode("au71a147ge")
        self.sp.validateStoreTitlePage()
        self.logger.info("*** Successfully lands in the DashBoard ***")
        self.sp.nextProductNavigate()
        self.sp.addSingleProduct()
        self.logger.info("*** Added Product to the Cart ***")
        self.sp.checkOutValidation()
        self.sp.productManageInCheckoutPage()
        self.driver.save_screenshot(".\\Screenshots\\" + "ProductDetailsBasketPage.png")
        self.sp.cartValidations()
        self.logger.info("*** Updated the Product count lands in checkout page ***")
        self.driver.save_screenshot(".\\Screenshots\\" + "CartPage.png")
        self.sp.cartEmpty()
        self.driver.close()


