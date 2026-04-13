import datetime

class Base:
    """Базовый класс, содержащий универсальные методы"""

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод проверки url"""
        current_url = self.driver.current_url
        print(f"Current url - {current_url}")

    def assert_word(self, word, result):
        """Проверка значения текста"""
        word_value = word.text
        assert word_value == result
        print("Correct word")

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = "screenshot_" + now_date + ".png"
        self.driver.save_screenshot(".\\screen\\" + name_screenshot)
        print("Скриншот выполнен")

    def assert_url(self, result):
        """Проверка значения url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Correct url")
