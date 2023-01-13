import time
import random

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage


class PluginCreationPage:
    btn_menu_Xpath = "//*[@class='cp-nav-link']/span[text()='$mainMenu']"  # Apps
    btn_link_navigate_Xpath = "//ul[@role='group']/a[text()='My Apps']"
    btn_app_list_Xpath = "//span[text()='My Draft Apps']"
    myapps_frame_Id = "content-iframe"
    app_link_Xpath = "//ng-transclude/child::div/h2"
    btn_img_app_link_Xpath = "(//ng-transclude/child::div/h2[text()='$Applink']/../../preceding::figcaption/a)[5]"
    btn_install_Xpath = "//button[@class='button button--primary']"
    terms_frame_Xpath = "//*[@title='App iframe']"
    btn_checkBox_Id = "pci_confirmation"
    btn_confirm_terms_Xpath = "//button[contains(text(),'Confirm')]"
    btn_zohoReSignIn_Xpath = "//*[contains(text(),'Access Zoho mail')]"
    text_otp_business_Xpath = "//*[@id='verification-input-code']/child::div/input[contains(@name,'code')]"
    txtbox_email_firework_Name = "email"
    btn_continue_email_Id = "btn-email-login"
    btn_authorize_Xpath = "//button[contains(text(),'Authorize')]"
    btn_create_business_Xpath = "//a[contains(text(), 'Create business')]"
    txtbox_business_form_name_Id = "business-form_name"
    txtbox_primary_email_address_Id = "business-form_primary_email_address"
    txtbox_business_form_website_Id = "business-form_website"
    btn_business_details_Xpath = "//button[contains(text(),'Save')]"
    btn_select_business_Xpath = "(//button[contains(text(),'Select')])[1]"
    btn_plugin_Xpath = "//ul[@role='group']/a/span[text()='Fireworks']"
    my_apps_link_Xpath = "//ng-transclude/child::div/h1"
    uninstall_plugin_Xpath = "//h1[contains(text(),'Fireworks')]/../../footer/a/span[text()='Uninstall']"
    back_to_main_menu_Xpath = "(//button[@aria-label='Back to main navigation'])[9]"
    btn_logOut_Xpath = "//button[contains(text(),'Log Out')]"
    text_zohoReMailOTP_Xpath = "(//td[@ align='center'])[3]"
    btn_back_menu_Xpath = "//*[@class='cp-nav-link cp-nav-link--crumb']/span[text()='$mainMenu']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnApps(self, menuName):
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_link_navigate_Xpath).click()
        self.driver.switch_to.frame(self.myapps_frame_Id)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_app_list_Xpath).click()
        time.sleep(10)

    def selectApp(self, appName):
        apps = self.driver.find_elements(By.XPATH, self.app_link_Xpath)
        for i in apps:
            appText = i.text
            print(appText)
            if appText == appName:
                print("**********Fireworks App Available********")
                element = self.driver.find_element(By.XPATH,
                                                   self.btn_img_app_link_Xpath.replace("$Applink", appText))
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(2)
                element.click()
                time.sleep(10)
                self.driver.switch_to.default_content()
                break
            else:
                print("**********Fireworks App Not Available********")

    def installApp(self, redirectedUrl):
        self.driver.switch_to.frame(self.myapps_frame_Id)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_install_Xpath).click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        time.sleep(10)
        element = self.driver.find_element(By.XPATH, self.terms_frame_Xpath)
        self.driver.switch_to.frame(element)
        time.sleep(10)
        print("entered into the frame")
        self.driver.find_element(By.ID, self.btn_checkBox_Id).click()
        self.driver.find_element(By.XPATH, self.btn_confirm_terms_Xpath).click()
        time.sleep(10)
        self.driver.switch_to.default_content()
        time.sleep(20)
        self.driver.get(redirectedUrl)

    def confirmUserDetails(self, username):
        time.sleep(10)
        self.driver.find_element(By.NAME, self.txtbox_email_firework_Name).send_keys(username)
        self.driver.find_element(By.ID, self.btn_continue_email_Id).click()
        time.sleep(50)

    def enteringOTP(self, emailHost, folder):
        self.lp = LoginPage(self.driver)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(emailHost)
        self.driver.find_element(By.XPATH, self.btn_zohoReSignIn_Xpath).click()
        time.sleep(40)
        self.driver.find_element(By.XPATH, self.lp.zohoMailFolder_Xpath.replace("$folderName", folder)).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.lp.zohomail_Xpath).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(5)
        otpText = self.driver.find_element(By.XPATH, self.text_zohoReMailOTP_Xpath).text
        myOTP = otpText.strip(' ').split(':', 1)[1]
        finalOTP = myOTP.replace(" ", "")
        print(finalOTP)
        self.lp.mailLogOut()
        time.sleep(10)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(30)
        otp = finalOTP
        otp_split = [each_num for each_num in otp]
        for i in range(4):
            otp_elem = self.driver.find_element(By.XPATH,
                                                "// *[ @ id = 'verification-input-code'] / child::div / input" + str(
                                                    [i + 2]))
            otp_elem.send_keys(otp_split[i])

    def businessDetails(self, nameId, emailId, website):
        element = self.driver.find_element(By.XPATH, self.btn_select_business_Xpath)
        if element.is_displayed():
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.btn_select_business_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.btn_create_business_Xpath).click()
            time.sleep(10)
            randomValue = random.randint(1, 100)
            self.driver.find_element(By.ID, self.txtbox_business_form_name_Id).send_keys(nameId + str(randomValue))
            time.sleep(5)
            self.driver.find_element(By.ID, self.txtbox_primary_email_address_Id).send_keys(emailId)
            time.sleep(5)
            self.driver.find_element(By.ID, self.txtbox_business_form_website_Id).send_keys(website)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_business_details_Xpath).click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.btn_select_business_Xpath).click()

    def verifyPlugInCreated(self, menuName):
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_link_navigate_Xpath).click()
        time.sleep(10)
        plugIn = self.driver.find_element(By.XPATH, self.btn_plugin_Xpath).text
        if plugIn == "Fireworks":
            print("**********Fireworks App is Installed Successfully********")
        else:
            print("**********Fireworks App Not Installed********")

    def uninstallPlugin(self, menuName):
        self.driver.switch_to.frame(self.myapps_frame_Id)
        time.sleep(10)
        apps = self.driver.find_elements(By.XPATH, self.app_link_Xpath)
        size = len(apps)
        for i in range(size):
            appText = apps[i].self.driver.find_element(By.XPATH, self.my_apps_link_Xpath).text
            if appText == "Firework":
                print("**********Fireworks App Available under App Section********")
            else:
                print("**********Fireworks App Not under App Section********")
        self.driver.find_element(By.XPATH, self.uninstall_plugin_Xpath).click()
        time.sleep(20)
        self.driver.switch_to.default_content()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_back_menu_Xpath.replace('$mainMenu', menuName)).click()

    def logOut(self, menuName):
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        self.driver.execute_script("window.scrollBy(0,250)", "")
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.btn_logOut_Xpath).click()
        print("BigCommerce Application Logged Out Successfully")
