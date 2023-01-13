import time

from selenium.webdriver.common.by import By
from pageObjects.PluginCreationPage import PluginCreationPage


class ImportProductsIntoStorePage:
    btn_myApps_Xpath = "//span[text()='My Apps']"
    btn_img_myapp_link_Xpath = "//ng-transclude/child::div/h1[text()='$Applink']//..//..//parent::article//child::figcaption//a"
    frame_store_Xpath = "app-iframes > iframe"
    btn_profile_tab_Xpath = "//button[@id='profile-tab']//child::p[text()='$profileTab']"#Business Portal & Widget Configuration
    frame_store_ID = "fw-iframe"
    btn_menu_bar_Xpath = "//span[@aria-label='menu']//parent::button"
    btn_store_Xpath = "//span[text()='Stores']//parent::button"
    btn_storeName_Xpath = "//div[contains(@class,'cy-sub-menu-list')]//a//child::span[contains(text(),'$StoreName')]"
    tabs_store_import_Xpath = "//div[@class='ant-tabs-nav-list']//child::div//div"
    tab_name_Xpath = "//div[@class='ant-tabs-nav-list']//child::div//div[text()='$tabName']"
    txt_search_box_Xpath = "//input[@id='query']"
    btn_search_Xpath = "//button[@type='submit']/span"
    btn_import_product_Xpath = "//p[text()='$product']//parent::div/..//following-sibling::div//child::div//button//span"
    txt_product_name_productTab_Xpath = "//tbody[@class='ant-table-tbody']//tr//td//span[text()='$product']"
    txt_search_box_productTab_ClassName = "ant-input"
    btn_search_productTab_ClassName = "ant-btn ant-btn-default ant-input-search-button"
    lnk_product_url_Xpath = "//span[text()='$product']//..//following-sibling::td//a"

    def __init__(self, driver):
        self.driver = driver

    def launchPlugin(self):
        self.pp = PluginCreationPage(self.driver)
        self.driver.switch_to.frame(self.pp.myapps_frame_Id)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_myApps_Xpath).click()
        time.sleep(5)
        apps = self.driver.find_elements(By.XPATH, self.pp.my_apps_link_Xpath)
        size = len(apps)
        for i in range(size):
            appText = apps[i].text
            print(appText)
            if appText == "Firework":
                print("**********Fireworks App Available under App Section********")
                element = self.driver.find_element(By.XPATH,
                                                   self.btn_img_myapp_link_Xpath.replace("$Applink", appText))
                element.click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.pp.btn_install_Xpath).click()
                time.sleep(10)
                self.driver.switch_to.default_content()
                break
            else:
                print("**********Fireworks App Not Available under App Section********")

    def verifyAndNavigateTab(self, ProfileTab, storeName, TabName):
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.frame_store_Xpath)
        self.driver.switch_to.frame(ifr)
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_profile_tab_Xpath.replace("$profileTab", ProfileTab)).click()
        time.sleep(7)
        self.driver.switch_to.frame(self.frame_store_ID)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_menu_bar_Xpath).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_store_Xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_storeName_Xpath.replace("$StoreName", storeName)).click()
        time.sleep(7)
        tabs = self.driver.find_elements(By.XPATH, self.tabs_store_import_Xpath)
        size = len(tabs)
        for i in range(size):
            tabText = tabs[i].text
            if tabText == "Products":
                print("Products Tab is available")
                tabs[i].click()
            elif tabText == "Import products":
                print("Import products Tab is available")
                tabs[i].click()
            elif tabText == "Store details":
                print("Store details Tab is available")
                tabs[i].click()
            elif tabText == "Payments":
                print("Payments is available")
                tabs[i].click()
            else:
                print("Tab are not available")
        print("**********Four Tabs are Present in the Plugin********")
        element = self.driver.find_element(By.XPATH, self.tab_name_Xpath.replace("$tabName", TabName))
        time.sleep(5)
        element.click()

    def selectProduct(self, productName):
        element = self.driver.find_element(By.XPATH, self.txt_search_box_Xpath)
        element.clear()
        element.click()
        element.send_keys(productName)
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_search_Xpath).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_import_product_Xpath.replace("$product", productName)).click()

    def verifyAddedProductInProductsTab(self, TabName, ProductName):
        self.driver.find_element(By.XPATH, self.tab_name_Xpath.replace("$tabName", TabName)).click()
        time.sleep(10)
        element = self.driver.find_element(By.XPATH,
                                           self.txt_product_name_productTab_Xpath.replace("$product", ProductName))
        #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element.is_displayed():
            print(ProductName + ": " + " is Available in the Product Tab")
        else:
            print(ProductName + ": " + " is Not Available in the Product Tab")

    def searchProductInProductTab(self, productName):
        element1 = self.driver.find_element(By.CLASS_NAME, self.txt_search_box_productTab_ClassName)
        element1.click()
        element1.send_keys(productName)
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, self.btn_search_productTab_ClassName).click()
        time.sleep(10)
        element = self.driver.find_element(By.XPATH,
                                           self.txt_product_name_productTab_Xpath.replace("$product", productName))
        #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element.is_displayed():
            print(productName + ": " + " is Available in the Product Tab")
        else:
            print(productName + ": " + " is Not Available in the Product Tab")

    def navigateToProductURL(self, menuName):
        self.cp = PluginCreationPage(self.driver)
        self.driver.find_element(By.XPATH, self.lnk_product_url_Xpath).click()
        time.sleep(10)
        self.driver.switch_to.defaultContent()
        time.sleep(5)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        getTitle = self.driver.title
        print(getTitle)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.cp.btn_back_menu_Xpath.replace('$mainMenu', menuName)).click()
