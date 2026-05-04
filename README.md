# Temperature Analyzer

A Python utility that reads a week's worth of half-hourly temperature readings (in Fahrenheit), converts them to Celsius, classifies each into one of four categories, and prints a summary.

---

## Project Structure

```
.
├── functions.py       # Reusable converter and classifier functions
├── temp_analyzer.py   # Main script: data, analysis loop, and summary output
└── README.md
```

---

## How It Works

### 1. Data

`temp_analyzer.py` contains `tempData` — a list of **336 Fahrenheit readings** recorded every 30 minutes over one week.

### 2. Conversion — `fahrToCelsius(tempFahrenheit)`

Converts a Fahrenheit value to Celsius using the standard formula:

```
C = (F − 32) / 1.8
```

### 3. Classification — `tempClassifier(tempCelsius)`

Assigns each Celsius temperature to one of four classes:

| Class | Label       | Range                        |
|-------|-------------|------------------------------|
| `0`   | Cold        | Below −2 °C                  |
| `1`   | Slippery    | −2 °C to +2 °C (inclusive)   |
| `2`   | Comfortable | Above +2 °C to +15 °C (incl.)|
| `3`   | Warm        | Above +15 °C                 |

### 4. Analysis Loop

For every reading in `tempData` the script:
1. Converts it from °F to °C
2. Classifies the result
3. Appends the class code to `tempClasses`

It then counts occurrences of each class and prints a formatted summary.

---

## Usage

Run the main analysis script directly:

```bash
python temp_analyzer.py
```

**Example output:**

```
Temperature Classification Summary
======================================
Class 0 - Cold        (below -2 °C)    :   0 readings
Class 1 - Slippery    (-2 °C to +2 °C) :  56 readings
Class 2 - Comfortable (+2 °C to +15 °C):  92 readings
Class 3 - Warm        (above +15 °C)   : 188 readings
======================================
Total readings processed               : 336
```

To run the built-in self-tests for the helper functions:

```bash
python functions.py
```

---

## Requirements

- Python 3.6 or later
- No third-party dependencies
