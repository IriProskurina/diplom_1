import pytest
import allure
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture
def mock_bun():
    return Bun("Флюоресцентная булка R2-D3", 100)

@pytest.fixture
def mock_bun_2():
    return Bun("Краторная булка", 200)

@pytest.fixture
def mock_sauce():
    return Ingredient("SAUCE", "Соус традиционный галактический", 50)

@pytest.fixture
def mock_sauce_2():
    return Ingredient("SAUCE", "Соус Spicy-X", 75)

@pytest.fixture
def mock_filling():
    return Ingredient("FILLING", "Мясо бессмертных моллюсков Protostomia", 150)

@pytest.fixture
def mock_filling_2():
    return Ingredient("FILLING", "Сыр с астероидной плесенью", 200)

@allure.feature('Тесты для класса Burger')
class TestBurger:
    def test_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_success(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_remove_ingredient_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    def test_move_ingredient_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    def test_get_price_burger_success(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        expected_price = mock_bun_2.get_price() * 2 + mock_sauce_2.get_price() + mock_filling_2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_sauce.get_type().lower()} {mock_sauce.get_name()} =\n"
            f"= {mock_filling.get_type().lower()} {mock_filling.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt



    def test_get_price_without_bun(self):
        burger = Burger()
        assert burger.get_price() == 0

    def test_get_receipt_without_bun(self):
        burger = Burger()
        assert burger.get_receipt()  # Проверяем, что хоть какая-то строка возвращается

    def test_get_price_only_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == mock_bun.get_price() * 2

    def test_remove_ingredient_invalid_index(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        with pytest.raises(IndexError):
            burger.remove_ingredient(10)

    def test_move_ingredient_index_error(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 5)

    # Параметризация
    @pytest.mark.parametrize(
        "ingredients, expected_types",
        [
            ([("SAUCE", "Соус 1", 10)], ["sauce"]),
            ([("FILLING", "Начинка 1", 20)], ["filling"]),
            ([("SAUCE", "Соус 1", 10), ("FILLING", "Начинка 2", 20)], ["sauce", "filling"]),
        ]
    )
    def test_burger_ingredients_types(self, mock_bun, ingredients, expected_types):
        burger = Burger()
        burger.set_buns(mock_bun)
        for t, name, price in ingredients:
            burger.add_ingredient(Ingredient(t, name, price))
        actual_types = [ingredient.get_type().lower() for ingredient in burger.ingredients]
        assert actual_types == expected_types
