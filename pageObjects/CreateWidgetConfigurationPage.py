import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.ImportProductsIntoStorePage import ImportProductsIntoStorePage


class CreateWidgetConfigurationPage:
    btn_add_new_widget_Xpath = "//div[@x-data='dropdown()']/button"
    btn_all_grids_Xpath = "//div[starts-with(@x-bind,'btn')]"
    btn_specific_grids_Xpath = "//div[contains(text(),'$widgetName')]/img"
    btn_widget_forms_Xpath = "form > p"
    drpdwn_channel_selects_Xpath = "(//select[@class='form-control'])['$index']"
    txt_name_of_widget_Xpath = "(//input[@class='form-control'])['$index']"
    btn_save_Xpath = "(//button[contains(text(),'Save')])['$index']"
    btn_Video_Player_Location_Xpath = "(//span[contains(text(),'$position')]/../input)[1]"
    txt_video_duration_Xpath = "//input[@type='number']"
    display_widget_dashboard_Xpath = "//div[contains(@class,'flex items')]/span"

    def __init__(self, driver):
        self.driver = driver

    def addWidget(self, ProfileTab, WidgetName):
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
            else:
                print("Tabs are not available")
        print("**********Five Widgets are Present in the Plugin********")
        self.driver.find_element(By.XPATH, self.btn_specific_grids_Xpath.replace("$widgetName", WidgetName)).click()

    def saveWidget(self, WidgetName, channelName, positionOfVideo):
        time.sleep(3)
        forms = self.driver.find_elements(By.CSS_SELECTOR, self.btn_widget_forms_Xpath)
        size = len(forms)
        for i in range(size):
            textP = forms[i].text
            print(textP)
            if textP == "* Story Block Configuration":
                self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "i-1")).send_keys(
                    WidgetName)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "i-1")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "i-1")).click()
                break
            elif textP == "* Carousel Configuration":
                self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "i-1")).send_keys(
                    WidgetName)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "i-1")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_Location_Xpath.replace("$position", positionOfVideo))
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "i-1")).click()
                break
            elif textP == "* Grid Configuration":
                self.driver.find_element(By.XPATH, self.txt_name_of_widget_Xpath.replace("$index", "i-1")).send_keys(
                    WidgetName)
                self.driver.execute_script("window.scrollBy(0,200)", "")
                sel = Select(
                    self.driver.find_element(By.XPATH, self.drpdwn_channel_selects_Xpath.replace("$index", "i-1")))
                sel.select_by_visible_text(channelName)
                time.sleep(5)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_Location_Xpath.replace("$position",
                                                                                                         positionOfVideo))

                self.driver.find_element(By.XPATH,self.txt_video_duration_Xpath).send_keys("6")
                time.sleep(3)
                self.driver.find_element(By.XPATH, self.btn_Video_Player_Location_Xpath.replace("$position",
                                                                                                positionOfVideo))
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_save_Xpath.replace("$index", "i-1")).click()
                break
            else:
                print("Configurations not available")

    def VerifyWidget(self, WidgetName):
        widgetname = self.driver.find_elements(By.XPATH, self.display_widget_dashboard_Xpath)
        size = len(widgetname)
        for i in range(size):
            widget = widgetname[i].text
            if widget == WidgetName:
                print(WidgetName + " is saved successfully and Widget saved successfully")
                break
            else:
                print(WidgetName + " is not saved successfully and Widget saved successfully")
                break
