import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verfication(self,setup):
        self.logger.info("********Test_01_Admin_login************")
        self.logger.info("********verification of admin page title************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Swag Labs"

        if act_title == exp_title:
            self.logger.info("********test_title_verfication Title match ************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verfication.png")
            self.logger.info("********test_title_verfication Title not match ************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("********test_valid_admin_login started************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH,"//span[text()='Products']").text

        if act_dashboard_text == "Products":
            self.logger.info("********test_valid_admin_login Dashboard text found************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.logger.info("********test_valid_admin_login Dashboard text not found************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("******** test_invalid_admin_login************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,"//h3[@data-test='error']").text

        if error_message == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("******** test_invalid_admin_login error message found************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("******** test_invalid_admin_login error message not found************")
            self.driver.close()
            assert False