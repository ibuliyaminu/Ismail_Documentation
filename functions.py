# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html


def my_adder(a: int, b: int, c: int) -> int:
    """
    Function to sum three numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: The sum of a, b, and c.
    """
    # Perform the summation
    result = a + b + c

    return result


def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """
    Changes the status of the thermostat based on temperature and desired temperature.

    Parameters:
        temp (int): The current temperature.
        desired_temp (int): The desired temperature.

    Returns:
        str: The thermostat status based on temperature and desired temperature.
    """
    if temp < desired_temp - 5:
        status = "Heat"
    elif temp > desired_temp + 5:
        status = "AC"
    else:
        status = "off"
    return status


def have_digits(s: str) -> bool:
    """
    Checks if a string has digits in it.

    Parameters:
        s (str): The input string.

    Returns:
        bool: True if the string contains digits, False otherwise.
    """
    # Initialize a flag to False
    has_digits = False

    # Loop through the string
    for c in s:
        # Check if the character is a digit
        if c.isdigit():
            has_digits = True
            break

    return has_digits


def area_of_rectangle(width: float, height: float) -> float:
    """
    Function to calculate the area of a rectangle.

    Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    # Calculate the area of the rectangle
    area = width * height

    return area


def perimeter_of_rectangle(width: float, height: float) -> float:
    """
    Function to find the perimeter of a rectangle.

    Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    # Calculate the perimeter of the rectangle
    perimeter = 2 * (width + height)

    return perimeter
