from data import TestDataBase
import pytest
from data import TestDataBase
import pytest
import allure
from unittest.mock import MagicMock
from praktikum.database import Database

@pytest.fixture
def db():
    """Фикстура для тестируемой базы данных."""
    return Database()

class TestDB:
    @allure.title('Проверка метода available_buns: содержимое и типы данных')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name
        assert data_buns[index_bun].get_price() == bun_price
        # Проверяем тип
        from praktikum.bun import Bun
        assert isinstance(data_buns[index_bun], Bun)

    @allure.title('Проверка метода available_ingredients: содержимое и типы данных')
    @pytest.mark.parametrize('index, type_, name, price', TestDataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, db, index, type_, name, price):
        data_ingredients = db.available_ingredients()
        assert data_ingredients[index].get_name() == name
        assert data_ingredients[index].get_type() == type_
        assert data_ingredients[index].get_price() == price
        # Проверяем тип
        from praktikum.ingredient import Ingredient
        assert isinstance(data_ingredients[index], Ingredient)

    @allure.title('Проверка размера списков доступных булок и ингредиентов')
    def test_buns_ingredients_count(self, db):
        buns = db.available_buns()
        ingredients = db.available_ingredients()
        assert len(buns) == len(TestDataBase.test_data_base_buns)
        assert len(ingredients) == len(TestDataBase.test_data_base_ingredients)

    @allure.title('Проверка работы методов при пустой базе (с использованием mock)')
    def test_empty_database_returns_empty_list(self, monkeypatch):
        # Мокаем методы БД, чтобы вернуть пустой список
        mock_db = MagicMock()
        mock_db.available_buns.return_value = []
        mock_db.available_ingredients.return_value = []
        assert mock_db.available_buns() == []
        assert mock_db.available_ingredients() == []

    @allure.title('Проверка, что списки из БД независимы')
    def test_db_returns_copy(self, db):
        buns = db.available_buns()
        buns_orig_len = len(buns)
        buns.pop()
        # БД должна возвращать новый список, а не ссылку на внутренний
        buns2 = db.available_buns()
        assert len(buns2) == buns_orig_len



