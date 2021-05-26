import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    # static method is called by using class name
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("**** Test_001_Login ****")
        self.logger.info("**** Verify test_homepageTitle ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**** Home page title testcase is passed ****")
        else:
            self.driver.save_screenshot("Screenshots/test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**** Home page title testcase is failed ****")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("**** Verify Login Test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**** Login page title testcase is passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot("Screenshots/test_Login.png")
            self.driver.close()
            self.logger.error("**** Login page title testcase is failed ****")
            assert False

# running command
# sunil@sunil-Vostro-3558:~/Documents/seleniumpython$ pytest -v -s Hybridframework/nopcommerceApp/testCases/test_login.py

# type if you want to run testcases on diff browser
# sunil@sunil-Vostro-3558:~/Documents/seleniumpython$ pytest -v -s Hybridframework/nopcommerceApp/testCases/test_login.py --browser firefox

# type if you want to run testcases on diff browser
# sunil@sunil-Vostro-3558:~/Documents/seleniumpython$ pytest -v -s Hybridframework/nopcommerceApp/testCases/test_login.py --browser chrome

# to run testcases on parallel browser
# sunil@sunil-Vostro-3558:~/Documents/seleniumpython$ pytest -v -s -n=2 Hybridframework/nopcommerceApp/testCases/test_login.py --browser firfox

# to get the html reports type below command
# sunil@sunil-Vostro-3558:~/Documents/seleniumpython$ pytest -v -s -n=2 --html=Hybridframework/nopcommerceApp/Reports/report.html Hybridframework/nopcommerceApp/testCases/test_login.py --browser chrome

# run only regression and sanity testcases
# -m to refer the markers in pytest.ini file
# pytest -v -s -m "regression and sanity" --capture=sys --html=Hybridframework/nopcommerceApp/Reports/sanity_report.html Hybridframework/nopcommerceApp/testCases/ --browser chrome