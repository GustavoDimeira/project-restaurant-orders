from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501

# Req 1
def test_ingredient():
    bacon = Ingredient("bacon")

    assert bacon.name == "bacon"
    assert bacon.restrictions == {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert bacon.__repr__() == f"Ingredient('bacon')"
    assert bacon.__eq__(bacon)
    assert bacon.__hash__() == hash("bacon")
