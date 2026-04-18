from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class PopupPage(Base):
    """Класс содержащий локаторы и методы для всплывающего окна добавления товара в корзину"""


    # Locators

    title = "//div[contains(text(), 'Товар добавлен в корзину')]"
    product_name = "//a[@class='cart-prodcard__name']"
    product_price_popup = "//div[@class='cart-prodcard__price-current']"
    move_to_cart_button = "//a[@class='btn btn_cta']"


    # Getters

    def get_popup_title(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.title)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.product_name)))

    def get_product_price_popup(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.product_price_popup)))

    def get_move_to_cart_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.move_to_cart_button)))


    # Actions

    def assert_popup_title(self):
        title_value = self.get_popup_title().text
        assert title_value == "Товар добавлен в корзину", "Некорректный заголовок окна"
        print("Assert title value")

    def assert_product_name(self):
        product_name_value = self.get_product_name().text
        assert product_name_value == "Смартфон Apple iPhone 14 512GB, фиолетовый", "Некорректное название товара"
        print("Assert product name value")

    def assert_product_price_popup(self):
        product_price_value_popup = self.get_product_price_popup().text
        assert product_price_value_popup == "54 290 ₽", "Некорректная цена товара"
        print("Assert product price popup value")

    def click_move_to_cart_button(self):
        self.get_move_to_cart_button().click()
        print("Click move to cart button")


    # Methods (Steps)

    def move_to_cart(self):
        """Проверка выбранного товара и Переход в корзину"""
        self.get_current_url()
        self.assert_popup_title()
        self.assert_product_name()
        self.assert_product_price_popup()
        self.click_move_to_cart_button()
