import pytest


def pytest_addoption(parser):
    """Параметр для задания url"""

    parser.addoption("--url", action="store", default="http://localhost/opencart", help="Specify opencart url")
    parser.addoption("--browser", action="store", default="Chrome", help="Select browser")






