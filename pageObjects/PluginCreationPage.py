import time
import random

from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class PluginCreationPage:
    redirectedUrl = ReadConfig.getRedirectedURL()
    emailId = ReadConfig.getMailId()
    NameId = ReadConfig.getnameID()
    websiteId = ReadConfig.getWebsite()
    emailHost = ReadConfig.getHostName()

    btn_home_Id = "nav-dashboard"
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
    btn_select_business_Xpath = "//span[text()='$nameID']/../../button"
    txtbox_primary_email_address_Id = "business-form_primary_email_address"
    txtbox_business_form_website_Id = "business-form_website"
    btn_business_details_Xpath = "//button[contains(text(),'Save')]"
    #btn_select_business_Xpath = "(//button[contains(text(),'Select')])[1]"
    btn_plugin_Xpath = "//ul[@role='group']/a/span[text()='Firework']"
    my_apps_link_Xpath = "//ng-transclude/child::div/h1"
    uninstall_plugin_Xpath = "//h1[contains(text(),'Firework')]/../../footer/a/span[text()='Uninstall']"
    back_to_main_menu_Xpath = "(//button[@aria-label='Back to main navigation'])[9]"
    btn_logOut_Xpath = "//button[contains(text(),'Log Out')]"
    text_zohoReMailOTP_Xpath = "(//td[@ align='center'])[3]"
    btn_back_menu_Xpath = "//*[@class='cp-nav-link cp-nav-link--crumb']/span[text()='$mainMenu']"
    business_store_verify_Xpath = "//span[@class='business-name' and contains(text(),'$businessName')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnApps(self, menuName):
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_link_navigate_Xpath).click()
        self.driver.switch_to.frame(self.myapps_frame_Id)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_app_list_Xpath).click()
        time.sleep(5)
        self.driver.switch_to.default_content()

    def selectApp(self, appName):
        self.driver.switch_to.frame(self.myapps_frame_Id)
        time.sleep(3)
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
        time.sleep(20)
        self.driver.get(self.redirectedUrl)

    def confirmUserDetails(self):
        time.sleep(10)
        element = self.driver.find_element(By.NAME, self.txtbox_email_firework_Name)
        emailID = element.get_attribute("value")
        print("Email ID Populated:" + emailID)
        time.sleep(5)

    def enteringOTP(self):
        element = self.driver.find_element(By.NAME, self.txtbox_email_firework_Name)
        emailID = element.get_attribute("value")
        mail = emailID.strip('@').split('@', 1)[0]
        print(mail)
        self.driver.find_element(By.ID, self.btn_continue_email_Id).click()
        self.lp = LoginPage(self.driver)
        time.sleep(10)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.emailHost + mail)
        time.sleep(40)
        elements = self.driver.find_elements(By.XPATH, self.lp.allMails_Xpath.replace("$UserName", mail))
        for element in elements:
            time.sleep(10)
            element.click()
            break
        ifr = self.driver.find_element(By.XPATH, self.lp.message_body_frame_Xpath)
        self.driver.switch_to.frame(ifr)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(5)
        otpText = self.driver.find_element(By.XPATH, self.lp.mailinator_otp_xpath).text
        myOTP = otpText.strip(' ').split(':', 1)[1]
        finalOTP = myOTP.replace(" ", "")
        print(finalOTP)
        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        otp = finalOTP
        otp_split = [each_num for each_num in otp]
        for i in range(4):
            otp_elem = self.driver.find_element(By.XPATH,
                                                "// *[ @ id = 'verification-input-code'] / child::div / input" + str(
                                                    [i + 2]))
            otp_elem.send_keys(otp_split[i])

    def enteringZohoOTP(self, emailHost, folder):
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
        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        otp = finalOTP
        otp_split = [each_num for each_num in otp]
        for i in range(4):
            otp_elem = self.driver.find_element(By.XPATH,
                                                "// *[ @ id = 'verification-input-code'] / child::div / input" + str(
                                                    [i + 2]))
            otp_elem.send_keys(otp_split[i])

    def CreateNewBusinessDetails(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.btn_create_business_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(10)
        randomValue = random.randint(1, 100)
        name = self.NameId + str(randomValue)
        self.driver.find_element(By.ID, self.txtbox_business_form_name_Id).send_keys(name)
        time.sleep(5)
        self.driver.find_element(By.ID, self.txtbox_primary_email_address_Id).send_keys(self.emailId)
        time.sleep(5)
        self.driver.find_element(By.ID, self.txtbox_business_form_website_Id).send_keys(self.websiteId)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_business_details_Xpath).click()
        time.sleep(20)
        self.driver.save_screenshot(".\\Screenshots\\" + "BusinessCreated.png")
        t = self.driver.find_element(By.XPATH, self.business_store_verify_Xpath.replace("$businessName", name))
        print(t.is_displayed())

    def businessDetails(self):
        time.sleep(6)
        element = self.driver.find_element(By.XPATH, self.btn_select_business_Xpath.replace("$nameID", self.NameId))
        if element.is_displayed():
            time.sleep(10)
            element.click()
        else:
            self.driver.find_element(By.XPATH, self.btn_create_business_Xpath).click()
            time.sleep(10)
            randomValue = random.randint(1, 100)
            self.driver.find_element(By.ID, self.txtbox_business_form_name_Id).send_keys(self.NameId + str(randomValue))
            time.sleep(5)
            self.driver.find_element(By.ID, self.txtbox_primary_email_address_Id).send_keys(self.emailId)
            time.sleep(5)
            self.driver.find_element(By.ID, self.txtbox_business_form_website_Id).send_keys(self.websiteId)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_business_details_Xpath).click()
            time.sleep(20)
            self.driver.find_element(By.XPATH, self.btn_select_business_Xpath.replace("$nameID", self.NameId)).click()

    def verifyPlugInCreated(self, menuName):
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_link_navigate_Xpath).click()
        time.sleep(10)
        plugIn = self.driver.find_element(By.XPATH, self.btn_plugin_Xpath).text
        if plugIn == "Firework":
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
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, self.btn_home_Id).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.btn_menu_Xpath.replace('$mainMenu', menuName)).click()
        self.driver.execute_script("window.scrollBy(0,250)", "")
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.btn_logOut_Xpath).click()
        print("BigCommerce Application Logged Out Successfully")
        self.driver.close()
