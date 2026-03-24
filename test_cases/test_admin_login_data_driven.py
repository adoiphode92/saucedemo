import time
import pytest

from utilities import excel_utils
from base_pages.Login_Admin_Page import Login_Admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_02_Admin_login_data_driven:

    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data//saucedemo_testdata.xlsx"

    status_list = []

    def test_valid_admin_login_data_driven(self, setup):

        self.logger.info("******** test_valid_admin_login_data_driven ********")

        self.driver = setup
        self.driver.implicitly_wait(10)

        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_page(self.driver)

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")

        print("Number of rows:", self.rows)

        for r in range(2, self.rows + 1):

            self.username = excel_utils.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 3)

            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()

            time.sleep(3)

            act_url = self.driver.current_url

            # =========================
            # LOGIN SUCCESS
            # =========================

            if "inventory" in act_url:

                if self.exp_login == "Yes":

                    self.logger.info("Test data Passed")
                    self.status_list.append("Pass")

                    self.admin_lp.click_menu()
                    time.sleep(2)
                    self.admin_lp.click_logout()
                    time.sleep(2)

                elif self.exp_login == "No":

                    self.logger.info("Test data Failed")
                    self.status_list.append("Fail")

            # =========================
            # LOGIN FAILED
            # =========================

            else:

                if self.exp_login == "Yes":

                    self.logger.info("Test data Failed")
                    self.status_list.append("Fail")

                elif self.exp_login == "No":

                    self.logger.info("Test data Passed")
                    self.status_list.append("Pass")

        print("Status list:", self.status_list)

        if "Fail" in self.status_list:

            self.logger.info("Data Driven Test Failed")
            assert False

        else:

            self.logger.info("Data Driven Test Passed")
            assert True