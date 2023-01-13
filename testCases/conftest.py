import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(30)
        print("Launching Chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(30)
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(30)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


#############  PyTest HTML Report #####################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Big Commerce'
    config._metadata['Module Name'] = 'Firework'
    config._metadata['Tester'] = 'RajKumar'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)