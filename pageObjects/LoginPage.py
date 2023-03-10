import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_username_id = "user_email"
    textbox_password_id = "user_password"
    button_login_id = "login_submit_button"
    select_account_type_xpath = "//select[@id='account-selector']"
    button_continue_xpath = "//button[contains(text(),'Continue')]"
    select_store_type_xpath = "//select[@id='store - selector']"
    link_logout_linktext = "Logout"
    otpVerifyPage_ID = "device_verification_otp_code"
    verifyPageSubmit_Xpath = "//input[@name='commit' and @value='Verify']"
    zohoMailSignIn_Xpath = "//a[contains(text(),'SIGN IN') and @class='zlogin-apps']"
    zohoLogIn_ID = "login_id"
    zohoPassword_ID = "password"
    zohoSignIn_ID = "nextbtn"
    zohoRemind_XPATH = "//a[contains(text(),'Remind me later')]"
    zohoMailFolder_Xpath = "//span[contains(text(),'$folderName')]"
    zohomail_Xpath = "(//div[contains(@class,'zmList')])[1]"
    zohoMailOTP_Xpath = "(//td[@align='left' and @valign='top'])[17]/div/div/div/p/span"
    zohoMailProfileImg_Xpath = "//img[@class='zmavatar__image']"
    zohoMailSignOut_Xpath = "//button/child::span[contains(text(),'Sign out')]"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def selectAccount(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()

    def selectStore(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()

    def mailLogIn(self, emailHost, mailID, mailPassword, folder, text):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(emailHost)
        self.driver.find_element(By.XPATH, self.zohoMailSignIn_Xpath).click()
        self.driver.find_element(By.ID, self.zohoLogIn_ID).send_keys(mailID)
        self.driver.find_element(By.ID, self.zohoSignIn_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.zohoPassword_ID).send_keys(mailPassword)
        self.driver.find_element(By.ID, self.zohoSignIn_ID).click()
        self.driver.find_element(By.XPATH, self.zohoMailFolder_Xpath.replace("$folderName", folder)).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, self.zohomail_Xpath).click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(5)
        otpText = self.driver.find_element(By.XPATH, self.zohoMailOTP_Xpath).text
        myOTP = otpText.strip(' ').split(' ', 1)[0]
        print(myOTP)
        if text.__eq__("signOut"):
            self.mailLogOut()
        elif text.__eq__("continue"):
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        else:
            print("Mail Got Terminated")
        time.sleep(10)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(5)
        self.driver.find_element(By.ID, self.otpVerifyPage_ID).click()
        self.driver.find_element(By.ID, self.otpVerifyPage_ID).send_keys(myOTP)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.verifyPageSubmit_Xpath).click()

    def mailLogOut(self):
        self.driver.find_element(By.XPATH, self.zohoMailProfileImg_Xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.zohoMailSignOut_Xpath)))
        self.driver.find_element(By.XPATH, self.zohoMailSignOut_Xpath).click()
        time.sleep(2)
