import string
import time
import random

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage
from pageObjects.PluginCreationPage import PluginCreationPage


class CreateWidgetConfigurationPage:
    btn_add_new_widget_Xpath = "//div[@x-data='dropdown()']/button"
    btn_all_grids_Xpath = "//div[starts-with(@x-bind,'btn')]"
    btn_specific_grids_Xpath = "//div[contains(text(),'$widgetName')]/img"
    btn_widget_forms_Xpath = "form > p"
    drpdwn_channel_selects_Xpath = "(//select[@class='form-control'])[$index]"
    drpdwn_playList_selects_Xpath = "(//label[contains(text(),'PlayList List')]/../select)[$index]"
    drpdwn_videoList_selects_Xpath = "(//label[text()='Videos']/../select)[$index]"
    # txt_name_of_widget_Xpath = "(//input[@class='form-control'])['$index']"
    txt_name_of_widget_Xpath = "(//label[contains(text(),'Name for the widget')]/../input)[$index]"
    btn_save_Xpath = "(//button[contains(text(),'Save')])[$index]"
    btn_Video_Player_Location_Xpath = "(//span[contains(text(),'$position')]/../input)[1]"
    btn_Video_Player_floating_Location_Xpath = "(//span[contains(text(),'$position')]/../input)[3]"
    btn_Video_Player_grid_Location_Xpath = "(//span[contains(text(),'$position')]/../input)[2]"
    txt_video_duration_Xpath = "//input[@type='number']"
    txt_video_vertical_offset_Xpath = "(//input[@type='number'])[2]"
    txt_video_horizantal_offset_Xpath = "(//input[@type='number'])[3]"
    btn_home_Id = "nav-dashboard"
    display_widget_dashboard_Xpath = "//div[contains(@class,'flex items')]/span"
    btn_widget_edit_Xpath = "//span[contains(text(),'$widgetName')]/../following-sibling::div//child::button/span"
    btn_widget_delete_Xpath = "//span[contains(text(),'$widgetName')]/../following-sibling::div//child::button[2]"
    btn_widget_deleteAll_Xpath = "//button[@class='btn-danger']"
    btn_manage_theme_Xpath = "//span[text()='$themeManage']/parent::a[contains(@class,'button')]"
    txt_page_builder_Xpath = "//div[text()='Page Builder']"
    txt_widgetName = "//div[contains(text(),'$widgetName')]/.."
    frame_edit_web_CSS = "div > iframe"
    dragAndDrop_Xpath = "(//div[text()='Drop widgets here']/..)"
    dragAndDropSelect_Xpath = "(//div[text()='Drop widgets here']/..)[$index]"
    btn_saveweb_Xpath = "//div[text()='Save']/parent::button"
    btn_publish_Xpath = "//div[text()='Publish']/parent::button"
    btn_cnfrm_publish_Xpath = "//div[text()='Publish']/parent::button[@data-test-id='publish']"
    btn_logo_Xpath = "//div[@data-test-id='bc-logo']/parent::div"
    btn_viewStore_Xpath = "//div[contains(@class,'viewStore')]/parent::button"
    btn_reset_Xpath = "//span[contains(text(),'Reset')]/parent::button"
    btn_connect_Xpath = "//span[contains(text(),'Connect')]/parent::button"
    btn_widget_editAll_Xpath = "//span[text()='Edit']/parent::button"
    drpdwn_edit_videoText_Xpath = "(//label[text()='Videos'])[$index]"
    verify_profile_tabs_CSS = "button > p"
    txt_search_widgetName_Xpath = "//input[@class='form-control' and @type='search']"

    def __init__(self, driver):
        self.driver = driver

    def addWidget(self, ProfileTab):
        self.iis = ImportProductsIntoStorePage(self.driver)
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.iis.frame_store_Xpath)
        self.driver.switch_to.frame(ifr)
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.iis.btn_profile_tab_Xpath.replace("$profileTab", ProfileTab)).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_add_new_widget_Xpath).click()
        time.sleep(5)
        widgets = self.driver.find_elements(By.XPATH, self.btn_all_grids_Xpath)
        size = len(widgets)
        for i in range(size):
            widgetText = widgets[i].text
            print(widgetText)
            time.sleep(3)
            if widgetText == "Story Block":
                print("Story Block Widget is available")
                widgets[i].click()
                time.sleep(3)
            elif widgetText == "Floating Player":
                print("Floating Player Widget is available")
                widgets[i].click()
                time.sleep(3)
            elif widgetText == "Grid":
                print("Grid Widget is available")
                widgets[i].click()
                time.sleep(3)
            elif widgetText == "Carousel":
                print("Carousel Widget is available")
                widgets[i].click()
                time.sleep(3)
            elif widgetText == "Floating Button":
                print("Floating Button Widget is available")
                widgets[i].click()
                widgets[i].click()
                time.sleep(3)
            else:
                print("Tabs are not available")
        print("**********Five Widgets are Present in the Plugin********")

    def saveWidget(self, WidgetName, channelName, playListName, videoName, displayPositionOfVideo, positionOfVideo,
                   videoOpenIn):
        time.sleep(3)
        forms = self.driver.find_elements(By.CSS_SELECTOR, self.btn_widget_forms_Xpath)
        size1 = len(forms)
        print(size1)
        widgets = self.driver.find_elements(By.XPATH, self.btn_all_grids_Xpath)
        size = len(widgets)
        for i in range(size):
            textP = widgets[i].text
            time.sleep(6)
            print(textP)
            if textP == "* Story Block Configuration" or textP == "Story Block":
                widgets[i].click()
                time.sleep(3)
                ele = self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "1"))
                ele.click()
                ele.send_keys(WidgetName)
                time.sleep(3)
                ele.send_keys(Keys.TAB)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "1")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                sel1 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_playList_selects_Xpath.replace("$index", "1")))
                sel1.select_by_visible_text(playListName)
                time.sleep(5)
                sel2 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_videoList_selects_Xpath.replace("$index", "1")))
                sel2.select_by_visible_text(videoName)
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "1")).click()

            elif textP == "* Floating Configuration" or textP == "Floating Player":
                widgets[i].click()
                time.sleep(3)
                ele = self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "2"))
                ele.click()
                ele.send_keys(WidgetName)
                time.sleep(3)
                ele.send_keys(Keys.TAB)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "4")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                sel1 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_playList_selects_Xpath.replace("$index", "2")))
                sel1.select_by_visible_text(playListName)
                time.sleep(5)
                sel2 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_videoList_selects_Xpath.replace("$index", "2")))
                sel2.select_by_visible_text(videoName)
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "2")).click()

            elif textP == "*Carousel Configuration" or textP == "Carousel":
                widgets[i].click()
                time.sleep(3)
                self.driver.execute_script("window.scrollBy(0,100)", "")
                ele = self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "3"))
                ele.click()
                ele.send_keys(WidgetName)
                time.sleep(3)
                ele.send_keys(Keys.TAB)
                self.driver.execute_script("window.scrollBy(0,100)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "7")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                sel1 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_playList_selects_Xpath.replace("$index", "3")))
                sel1.select_by_visible_text(playListName)
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_Location_Xpath.replace("$position",
                                                                                                positionOfVideo)).click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "3")).click()

            elif textP == "*Grid Configuration" or textP == "Grid":
                widgets[i].click()
                time.sleep(3)
                ele = self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "4"))
                ele.click()
                ele.send_keys(WidgetName)
                time.sleep(3)
                ele.send_keys(Keys.TAB)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "9")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                sel1 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_playList_selects_Xpath.replace("$index", "4")))
                sel1.select_by_visible_text(playListName)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_Location_Xpath.replace("$position",
                                                                                                displayPositionOfVideo)).click()

                self.driver.find_element(By.XPATH, self.txt_video_duration_Xpath).send_keys("6")
                time.sleep(5)
                self.driver.execute_script("window.scrollBy(0,100)", "")
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_grid_Location_Xpath.replace("$position",
                                                                                                     positionOfVideo)).click()
                self.driver.execute_script("window.scrollBy(0,100)", "")
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "4")).click()

            elif textP == "* Floating Button Configuration" or textP == "Floating Button":
                widgets[i].click()
                time.sleep(3)
                ele = self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "5"))
                ele.click()
                ele.send_keys(WidgetName)
                time.sleep(3)
                ele.send_keys(Keys.TAB)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "11")))
                sel.select_by_visible_text(channelName)
                time.sleep(6)
                sel1 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_playList_selects_Xpath.replace("$index", "5")))
                sel1.select_by_visible_text(playListName)
                time.sleep(3)
                sel2 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_videoList_selects_Xpath.replace("$index", "3")))
                sel2.select_by_visible_text(videoName)
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_floating_Location_Xpath.replace("$position",
                                                                                                         positionOfVideo)).click()
                time.sleep(3)
                element1 = self.driver.find_element(By.XPATH, self.btn_Video_Player_Location_Xpath.replace("$position",
                                                                                                           videoOpenIn))
                element1.click()
                time.sleep(3)
                element1.send_keys(Keys.TAB)
                time.sleep(3)
                self.driver.execute_script("window.scrollBy(0,150)", "")
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.txt_video_vertical_offset_Xpath).send_keys("3")
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.txt_video_horizantal_offset_Xpath).send_keys("6")
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "5")).click()
            else:
                print("Configurations not available")

    def VerifyWidget(self, WidgetName):
        self.driver.execute_script("window.scrollBy(0,-200)", "")
        time.sleep(6)
        self.driver.find_element(By.XPATH, self.btn_add_new_widget_Xpath).click()
        time.sleep(4)
        widgetname = self.driver.find_elements(By.XPATH, self.display_widget_dashboard_Xpath)
        size = len(widgetname)
        for i in range(size):
            widget = widgetname[i].text
            if widget == WidgetName:
                print(WidgetName + " is saved successfully and Widget Available")
                break
            else:
                print(WidgetName + " is not saved successfully and Widget Not Available")
                break

    def editPlaylistWidget(self, playListName):
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
        element = self.driver.find_elements(By.XPATH, self.btn_widget_editAll_Xpath)
        elementSize = len(element)
        for i in range(elementSize):
            element[i].click()
            time.sleep(5)
            sel1 = Select(
                self.driver.find_element(By.XPATH, self.drpdwn_playList_selects_Xpath.replace("$index", "1")))
            sel1.select_by_visible_text(playListName)
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "6")).click()
            time.sleep(3)
            self.driver.save_screenshot(".\\Screenshots\\" + "Edited" + playListName + res + ".png")

    def editVideoNameWidget(self, videoName):
        element = self.driver.find_elements(By.XPATH, self.btn_widget_editAll_Xpath)
        elementSize = len(element)
        for i in range(elementSize):
            element[i].click()
            time.sleep(5)
            element1 = self.driver.find_element(By.XPATH, self.drpdwn_edit_videoText_Xpath.replace("$index", "1"))
            if element1.is_displayed():
                sel1 = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_videoList_selects_Xpath.replace("$index", "1")))
                sel1.select_by_visible_text(videoName)
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "6")).click()
            else:
                print("Video option is not available for the widget")

    def editPositionOfWidget(self, widgetName, positionOfVideo):
        self.driver.find_element(By.XPATH, self.btn_widget_edit_Xpath.replace("$widgetName", widgetName)).click()
        self.driver.find_element(By.XPATH, self.btn_Video_Player_floating_Location_Xpath.replace("$position",
                                                                                                 positionOfVideo)).click()
        self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "6")).click()

    def deleteWidget(self):
        element = self.driver.find_elements(By.XPATH, self.btn_widget_deleteAll_Xpath)
        elementSize = len(element)
        for i in range(elementSize):
            print(elementSize)
            element[i].click()
            break

    def dragAndDrpWidgetToPageBuilder(self, menuName, manageTheme, widgetName):  # Storefront#Customize
        self.pc = PluginCreationPage(self.driver)
        self.driver.find_element(By.ID, self.btn_home_Id).click()
        self.driver.find_element(By.XPATH, self.pc.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        self.driver.switch_to.frame(self.pc.myapps_frame_Id)
        time.sleep(5)
        if manageTheme == "Customize":
            self.driver.find_element(By.XPATH, self.btn_manage_theme_Xpath.replace('$themeManage', manageTheme)).click()
            time.sleep(5)
            self.driver.switch_to.default_content()
            ele = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_page_builder_Xpath)))
            element = self.driver.find_elements(By.XPATH, self.txt_widgetName.replace("$widgetName", widgetName))
            elementSize = len(element)
            print(elementSize)
            for i in range(elementSize):
                time.sleep(5)
                self.driver.execute_script("arguments[0].scrollIntoView();", element[i])
                time.sleep(5)
                source1 = element[i]
                time.sleep(8)
                actions2 = ActionChains(self.driver)
                actions2.click_and_hold(source1).perform()
                ifr = self.driver.find_element(By.CSS_SELECTOR, self.frame_edit_web_CSS)
                self.driver.switch_to.frame(ifr)
                time.sleep(5)
                #element1 = self.driver.find_elements(By.XPATH, self.dragAndDrop_Xpath)
               # size = len(element1)
               # for j in range(size):
                time.sleep(5)
                target1 = self.driver.find_element(By.XPATH, self.dragAndDropSelect_Xpath.replace("$index", "1"))
                actions2 = ActionChains(self.driver)
                actions2.move_to_element(target1).perform()
                break
        time.sleep(7)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, self.btn_saveweb_Xpath).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, self.btn_publish_Xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_cnfrm_publish_Xpath).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, self.btn_logo_Xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_viewStore_Xpath).click()
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.quit()

    def dragAndDrpWidgetToPageBuilder1(self, menuName, manageTheme, widgetName):  # Storefront#Customize
        self.pc = PluginCreationPage(self.driver)
        self.driver.find_element(By.ID, self.btn_home_Id).click()
        self.driver.find_element(By.XPATH, self.pc.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        self.driver.switch_to.frame(self.pc.myapps_frame_Id)
        time.sleep(5)
        if manageTheme == "Customize":
            self.driver.find_element(By.XPATH, self.btn_manage_theme_Xpath.replace('$themeManage', manageTheme)).click()
            time.sleep(5)
            self.driver.switch_to.default_content()
            ele = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_page_builder_Xpath)))
            time.sleep(5)
            element = self.driver.find_element(By.XPATH, self.txt_widgetName.replace("$widgetName", widgetName))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot(".\\Screenshots\\" + "WidgetsInPageBuilder.png")
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_logo_Xpath).click()
        time.sleep(5)

    def resetPlugIn(self, ProfileTab):
        self.ipis = ImportProductsIntoStorePage(self.driver)
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.ipis.frame_store_Xpath)
        self.driver.switch_to.frame(ifr)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.ipis.btn_profile_tab_Xpath.replace("$profileTab", ProfileTab)).click()
        time.sleep(5)
        print("Reset button is displayed")
        self.driver.find_element(By.XPATH, self.btn_reset_Xpath).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.btn_connect_Xpath).click()
        self.driver.switch_to.default_content()

    def connectPlugIn(self, ProfileTab):
        self.ipis = ImportProductsIntoStorePage(self.driver)
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.ipis.frame_store_Xpath)
        self.driver.switch_to.frame(ifr)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.ipis.btn_profile_tab_Xpath.replace("$profileTab", ProfileTab)).click()
        time.sleep(5)
        print("Connect button is displayed")
        self.driver.find_element(By.XPATH, self.btn_connect_Xpath).click()
        self.driver.switch_to.default_content()

    def verifyProfileTabs(self):
        self.iis = ImportProductsIntoStorePage(self.driver)
        ifr = self.driver.find_element(By.CSS_SELECTOR, self.iis.frame_store_Xpath)
        self.driver.switch_to.frame(ifr)
        time.sleep(5)
        element = self.driver.find_elements(By.CSS_SELECTOR, self.verify_profile_tabs_CSS)
        eleSize = len(element)
        for i in range(eleSize):
            profileTabsText = element[i].text
            time.sleep(7)
            print(profileTabsText)
            if profileTabsText == "Business Portal":
                element[i].click()
                print("Business Portal Tab is loaded")
            elif profileTabsText == "Widget Configuration":
                element[i].click()
                print("Widget Configuration Tab is loaded")
            elif profileTabsText == "Settings":
                element[i].click()
                print("Settings Tab is loaded")
            else:
                print("Iframe Not Loaded Successfully")

    def searchWidget(self, widgetName):
        element = self.driver.find_element(By.XPATH, self.txt_search_widgetName_Xpath)
        element.send_keys(widgetName)
        time.sleep(5)
        element.send_keys(Keys.ENTER)
        widgetname = self.driver.find_elements(By.XPATH, self.display_widget_dashboard_Xpath)
        size = len(widgetname)
        for i in range(size):
            widget = widgetname[i].text
            if widget == widgetName:
                print(widgetName + " is saved successfully and Widget is Available")
                break
            else:
                print(widgetName + " is not saved successfully and Widget Not Available")
                break
        element.clear()
        element.send_keys("WrongInput")
        time.sleep(5)
        element.send_keys(Keys.ENTER)
        self.driver.save_screenshot(".\\Screenshots\\" + "NoResultDisplayed.png")
