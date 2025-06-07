import allure
import pytest
import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

# Тестовые данные
class TestData:
    BUN_NAME_1 = "Флюоресцентная булка R2-D3"
    BUN_PRICE_1 = 988
    BUN_NAME_2 = "Краторная булка N-200i"
    BUN_PRICE_2 = 1255

# Импортируем тестируемый класс
from praktikum.bun import Bun

# Фикстуры
@pytest.fixture
def bun_1():
    return Bun(TestData.BUN_NAME_1, TestData.BUN_PRICE_1)

@pytest.fixture
def bun_2():
    return Bun(TestData.BUN_NAME_2, TestData.BUN_PRICE_2)

# Тесты для класса Bun
@allure.feature('Тесты для класса Bun')
class TestBun:
    @allure.title('Проверка метода get_name для первой булки')
    def test_get_name_1(self, bun_1):
        assert bun_1.get_name() == TestData.BUN_NAME_1

    @allure.title('Проверка метода get_price для первой булки')
    def test_get_price_1(self, bun_1):
        assert bun_1.get_price() == TestData.BUN_PRICE_1

    @allure.title('Проверка метода get_name для второй булки')
    def test_get_name_2(self, bun_2):
        assert bun_2.get_name() == TestData.BUN_NAME_2

    @allure.title('Проверка метода get_price для второй булки')
    def test_get_price_2(self, bun_2):
        assert bun_2.get_price() == TestData.BUN_PRICE_2

    @allure.title('Проверка метода set_name для первой булки')
    def test_set_name_1(self, bun_1):
        new_name = "Новая булка"
        bun_1.set_name(new_name)
        assert bun_1.get_name() == new_name

    @allure.title('Проверка метода set_price для первой булки')
    def test_set_price_1(self, bun_1):
        new_price = 1000
        bun_1.set_price(new_price)
        assert bun_1.get_price() == new_price

    @allure.title('Проверка метода set_name для второй булки')
    def test_set_name_2(self, bun_2):
        new_name = "Новая булка 2"
        bun_2.set_name(new_name)
        assert bun_2.get_name() == new_name

    @allure.title('Проверка метода set_price для второй булки')
    def test_set_price_2(self, bun_2):
        new_price = 1500
        bun_2.set_price(new_price)
        assert bun_2.get_price() == new_price

    # Дополнительные тесты:
    @allure.title('Проверка, что имя булки строка')
    def test_name_is_string(self, bun_1):
        assert isinstance(bun_1.get_name(), str)

    @allure.title('Проверка, что цена булки int')
    def test_price_is_int(self, bun_1):
        assert isinstance(bun_1.get_price(), int)

    @allure.title('Проверка независимости объектов булок')
    def test_buns_are_independent(self, bun_1, bun_2):
        bun_1.set_name("Булка 3")
        assert bun_2.get_name() == TestData.BUN_NAME_2

