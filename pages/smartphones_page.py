import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class SmartphonesPage(Base):
    """Класс содержащий локаторы и методы для страницы Смартфонов"""


    # Locators

    brand_button = "(//div[@class='filter__block js_toggle'])[5]"
    apple_filter = "(//span[contains(text(),  'Apple')])[6]"
    memory_filter = "//span[contains(text(),  '512GB')]"
    display_filter = "//span[contains(text(),  '6.1')]"
    add_to_cart_button = "(//button[@data-product-id='16060'])[3]"


    # Getters

    def get_brand_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.brand_button)))

    def get_apple_filter(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.apple_filter)))

    def get_memory_filter(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.memory_filter)))

    def get_display_filter(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.display_filter)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))


    # Actions

    def click_brand_button(self):
        self.get_brand_button().click()
        print("Click brand button")

    def click_apple_filter(self):
        self.get_apple_filter().click()
        print("Click apple option")

    def click_memory_filter(self):
        self.get_memory_filter().click()
        print("Click memory button")

    def click_display_filter(self):
        self.get_display_filter().click()
        print("Click display button")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")


    # Methods (Steps)

    def select_smartphone(self):
        """Выбор Смартфона"""
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(5)
        self.click_brand_button()
        self.click_apple_filter()
        self.click_memory_filter()
        self.click_display_filter()
        self.click_add_to_cart_button()
