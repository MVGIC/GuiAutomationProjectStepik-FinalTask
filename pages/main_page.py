from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    """Класс содержащий локаторы и методы для Главной страницы"""

    url = 'https://pitergsm.ru/'


    # Locators

    smartphone_button = "//li[@id='bx_651765591_1757']"
    cookie_button = "//button[@id='cookie-consent-btn']"


    # Getters

    def get_smartphone_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.smartphone_button)))

    def get_cookie_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    # Actions

    def click_smartphone_button(self):
        self.get_smartphone_button().click()
        print("Click smartphone button")

    def click_cookie_button(self):
        self.get_cookie_button().click()
        print("Click cookie button")


    # Methods (Steps)

    def select_smartphone_category(self):
        """Переход в каталог Смартфонов"""
        self.driver.get(self.url)
        self.click_cookie_button()
        self.driver.maximize_window()
        self.get_current_url()
        self.click_smartphone_button()
        self.assert_url("https://pitergsm.ru/catalog/phones/")
