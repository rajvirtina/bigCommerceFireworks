import time
from selenium.webdriver.common.by import By

class LoginPage:

    textbox_username_id= "user_email"
    textbox_password_id="user_password"
    button_login_id="login_submit_button"
    select_account_type_xpath = "//select[@id='account-selector']"
    button_continue_xpath= "//button[contains(text(),'Continue')]"
    select_store_type_xpath = "//select[@id='store - selector']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.button_login_id).click()
        time.sleep(100)

    def selectAccount(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()
        time.sleep(10)

    def selectStore(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()
        time.sleep(10)

    #def clickLogout(self):
        #self.driver.find_elememt_by_link_text(self.link_logout_linktext).click()
