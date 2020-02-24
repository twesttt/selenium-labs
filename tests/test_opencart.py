from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def get_param(request):
    """Получаем значения параметров в словарь"""

    config_param = {"url": request.config.getoption("--url"), "browser": request.config.getoption('--browser')}
    return config_param


@pytest.fixture()
def launch_browser(get_param):
    browser = get_param["browser"]

    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("start-maximized")
        wd = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        options = Options()
        options.add_argument("--headless")
        wd = webdriver.Firefox(options=options)
        wd.maximize_window()
    else:
        raise Exception("Некорректно задан браузер")

    return wd


def test_response(launch_browser, get_param):
    """Отправляем get запрос по полученному url и сверяем статусы ответа"""

    launch_browser.get(get_param["url"])
    assert launch_browser.title == "Your Store"
    launch_browser.quit()
