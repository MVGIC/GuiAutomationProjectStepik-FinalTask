from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    """Класс содержащий локаторы и методы для страницы Корзины"""


    # Locators

    cart_title = "//h1[@class='section__title']"
    cart_product_name = "//a[@class='cart-prodcard__name']"
    total_price = "//div[@class='total__price']"
    move_to_checkout_button = "(//a[@class='btn btn_cta'])[1]"


    # Getters

    def get_cart_title(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_title)))

    def get_cart_product_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_name)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.total_price)))

    def get_move_checkout_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.move_to_checkout_button)))


    # Actions

    def assert_cart_title(self):
        cart_title_value = self.get_cart_title().text
        assert cart_title_value == "Корзина", "Некорректный заголовок страницы"
        print("Assert cart title value")

    def assert_cart_product_name(self):
        cart_product_name = self.get_cart_product_name().text
        assert cart_product_name == "Смартфон Apple iPhone 14 512GB, фиолетовый", "Некорректное название товара"
        print("Assert cart product name value")

    def assert_total_price(self):
        total_price_value = self.get_total_price().text
        assert total_price_value == "54 290 ₽", "Некорректная цена товара"
        print("Assert total price value")

    def click_move_checkout_button(self):
        self.get_move_checkout_button().click()
        print("Click checkout button")


    # Methods (Steps)

    def move_to_checkout_order(self):
        """Проверка добавленного в корзину товара и переход к оформлению"""
        self.get_current_url()
        self.assert_cart_title()
        self.assert_cart_product_name()
        self.assert_total_price()
        self.click_move_checkout_button()
