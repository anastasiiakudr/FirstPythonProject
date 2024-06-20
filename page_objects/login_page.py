from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get()

    def execute_login(self, username: str, password: str):
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.presence_of_element_located(self.__username_field))
        self._driver.find_element(self.__username_field).send_keys(username)
        wait.until(EC.presence_of_element_located(self.__password_field))
        self._driver.find_element(self.__password_field).send_keys(password)
        wait.until(EC.presence_of_element_located(self.__submit_button))
        self._driver.find_element(self.__submit_button).click()

