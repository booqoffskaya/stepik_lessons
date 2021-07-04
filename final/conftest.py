import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en-GB, es, fr")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    if browser_name == "chrome":
        print(f"\nstart chrome browser ({language}) for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nstart firefox browser ({language}) for test..")
        browser = webdriver.Firefox(options=options)
    else:
        print("Browser {} still is not implemented".format(browser_name))

    yield browser
    print("\nquit browser..")
    browser.quit()
