# test_portfolio.py
import pytest
from portfolio import Portfolio

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

def test_buy_two_stocks():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0

def test_buy_zero_shares():
    p = Portfolio()
    with pytest.raises(ValueError):
        p.buy("MSFT",0,100.00)

def test_buy_neg_shares():
    p = Portfolio()
    with pytest.raises(ValueError):
        p.buy("MSFT", -100,100.00)