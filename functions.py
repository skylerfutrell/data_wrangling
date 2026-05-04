# -------------------------------------------------------------------------
# Part 1 - Temperature Converter
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
    # Apply the Fahrenheit-to-Celsius conversion formula: C = (F - 32) / 1.8
    convertedTemp = (tempFahrenheit - 32) / 1.8
    return convertedTemp


# -------------------------------------------------------------------------
# Part 2 - Temperature Classifier
# -------------------------------------------------------------------------

def tempClassifier(tempCelsius):
    """
    Classifies a Celsius temperature into one of four categories:
        0 -> Cold      : below -2 °C
        1 -> Slippery  : -2 °C up to and including +2 °C
        2 -> Comfortable: above +2 °C up to and including +15 °C
        3 -> Warm      : above +15 °C

    Parameters
    ----------
    tempCelsius : float or int
        Temperature value in degrees Celsius.

    Returns
    -------
    int
        Classification code: 0, 1, 2, or 3.

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
        return 1          # Slippery (-2 and +2 inclusive)
    elif tempCelsius <= 15:
        return 2          # Comfortable (+15 inclusive)
    else:
        return 3          # Warm


# -------------------------------------------------------------------------
# Quick self-test (runs only when this file is executed directly)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Part 1 test cases
    print("48 °F in Celsius:", fahrToCelsius(48))   # Expected ~8.89
    print("71 °F in Celsius:", fahrToCelsius(71))   # Expected ~21.67
    print("32 degrees Fahrenheit in Celsius is:", fahrToCelsius(32))  # Expected 0.0

    # Part 2 test cases
    print("Class for 16.5 °C:", tempClassifier(16.5))  # Expected 3
    print("Class for +2 °C:  ", tempClassifier(2))     # Expected 1
