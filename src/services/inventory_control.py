from csv import DictReader
from typing import Dict

from models.dish import Recipe
from models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe):
        try:
            for ingredient in recipe:
                if (self.inventory[ingredient] < recipe[ingredient]):
                    return False
            return True
        except KeyError:
            return False

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if (self.check_recipe_availability(recipe)):
            for ingredient in recipe:
                self.inventory[ingredient] -= recipe[ingredient]
        else:
            raise ValueError
