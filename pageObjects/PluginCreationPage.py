import time

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
    txtbox_email_firework_Name = "email"
    btn_continue_email_Id = "btn-email-login"
    btn_authorize_Xpath = "//button[contains(text(),'Authorize')]"
    btn_create_business_Xpath = "//a[contains(text(), 'Create business')]"
    txtbox_business_form_name_Id = "business-form_name"
    txtbox_primary_email_address_Id = "business - form_primary_email_address"
    txtbox_business_form_website_Id = "business - form_website"
    btn_business_details_Xpath = "//button[contains(text(),'Save')]"
    btn_select_business_Xpath = "//button[contains(text(),'Select')]"
    btn_plugin_Xpath = "//ul[@role='group']/a/span[text()='Fireworks']"
    my_apps_link_Xpath = "//ng-transclude/child::div/h1"
    uninstall_plugin_Xpath = "//h1[contains(text(),'Fireworks')]/../../footer/a/span[text()='Uninstall']"
    back_to_main_menu_Xpath = "(//button[@aria-label='Back to main navigation'])[9]"
    btn_logOut_Xpath = "//button[contains(text(),'Log Out')]"

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

    def installApp(self):
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

    def confirmUserDetails(self, username):
        self.driver.find_element(By.NAME, self.txtbox_email_firework_Name).send_keys(username)
        self.driver.find_element(By.ID, self.btn_continue_email_Id).click()
        time.sleep(50)

    def enteringOTP(self, emailHost, mailID, mailPassword, folder):
        self.lp = LoginPage(self.driver)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(emailHost)
        self.driver.find_element(By.XPATH, self.lp.zohoMailSignIn_Xpath).click()
        self.driver.find_element(By.ID, self.lp.zohoLogIn_ID).send_keys(mailID)
        self.driver.find_element(By.ID, self.lp.zohoSignIn_ID).click()
        time.sleep(10)
        self.driver.find_element(By.ID, self.lp.zohoPassword_ID).send_keys(mailPassword)
        self.driver.find_element(By.ID, self.lp.zohoSignIn_ID).click()
        time.sleep(15)
        self.driver.find_element(By.XPATH, self.lp.zohoMailFolder_Xpath.replace("$folderName", folder)).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.lp.zohomail_Xpath).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(5)
        otpText = self.driver.find_element(By.XPATH, self.lp.zohoMailOTP_Xpath).text
        myOTP = otpText.strip(' ').split(':', 1)[1]
        finalOTP = myOTP.replace(" ", "")
        print(finalOTP)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1000)
        otp = finalOTP
        otp_split = [str(i) for i in str(otp[0])]
        for i in range(4):
            otp_elem = self.driver.find_element(By.XPATH, self.my_apps_link_Xpath).click()  # str([i + 1])
            otp_elem.send_keys(otp_split[i])

    def businessDetails(self, nameId, emailId, website):
        self.driver.find_element(By.XPATH, self.btn_authorize_Xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_create_business_Xpath).click()
        time.sleep(10)
        self.driver.find_element(By.ID, self.txtbox_business_form_name_Id).send_keys(nameId)
        self.driver.find_element(By.ID, self.txtbox_primary_email_address_Id).send_keys(emailId)
        self.driver.find_element(By.ID, self.txtbox_business_form_website_Id).send_keys(website)
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_business_details_Xpath).click()
        time.sleep(10)
        self.driver.find_element(By.ID, self.btn_select_business_Xpath).click()

    def verifyPlugInCreated(self):
        plugIn = len(self.driver.find_element(By.XPATH, self.btn_plugin_Xpath)) > 0
        if plugIn:
            print("**********Fireworks App is Installed Successfully********")
            self.driver.find_element(By.XPATH, self.btn_plugin_Xpath).click()
        else:
            print("**********Fireworks App Not Installed********")

    def myApps(self):
        self.driver.find_element(By.XPATH, self.btn_link_navigate_Xpath).click()
        time.sleep(10)

    def uninstallPlugin(self):
        apps = self.driver.find_elements(By.XPATH, self.app_link_Xpath)
        size = len(apps)
        for i in range(size):
            appText = apps[i].self.driver.find_element(By.XPATH, self.my_apps_link_Xpath).text
            if appText == "Fireworks":
                print("**********Fireworks App Available under App Section********")
            else:
                print("**********Fireworks App Not under App Section********")
        self.driver.find_element(By.XPATH, self.uninstall_plugin_Xpath).click()

    def logOut(self, menuName):
        self.driver.find_element(By.XPATH, self.back_to_main_menu_Xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName))
        self.driver.execute_script("window.scrollBy(0,100)", "")
        self.driver.find_element(By.XPATH, self.btn_logOut_Xpath).click()
