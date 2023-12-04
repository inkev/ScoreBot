import pytest
import cogs.valo as valo
import cogs.valo_match_history as test_value


def test_check_team():
    assert valo.check_team("inkev", test_value.history[0].players) == "blue"

def test_calc_drink():
    assert valo.calc_drinks("blue", test_value.history[0]) == test_value.calc_drink_return