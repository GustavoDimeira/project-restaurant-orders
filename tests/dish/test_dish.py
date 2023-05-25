from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest

# Req 2
def test_dish():
    prato = Dish("prato", 10)

    assert prato.name == "prato"
    print(prato.get_restrictions())
    assert prato.__repr__() == f"Dish('prato', R$10.00)"
    assert prato.__eq__(prato)
    assert prato.__hash__() == hash("Dish('prato', R$10.00)")
    assert prato.get_restrictions() == set()

    prato.add_ingredient_dependency("presunto", 10)
    assert prato.get_ingredients() == set({"presunto"})

    with pytest.raises(ValueError):
        Dish("valueError", -1)
    
    with pytest.raises(TypeError):
        Dish("valueError", "sqrt(2)")
