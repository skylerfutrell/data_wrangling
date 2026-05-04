"""
This script reads a list of half-hourly temperature readings (in degrees
Fahrenheit) recorded over one week, converts each reading to Celsius, and
classifies it into one of four temperature categories:

    0 -> Cold        (below -2 °C)
    1 -> Slippery    (-2 °C to +2 °C, inclusive)
    2 -> Comfortable (above +2 °C up to +15 °C, inclusive)
    3 -> Warm        (above +15 °C)

After processing all readings the script prints a summary showing how many
temperatures fall into each category.

Usage:
    Run this file directly:  python temp_analyzer.py
"""

# -------------------------------------------------------------------------
# Data – 336 half-hourly temperature values (°F) for one week
# -------------------------------------------------------------------------

tempData = [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 34, 34,
            34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27, 27, 27, 23, 23,
            21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 39, 39, 39, 39, 39, 39,
            41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30, 28, 27, 27, 25, 23, 23, 21, 21,
            19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 37, 39, 39, 39, 39, 41, 41, 39, 39, 39,
            39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28, 27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21,
            19, 21, 19, 21, 21, 19, 21, 27, 28, 32, 36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41,
            41, 41, 41, 39, 37, 36, 36, 34, 32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19,
            19, 19, 19, 19, 21, 23, 23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43,
            43, 43, 43, 43, 43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28,
            28, 27, 27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
            37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19, 19, 19,
            18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34, 36, 36, 36, 36,
            36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 28, 28]


# -------------------------------------------------------------------------
# Part 1 – Fahrenheit to Celsius converter
# -------------------------------------------------------------------------

def fahrToCelsius(tempFahrenheit):
    """
    Converts a temperature from degrees Fahrenheit to degrees Celsius.

    Parameters
    ----------
    tempFahrenheit : float or int
        Temperature value in degrees Fahrenheit.

    Returns
    -------
    float
        Temperature converted to degrees Celsius.

    Example
    -------
    >>> print("32 degrees Fahrenheit in Celsius is:", fahrToCelsius(32))
    32 degrees Fahrenheit in Celsius is: 0.0
    """
    # Formula: C = (F - 32) / 1.8
    convertedTemp = (tempFahrenheit - 32) / 1.8
    return convertedTemp


# -------------------------------------------------------------------------
# Part 2 – Temperature classifier
# -------------------------------------------------------------------------

def tempClassifier(tempCelsius):
    """
    Classifies a Celsius temperature into one of four categories.

    Parameters
    ----------
    tempCelsius : float or int
        Temperature value in degrees Celsius.

    Returns
    -------
    int
        0 -> Cold        (below -2 °C)
        1 -> Slippery    (-2 °C to +2 °C, inclusive at both ends)
        2 -> Comfortable (above +2 °C up to +15 °C, inclusive at +15)
        3 -> Warm        (above +15 °C)

    Example
    -------
    >>> tempClassifier(16.5)
    3
    >>> tempClassifier(2)
    1
    """
    if tempCelsius < -2:
        return 0          # Cold
    elif tempCelsius <= 2:
        return 1          # Slippery
    elif tempCelsius <= 15:
        return 2          # Comfortable
    else:
        return 3          # Warm


# -------------------------------------------------------------------------
# Part 3 – Main analysis: iterate, convert, classify, and count
# -------------------------------------------------------------------------

# Create an empty list that will hold the class number for each temperature
tempClasses = []

# Iterate over every Fahrenheit temperature in tempData
for temp in tempData:
    # Step 1: Convert the Fahrenheit value to Celsius
    tempCelsius = fahrToCelsius(temp)

    # Step 2: Classify the Celsius temperature into a class (0, 1, 2, or 3)
    tempClass = tempClassifier(tempCelsius)

    # Step 3: Append the class number to the tempClasses list
    tempClasses.append(tempClass)

# Count how many readings belong to each class
count0 = tempClasses.count(0)   # Cold
count1 = tempClasses.count(1)   # Slippery
count2 = tempClasses.count(2)   # Comfortable
count3 = tempClasses.count(3)   # Warm

# Print a readable summary of the results
print("Temperature Classification Summary")
print("=" * 38)
print(f"Class 0 - Cold        (below -2 °C)    : {count0:>4} readings")
print(f"Class 1 - Slippery    (-2 °C to +2 °C) : {count1:>4} readings")
print(f"Class 2 - Comfortable (+2 °C to +15 °C): {count2:>4} readings")
print(f"Class 3 - Warm        (above +15 °C)   : {count3:>4} readings")
print("=" * 38)
print(f"Total readings processed               : {len(tempClasses):>4}")
