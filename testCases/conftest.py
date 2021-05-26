from selenium import webdriver
import pytest


# instead of creating driver in multiple times so we are defining here
@pytest.fixture()
def setup(browser):
    # type if you want to run testcases on diff browser
    #  pytest -v -s Hybridframework/nopcommerceApp/testCases/test_login.py --browser chrome
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("lunching chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="/home/sunil/Documents/seleniumdrivers/geckodriver-v0.29.1-linux64/geckodriver")
        print("lunching firefox browser")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI(command line interface)/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# pytest HTML reports
# it is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sunil'


#it is hook for delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
