import math

def magnitude(x, y):
    """
    (float, float) -> float

    Calculate and return the magnitude of the vector (x, y) rounded to 3 decimal places.

    Parameters
    ----------
    x : float
        The x-coordinate of the vector.
    y : float
        The y-coordinate of the vector.

    Returns
    -------
    float
        The magnitude of the vector (x, y).

    Examples
    --------
    >>> magnitude(3.0, 4.0)
    5.0
    """
    mag = math.sqrt(x ** 2 + y ** 2)
    mag_3_decimal = round(mag, 3)
    return mag_3_decimal

## Run a simple test
# Step 1: Define the input values
x = 3.0
y = 4.0
# Step 2: Call the function and store the result in a variable
r = magnitude(x, y)
# Step 3: Print the result
print("The function computed a magnitude of ", r)  # Expected output: 5.0

# Test 2 - Make x negative (coordinates in the 2nd quadrant)
x = -3.0
y = 4.0
r = magnitude(x, y)
print("Test 2: The function computed a magnitude of ", r)  # Expected output: 5.0

## Test 3 - Coordinate in 3rd quadrant
x = -1.0
y = -1.0
r = magnitude(x, y)
print("Test 3: The function computed a magnitude of ", r)  # Expected output: 1.414

## Test 4 - Coordinate in 4th quadrant
x = 2.0
y = -10.0
r = magnitude(x, y)
print("Test 4: The function computed a magnitude of ", r)  # Expected output: 10.198

## Test 5 - Coordinate on the x-axis
x = 5.5
y = 0.0
r = magnitude(x, y)
print("Test 5: The function computed a magnitude of ", r)  # Expected output: 5.5

## Test 6 - Coordinate on the y-axis
x = 0.0
y = -7.15
r = magnitude(x, y)
print("Test 6: The function computed a magnitude of ", r)  # Expected output: 7.15

# Test 7 - Origin
x = 0.0
y = 0.0
r = magnitude(x, y)
print("Test 7: The function computed a magnitude of ", r)  # Expected output: 0.0