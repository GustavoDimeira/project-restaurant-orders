import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        data = pd.read_csv(source_path)
        for line in data.itertuples(index=False):
            dish, price, ingredient, recipe_amount = line
            is_new = True

            for item in self.dishes:
                if item.name == dish:
                    item.add_ingredient_dependency(
                        Ingredient(ingredient), int(recipe_amount)
                    )
                    is_new = False

            if is_new:
                new_dish = Dish(dish, price)
                new_dish.add_ingredient_dependency(
                    Ingredient(ingredient), int(recipe_amount)
                )
                self.dishes.add(new_dish)
