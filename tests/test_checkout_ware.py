import pytest
from app.ware import Ware
from app.checkout import Checkout

'''
things to test like

ware.py:
raises exceptions

checkout.py:
empty basket total is 0
adding wares increases total
payment deducts balance

'''

# def test_acrylic_weight_0():
#     ware = Ware('GREEN', 0, 'ACRYLIC')
#     assert ware.price == 5

# def test_merino_weight_7():
#     ware = Ware('BLACK', 7, 'MERINO WOOL')
#     assert ware.price == 30

# def test_chenille_weight_4():
#     ware = Ware('BROWN', 4, 'CHENILLE')
#     assert ware.price == 20


@pytest.mark.parametrize('colour, weight, fiber, expected', [
    ('GREEN', 0, 'ACRYLIC', 5),
    ('BLACK', 7, 'MERINO WOOL', 30),
    ('BROWN', 4, 'CHENILLE', 20)
])

def test_totals(colour, weight, fiber, expected):
    ware = Ware(colour, weight, fiber)
    assert ware.price == expected