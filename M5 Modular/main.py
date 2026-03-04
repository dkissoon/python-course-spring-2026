"""
main.py

Main program for the modular budgeting tool.

Requirements satisfied:
- Uses at least two custom modules: budget_calcs.py and report_io.py
- Uses two import styles:
    1) import budget_calcs as bc
    2) from report_io import save_report, ensure_reports_dir
- Uses at least one built-in library module: datetime
- Includes docstrings/comments throughout
"""

from __future__ import annotations

import datetime  # built-in library requirement
import budget_calcs as bc  # import style 1
from report_io import save_report, ensure_reports_dir  # import style 2


def prompt_money(prompt: str) -> float:
    """Prompt until user enters a valid non-negative money amount."""
    while True:
        raw = input(prompt).strip()
        if bc.is_valid_money(raw):
            return bc.parse_money(raw)
        print("Please enter a valid number (0 or greater). Example: 1250.50")


def prompt_non_empty(prompt: str, default: str) -> str:
    """Prompt for text; if blank, use default."""
    raw = input(prompt).strip()
    return raw if raw else default


def build_report(incomes: list[float], expenses: list[bc.Expense]) -> str:
    """Create a human-readable report string."""
    income_total = bc.total_income(incomes)
    expense_total = bc.total_expenses(expenses)
    net = bc.net_balance(incomes, expenses)
    cat_totals = bc.category_totals(expenses)
    biggest = bc.top_category(expenses)

    lines: list[str] = []
    lines.append("Personal Budget Report")
    lines.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append(f"Total Income:  ${income_total:,.2f}")
    lines.append(f"Total Expenses:${expense_total:,.2f}")
    lines.append(f"Net Balance:   ${net:,.2f}")
    lines.append("")

    lines.append("Expenses by Category:")
    if not cat_totals:
        lines.append("  (No expenses entered)")
    else:
        for cat, total in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"  {cat}: ${total:,.2f}")
        lines.append("")
        lines.append(f"Highest spend category: {biggest}")

    lines.append("")
    lines.append("Expense Details:")
    if not expenses:
        lines.append("  (No expenses entered)")
    else:
        for e in expenses:
            lines.append(f"  - {e.name} | {e.category.title()} | ${e.amount:,.2f}")

    return "\n".join(lines)


def main() -> None:
    print("Budget Tool (Modular Programming Project)")
    print("Enter your incomes and expenses. Type 'done' when finished adding expenses.")
    print("")

    incomes: list[float] = []
    expenses: list[bc.Expense] = []

    # Collect income entries (at least one)
    count_income = 1
    while True:
        amt = prompt_money(f"Income #{count_income} amount: $")
        incomes.append(amt)
        count_income += 1
        more = input("Add another income? (y/n): ").strip().lower()
        if more != "y":
            break

    print("")
    # Collect expense entries until user types done
    while True:
        name = input("Expense name (or type 'done'): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Expense name cannot be blank.")
            continue

        amount = prompt_money("Expense amount: $")
        category = prompt_non_empty("Category (press Enter for 'Uncategorized'): ", "Uncategorized")

        expenses.append(bc.Expense(name=name, amount=amount, category=category))
        print("Added.")
        print("")

    print("")
    report = build_report(incomes, expenses)
    print(report)

    # Save report with a timestamped filename
    ensure_reports_dir("reports")
    date_tag = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"budget_report_{date_tag}.txt"
    path = save_report(report, filename, "reports")

    print("")
    print(f"Saved report to: {path}")


if __name__ == "__main__":
    main()