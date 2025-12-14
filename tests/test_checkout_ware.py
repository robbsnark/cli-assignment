import pytest
from app.ware import Ware
from app.checkout import Checkout


@pytest.mark.parametrize('colour, weight, fiber, expected', [
    ('GREEN', 0, 'ACRYLIC', 5),
    ('BLACK', 7, 'MERINO WOOL', 30),
    ('BROWN', 4, 'CHENILLE', 20)
])

def test_totals(colour, weight, fiber, expected):
    ware = Ware(colour, weight, fiber)
    assert ware.price == expected

def test_empty_basket_total():
    checkout = Checkout()
    assert checkout.total() == 0

def test_unempty_basket_total():
    checkout = Checkout()
    ware = Ware('BLACK', 7, 'MERINO WOOL')
    checkout.add_ware(ware)
    assert checkout.total == 30

def test_payment_charges_wallet():
    checkout = Checkout()
    checkout.add_ware(Ware('BLACK', 7, 'MERINO WOOL'))
    checkout.pay()
    assert checkout.balance == 45