from typing import List

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class Database:
    """
    Класс с методами по работе с базой данных.
    """

    def __init__(self):
        self._buns: List[Bun] = []
        self._ingredients: List[Ingredient] = []

        self._buns.append(Bun("black bun", 100))
        self._buns.append(Bun("white bun", 200))
        self._buns.append(Bun("red bun", 300))

        self._ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        self._ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200))
        self._ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300))

        self._ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        self._ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200))
        self._ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))

    def available_buns(self) -> List[Bun]:
        # Возвращаем копию списка!
        return list(self._buns)

    def available_ingredients(self) -> List[Ingredient]:
        # Возвращаем копию списка!
        return list(self._ingredients)


