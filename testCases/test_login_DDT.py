import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


# Data Driven Testing
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "TestData/LoginData.xlsx"
    # static method is called by using class name
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("**** Test_002_DDT_Login ****")
        self.logger.info("**** Verify DDT on test_Login ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("no of rows:", self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readDate(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readDate(self.path, 'Sheet1', r, 2)
            self.excepted = XLUtils.readDate(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setUserPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.excepted == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.excepted == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif actual_title != expected_title:
                if self.excepted == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.excepted == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test cases is passed")
            self.driver.close()
            assert True
        else:
            self.logger.error("Login DDT test cases is failed")
            self.driver.close()
            assert False

        self.logger.info("********** End of the Login DDT Test cases ********")
        self.logger.info("********** completed Test_002_DDT_Login ********")



# run only regression testcases
# pytest -v -s -m "regression" --capture=sys --html=Hybridframework/nopcommerceApp/Reports/sanity_report.html Hybridframework/nopcommerceApp/testCases/ --browser chrome

# sunil@sunil-Vostro-3558:~/Documents/seleniumpython$ pytest -v -s --capture=sys --html=Hybridframework/nopcommerceApp/Reports/report.html Hybridframework/nopcommerceApp/testCases/test_login_DDT.py --browser chrome