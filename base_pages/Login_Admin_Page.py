from selenium.webdriver.common.by import By


class Login_Admin_page:

    textbox_username_id = "user-name"
    textbox_password_id = "password"
    btn_login_id = "login-button"

    menu_btn_id = "react-burger-menu-btn"
    logout_link_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def click_menu(self):
        self.driver.find_element(By.ID, self.menu_btn_id).click()

    def click_logout(self):
        self.driver.find_element(By.ID, self.logout_link_id).click()