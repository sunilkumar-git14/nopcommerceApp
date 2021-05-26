class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_id = "//button[contains(text(),'Log in')]"
    linktext_logout_id = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.linktext_logout_id).click()

