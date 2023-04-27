import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.PluginCreationPage import PluginCreationPage
from selenium.webdriver.support import expected_conditions as EC


class ImportProductsIntoStorePage:
    btn_myApps_Xpath = "//span[text()='My Apps']"
    btn_img_myapp_link_Xpath = "//ng-transclude/child::div/h1[text()='$Applink']//..//..//parent::article//child::figcaption//a"
    frame_store_Xpath = "app-iframes > iframe"
    btn_profile_tab_Xpath = "//button[@id='profile-tab']//child::p[text()='$profileTab']"  # Business Portal & Widget Configuration
    frame_store_CSS = "div > iframe#fw-iframe"
    btn_menu_bar_Xpath = "//span[@aria-label='menu']//parent::button"
    btn_store_Xpath = "//span[text()='Stores']//parent::button"
    btn_channel_Xpath = "//span[text()='Channels']//parent::button"
    btn_storeName_Xpath = "//div[contains(@class,'cy-sub-menu-list')]//a//child::span[contains(text(),'$StoreName')]"
    btn_channelName_Xpath = "//div[contains(@class,'cy-channels-list')]/a/span[text()='$ChannelName']"
    tabs_store_import_Xpath = "//div[@class='ant-tabs-nav-list']//child::div//div"
    tab_name_Xpath = "//div[@class='ant-tabs-nav-list']//child::div//div[text()='$tabName']"
    txt_search_box_Xpath = "//input[@id='query']"
    btn_search_Xpath = "//button[@type='submit']/span"
    btn_import_product_Xpath = "//p[text()='$product']//parent::div/..//following-sibling::div//child::div//button//span"
    txt_product_name_productTab_Xpath = "//tbody[@class='ant-table-tbody']//tr//td//span[text()='$product']"
    txt_search_box_productTab_ClassName = "ant-input"
    btn_search_productTab_ClassName = "//span[@class='ant-input-group-addon']/button"
    lnk_product_url_Xpath = "//span[text()='$product']//..//following-sibling::td//a"
    btn_all_videos_Xpath = "(//div[@data-cy='list-item']/div)[1]"
    btn_playlist_videos_Xpath = "(//div[@data-cy='playlistHeader']/div)"
    btn_addContent_videos_Xpath = "//button[@type='button']/div[text()='Add Content']"
    btn_create_playlist_Xpath = "//span[contains(text(),'Create Playlist')]/parent::button"
    txt_channelVideo_name_Name = "name"
    btn_upload_video_Xpath = "//span[text()='Upload video']/../parent::div[@role='menuitem']"
    btn_click_to_upload_Xpath = "//span[contains(@class,'ant-upload')]//input"
    btn_create_playlistName_Xpath = "//span[contains(text(),'Create')]//parent::button[@type='submit']"
    #select_playLit_Xpath = "//tbody[@class='ant-table-tbody']//tr//td//div//child::span[text()='$playlist']"
    select_playLit_Xpath = "//span[text()='$playlist']/../parent::div[contains(@data-cy,'playlistRow')]"
    btn_add_playList_collection_Xpath = "//span[contains(text(),'Add playlist to collection')]//parent::button[@type='button']"
    txt_channelName_Xpath = "//input[@class='ant-input']"
    btn_next_channel_Xpath = "//button[@data-cy='next-button']"
    btn_create_video_Xpath = "//span[text()='Create']/parent::button"
    txt_video_caption_Name = "caption"
    btn_add_videos_to_playlist_Xpath = "//span[text()='Add videos to Playlist']/parent::button"
    btn_add_to_playlist_Xpath = "//span[text()='Add to Playlist']/parent::button"
    btn_finish_to_playlist_Xpath = "//span[text()='Finish']/parent::button"


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
                time.sleep(20)
                self.driver.switch_to.default_content()
                break
            else:
                print("**********Fireworks App Not Available under App Section********")

    def verifyAndNavigateTab(self, storeName, TabName):
        self.pp = PluginCreationPage(self.driver)
        element = self.driver.find_element(By.XPATH, self.pp.terms_frame_Xpath)
        self.driver.switch_to.frame(element)
        time.sleep(4)
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.frame_store_CSS)
        self.driver.switch_to.frame(ifr)
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_menu_bar_Xpath).click()
        time.sleep(2)
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
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element.is_displayed():
            print(ProductName + ": " + " is Available in the Product Tab")
        else:
            print(ProductName + ": " + " is Not Available in the Product Tab")

    def searchProductInProductTab(self, productName):
        element1 = self.driver.find_element(By.CLASS_NAME, self.txt_search_box_productTab_ClassName)
        element1.click()
        element1.send_keys(productName)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_search_productTab_ClassName).click()
        time.sleep(10)
        element = self.driver.find_element(By.XPATH,
                                           self.txt_product_name_productTab_Xpath.replace("$product", productName))
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if element.is_displayed():
            print(productName + ": " + " is Available in the Product Tab")
        else:
            print(productName + ": " + " is Not Available in the Product Tab")

    def navigateToProductURL(self, productName, menuName):
        self.cp = PluginCreationPage(self.driver)
        self.driver.find_element(By.XPATH, self.lnk_product_url_Xpath.replace("$product", productName)).click()
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

    def verifyAndNavigateChannelTab(self, ProfileTab, channelName):
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.frame_store_Xpath)
        self.driver.switch_to.frame(ifr)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_profile_tab_Xpath.replace("$profileTab", ProfileTab)).click()
        time.sleep(7)
        ifr1 = self.driver.find_element(By.CSS_SELECTOR, self.frame_store_CSS)
        self.driver.switch_to.frame(ifr1)
        time.sleep(5)
        #self.driver.find_element(By.XPATH, self.txt_channelName_Xpath).send_keys(channelName)
        #time.sleep(3)
        #self.driver.find_element(By.XPATH, self.btn_next_channel_Xpath).click()
        #time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_menu_bar_Xpath).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_channel_Xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_channelName_Xpath.replace("$ChannelName", channelName)).click()
        time.sleep(10)
        tabs = self.driver.find_elements(By.XPATH, self.tabs_store_import_Xpath)
        size = len(tabs)
        print(size)
        for i in range(size):
            tabText = tabs[i].text
            time.sleep(5)
            print(tabText)
            if tabText == "Videos":
                print("Videos Tab is available")
                tabs[i].click()
                time.sleep(3)
                break
            else:
                print("Tab are not available")

    def createAllVideoList(self, videoName):
        self.driver.find_element(By.XPATH, self.btn_all_videos_Xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_addContent_videos_Xpath).click()
        self.driver.find_element(By.XPATH, self.btn_upload_video_Xpath).click()
        time.sleep(5)
        self.driver.find_element(By.NAME, self.txt_video_caption_Name).send_keys(videoName)
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.btn_click_to_upload_Xpath)
        time.sleep(5)
        element.send_keys("C:\\Users\\user\\Downloads\\video_1.mp4")
        time.sleep(15)
        element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_create_video_Xpath)))
        if element.is_enabled():
            element.click()
            time.sleep(7)

    def createPlayList(self, playListName):
        self.driver.find_element(By.XPATH, self.btn_playlist_videos_Xpath).click()
        self.driver.execute_script("window.scrollBy(0,250)", "")
        time.sleep(7)
        #self.driver.find_element(By.XPATH, self.btn_create_playlist_Xpath).click()
        #time.sleep(3)
        #self.driver.find_element(By.NAME, self.txt_channelVideo_name_Name).send_keys(playListName)
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, self.btn_create_playlistName_Xpath).click()
        #self.driver.execute_script("window.scrollBy(0,50)", "")
       # time.sleep(5)
        self.driver.find_element(By.XPATH, self.select_playLit_Xpath.replace("$playlist", playListName)).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.btn_add_videos_to_playlist_Xpath).click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, self.btn_add_to_playlist_Xpath).click()
        self.driver.find_element(By.XPATH, self.btn_finish_to_playlist_Xpath).click()
        time.sleep(7)
        self.driver.switch_to.parentFrame()



