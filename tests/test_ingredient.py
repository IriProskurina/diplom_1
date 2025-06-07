import pytest
import allure
from praktikum.ingredient import Ingredient

@pytest.fixture
def mock_sauce():
    return Ingredient("SAUCE", "Соус традиционный галактический", 88)

@pytest.fixture
def mock_filling():
    return Ingredient("FILLING", "Мясо бессмертных моллюсков Protostomia", 4142)

@pytest.fixture
def mock_sauce_2():
    return Ingredient("SAUCE", "Соус с шипами Антарианского плоскоходца", 88)

@allure.feature('Тесты класса Ingredient')
class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_fixture, expected_name, expected_price, expected_type",
        [
            ("mock_sauce", "Соус традиционный галактический", 88, "SAUCE"),
            ("mock_filling", "Мясо бессмертных моллюсков Protostomia", 4142, "FILLING"),
        ]
    )
    def test_ingredient_methods(self, request, ingredient_fixture, expected_name, expected_price, expected_type):
        ingredient = request.getfixturevalue(ingredient_fixture)
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
        assert ingredient.get_type() == expected_type

    def test_ingredient_name_is_string(self, mock_sauce):
        assert isinstance(mock_sauce.get_name(), str)

    def test_ingredient_price_is_int(self, mock_filling):
        assert isinstance(mock_filling.get_price(), int)

    def test_ingredient_type_is_string(self, mock_sauce):
        assert isinstance(mock_sauce.get_type(), str)

    @allure.title('Проверка: два ингредиента с разными названиями различны по данным')
    def test_ingredients_with_different_data_are_different(self, mock_sauce, mock_sauce_2):
        assert mock_sauce is not mock_sauce_2
        assert mock_sauce.get_name() != mock_sauce_2.get_name()



