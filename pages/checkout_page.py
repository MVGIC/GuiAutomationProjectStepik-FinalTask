import allure
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class CheckoutPage(Base):
    """Класс содержащий локаторы и методы для страницы Оформления заказа"""

    # Locators

    checkout_title = "//h1[@class='section__title']"
    customer_fio_field = "//input[@name='ORDER_PROP_1']"
    phone_number_field = "//input[@name='ORDER_PROP_3']"
    email_field = "//input[@name='ORDER_PROP_2']"
    pickup_button = "//button[@data-delivery-id='3']"
    comment_field = "//textarea[@name='ORDER_DESCRIPTION']"
    cash_payment_button = "//span[@data-paysystem-id='1']"
    checkout_product_name = "//div[@class='checkout-prodcard__info']"
    checkout_order_price = "//div[@class='checkout-prodcard__price-current']"
    delivery_address = "(//div[@class='deliveryinfo__val'])[3]"
    checkbox_info = "(//span[@class='radiocheck__text'])[3]"
    checkout_price = "//span[@class='m-nowrap js-order-price']"
    checkout_button = "//button[contains(text(), 'Оформить заказ')]"

    # Getters

    def get_checkout_title(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.checkout_title)))

    def get_customer_fio_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.customer_fio_field)))

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_pickup_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.pickup_button)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_cash_payment_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cash_payment_button)))

    def get_checkout_product_name(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.checkout_product_name)))

    def get_checkout_order_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.checkout_order_price)))

    def get_delivery_address(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.delivery_address)))

    def get_checkbox_info(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_info)))

    def get_checkout_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.checkout_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def assert_checkout_title(self):
        checkout_title_value = self.get_checkout_title().text
        assert checkout_title_value == "Оформление заказа", "Некорректный заголовок страницы"
        print("Assert checkout title value")

    def input_fio(self, fio):
        self.get_customer_fio_field().send_keys(fio)
        print("Input customer fio")

    def input_phone_number(self, phone):
        self.get_phone_number_field().send_keys(phone)
        print("Input phone number")

    def input_email(self, email):
        self.get_email_field().send_keys(email)
        print("Input email")

    def click_pickup_button(self):
        self.get_pickup_button().click()
        print("Click pickup button")

    def input_comment(self, comment):
        self.get_comment_field().send_keys(comment)
        print("Input comment")

    def click_cash_payment_button(self):
        self.get_cash_payment_button().click()
        print("Click cash payment button")

    def assert_checkout_product_name(self):
        checkout_product_name = self.get_checkout_product_name().text
        assert checkout_product_name == "Смартфон Apple iPhone 14 512GB, фиолетовый", "Некорректное название товара"
        print("Assert checkout product name value")

    def assert_delivery_address(self):
        delivery_address_value = self.get_delivery_address().text
        assert delivery_address_value == "ул. 2-я Советская, 7 Бизнес-центр «Сенатор», офис 107", "Некорректный адрес доставки"
        print("Assert delivery address value")

    # def click_checkbox_info(self):
    #     self.get_checkbox_info().click()
    #     print("Click checkbox info")

    def force_click_checkbox(self):
        self.driver.execute_script("arguments[0].click();", self.get_checkbox_info())
        print("Click checkbox info forced")

    def assert_checkout_prices(self):
        checkout_order_price_value = self.get_checkout_order_price().text
        checkout_price_value = self.get_checkout_price().text
        assert checkout_order_price_value == checkout_price_value, "Некорректная цена. Цены в заказе не совпадают."
        print("Assert checkout prices values")

    # Methods (Steps)

    def make_order(self):
        with allure.step("Оформление заказа"):
            Logger.add_start_step(method="make_order")
            fake = Faker()
            self.get_current_url()
            self.assert_checkout_title()
            self.input_fio(fake.name())
            self.input_phone_number(fake.phone_number())
            self.input_email(fake.email())
            self.click_pickup_button()
            self.input_comment("Очень жду заказ")
            self.click_cash_payment_button()
            self.assert_checkout_product_name()
            self.assert_delivery_address()
            # self.click_checkbox_info()
            self.force_click_checkbox()
            self.assert_checkout_prices()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="make_order")
