from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.popup_page import PopupPage
from pages.smartphones_page import SmartphonesPage


def test_buy_smartphone():
    """Тест по покупке смартфона включает в себя:
            переход на страницу сайта, выбор товара, добавление товара в корзину, подтверждение покупки."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")  # или options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start test")

    main = MainPage(driver)
    main.select_smartphone_category()  # Переход в каталог Смартфонов

    sp = SmartphonesPage(driver)
    sp.select_smartphone()  # Выбор смартфона

    pp = PopupPage(driver)
    pp.move_to_cart()  # Переход в корзину

    cp = CartPage(driver)
    cp.move_to_checkout_order()  # Переход к подтверждению товара

    checkout_page = CheckoutPage(driver)
    checkout_page.make_order()  # Оформление заказа

    print("Finish Test")
    driver.quit()
