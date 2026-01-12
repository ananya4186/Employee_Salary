import pytest
from employee_salary import calculate_salary


# -------- INVALID INPUT TEST --------
def test_invalid_basic_salary():
    gross, net = calculate_salary(0)
    assert gross == -1
    assert net == -1


# -------- LOWER SALARY (NO TAX) --------
def test_low_salary_no_tax():
    gross, net = calculate_salary(20000)
    assert gross == 26000      # 20000 + 20% + 10%
    assert net == 26000        # no tax


# -------- MID SALARY (10% TAX) --------
def test_mid_salary_tax_10_percent():
    gross, net = calculate_salary(40000)
    assert gross == 52000
    assert net == gross - (0.10 * gross)


# -------- HIGH SALARY (20% TAX) --------
def test_high_salary_tax_20_percent():
    gross, net = calculate_salary(70000)
    assert gross == 91000
    assert net == gross - (0.20 * gross)


# -------- EXACT BOUNDARY: 50000 --------
def test_exact_50000_boundary():
    gross, net = calculate_salary(50000)
    assert gross == 65000
    assert net == gross - (0.10 * gross)


# -------- EXACT BOUNDARY: 80000 --------
def test_exact_80000_boundary():
    gross, net = calculate_salary(80000)
    assert gross == 104000
    assert net == gross - (0.20 * gross)
