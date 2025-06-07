class Burger:
    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index):
        if index < 0 or index >= len(self.ingredients):
            raise IndexError('Индекс ингредиента вне диапазона')
        del self.ingredients[index]

    def move_ingredient(self, old_index, new_index):
        if (old_index < 0 or old_index >= len(self.ingredients)
                or new_index < 0 or new_index >= len(self.ingredients)):
            raise IndexError('Индекс ингредиента вне диапазона')
        self.ingredients.insert(new_index, self.ingredients.pop(old_index))

    def get_price(self):
        if self.bun is None:
            return 0
        return self.bun.get_price() * 2 + sum(i.get_price() for i in self.ingredients)

    def get_receipt(self):
        if self.bun is None:
            return "Булка не выбрана!\n"
        receipt = f"(==== {self.bun.get_name()} ====)\n"
        for ing in self.ingredients:
            receipt += f"= {ing.get_type().lower()} {ing.get_name()} =\n"
        receipt += f"(==== {self.bun.get_name()} ====)\n\n"
        receipt += f"Price: {self.get_price()}"  # без \n на конце!
        return receipt
