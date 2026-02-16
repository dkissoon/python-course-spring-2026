"""
Assignment 4 - Functions and Error Handling
Small project: Unit Converter + Safe Calculator
"""

# Global variable (scope demo)
APP_NAME = "Converter & Calculator"


def miles_to_km(miles: float, precision: int = 2) -> float:
    """
    Convert miles to kilometers.

    Args:
        miles: Distance in miles.
        precision: Number of decimal places to round to (default is 2).

    Returns:
        The converted distance in kilometers, rounded to the given precision.

    Raises:
        ValueError: If miles is negative or precision is negative.
    """
    if miles < 0:
        raise ValueError("Miles cannot be negative.")
    if precision < 0:
        raise ValueError("Precision cannot be negative.")
    km = miles * 1.609344
    return round(km, precision)


def fahrenheit_to_celsius(f: float, precision: int = 2) -> float:
    """
    Convert Fahrenheit to Celsius.

    Args:
        f: Temperature in Fahrenheit.
        precision: Number of decimal places to round to.

    Returns:
        Temperature in Celsius, rounded to the given precision.
    """
    if precision < 0:
        raise ValueError("Precision cannot be negative.")
    c = (f - 32) * (5 / 9)
    return round(c, precision)


def safe_divide(a: float, b: float) -> float:
    """
    Divide a by b safely.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        Result of a / b.

    Raises:
        ZeroDivisionError: If b is 0.
    """
    return a / b  # will raise ZeroDivisionError automatically if b == 0


def get_float(prompt: str) -> float:
    """
    Prompt the user for a float with input validation.

    Args:
        prompt: The input prompt to display.

    Returns:
        A valid float entered by the user.

    Raises:
        ValueError: If user enters something that cannot be converted to float.
    """
    text = input(prompt).strip()
    return float(text)


def show_scope_demo() -> None:
    """
    Demonstrate local vs global scope.
    Prints global APP_NAME and a local variable with the same name.
    """
    APP_NAME = "Local Name (inside function)"  # local variable shadows global
    print(f"Inside function, APP_NAME = {APP_NAME}")


def main() -> None:
    """
    Main program loop that lets the user choose conversions or calculator operations.
    Demonstrates try/except for multiple error types.
    """
    print(f"Welcome to {APP_NAME}!\n")

    # Scope demonstration
    print(f"Global APP_NAME = {APP_NAME}")
    show_scope_demo()
    print(f"After function call, Global APP_NAME still = {APP_NAME}\n")

    while True:
        print("Choose an option:")
        print("1) Miles to Kilometers")
        print("2) Fahrenheit to Celsius")
        print("3) Safe Divide (a / b)")
        print("4) Quit")

        choice = input("Enter 1-4: ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                miles = get_float("Enter miles: ")
                precision = int(input("Decimal places (0-6 recommended): ").strip())
                result = miles_to_km(miles, precision)
                print(f"{miles} miles = {result} km\n")

            elif choice == "2":
                f = get_float("Enter Fahrenheit: ")
                precision = int(input("Decimal places (0-6 recommended): ").strip())
                result = fahrenheit_to_celsius(f, precision)
                print(f"{f}°F = {result}°C\n")

            elif choice == "3":
                a = get_float("Enter numerator (a): ")
                b = get_float("Enter denominator (b): ")
                result = safe_divide(a, b)
                print(f"{a} / {b} = {result}\n")

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

        except ValueError as ve:
            # Handles invalid numeric input, invalid precision, negative miles, etc.
            print(f"Input error: {ve}\n")

        except ZeroDivisionError:
            # Handles division by zero specifically
            print("Math error: You cannot divide by zero.\n")

        except Exception as e:
            # Optional: catch-all for unexpected errors (still shows the message)
            print(f"Unexpected error: {e}\n")


if __name__ == "__main__":
    main()
