"""
budget_calcs.py

Purpose:
This module contains the core budgeting calculations and basic input validation.
It is imported by main.py to compute totals, net balance, and category breakdowns.

How it interacts with the program:
- main.py collects income and expenses from the user
- main.py passes those values into functions in this module
- the computed results are returned back to main.py for display and saving
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Expense:
    """Represents a single expense entry."""
    name: str
    amount: float
    category: str


def is_valid_money(value: str) -> bool:
    """
    Check whether a string can be parsed as a non-negative money amount.

    Returns:
        True if value is a number >= 0, else False.
    """
    try:
        num = float(value)
        return num >= 0
    except ValueError:
        return False


def parse_money(value: str) -> float:
    """
    Convert a string to a float money amount, raising ValueError if invalid.
    """
    if not is_valid_money(value):
        raise ValueError("Money amount must be a number greater than or equal to 0.")
    return float(value)


def total_income(incomes: List[float]) -> float:
    """Return the sum of all income amounts."""
    return round(sum(incomes), 2)


def total_expenses(expenses: List[Expense]) -> float:
    """Return the sum of all expense amounts."""
    return round(sum(e.amount for e in expenses), 2)


def net_balance(incomes: List[float], expenses: List[Expense]) -> float:
    """Return income minus expenses."""
    return round(total_income(incomes) - total_expenses(expenses), 2)


def category_totals(expenses: List[Expense]) -> Dict[str, float]:
    """
    Return a dictionary mapping category -> total spent in that category.
    """
    totals: Dict[str, float] = {}
    for exp in expenses:
        key = exp.category.strip().title() if exp.category.strip() else "Uncategorized"
        totals[key] = totals.get(key, 0.0) + exp.amount

    # Round totals for clean output
    return {k: round(v, 2) for k, v in totals.items()}


def top_category(expenses: List[Expense]) -> str:
    """
    Return the category with the highest spending.
    If there are no expenses, returns "None".
    """
    totals = category_totals(expenses)
    if not totals:
        return "None"
    return max(totals, key=totals.get)