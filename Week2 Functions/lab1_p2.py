import math 

def phase(x, y):
    """
    (float, float) -> float

    Calculate and return the phase of the vector (x, y) in radians rounded to 3 decimal places.

    Parameters
    ----------
    x : float
        The x-coordinate of the vector.
    y : float
        The y-coordinate of the vector.

    Returns
    -------
    float
        The phase of the vector (x, y) in degrees.

    Examples
    --------
    >>> phase(3.0, 4.0)
    0.927
    """
    angle = math.atan2(y, x) # calculate the arctan from y and x given
    angle_3_decimal = round(angle, 3) # round to 3 decimal spaces
    return angle_3_decimal

## Test the function with the same test cases as the magnitude function
# Test 1 - Quadrant 1
x = 3.0
y = 4.0
r = phase(x, y)
print("Test 1: The function computed a phase of ", r)  # Expected output: 0.927

# Test 2 - Quadrant 2
x = -3.0
y = 4.0
r = phase(x, y)
print("Test 2: The function computed a phase of ", r)  # Expected output: 2.214

# Test 3 - Quadrant 3
x = -1.0
y = -1.0
r = phase(x, y)
print("Test 3: The function computed a phase of ", r)  # Expected output: -2.356

# Test 4 - Quadrant 4
x = 2.0
y = -10.0
r = phase(x, y)
print("Test 4: The function computed a phase of ", r)  # Expected output: -1.373

# Test 5 - x-axis
x = 5.5
y = 0.0
r = phase(x, y)
print("Test 5: The function computed a phase of ", r)  # Expected output: 0.0

# Test 6 - y-axis
x = 0.0
y = -7.15
r = phase(x, y)
print("Test 6: The function computed a phase of ", r)  # Expected output: -1.571

# Test 7 - Origin
x = 0.0
y = 0.0
r = phase(x, y)
print("Test 7: The function computed a phase of ", r)  # Expected output: 0.0