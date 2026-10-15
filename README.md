# TASK-26-DATA-TIME-UTILITY# Date and Time Utility

A command-line Python utility for practical date and time calculations. It calculates age, days between dates, working days, and formatted date/time values using Python's built-in `datetime` module.

## Objective

Learn practical date and time manipulation in Python.

## Features

1. **Calculate age** - exact age in years, months and days from a birth date
2. **Days between two dates** - total number of days between any two dates
3. **Working days** - counts weekdays (Monday to Friday) between two dates, inclusive
4. **Formatted date and time** - shows the current date and time in six different formats
5. **Add or subtract days** - finds a future or past date and its day of the week
6. **Leap year check** - tells whether a given year is a leap year
7. **Sample calculations** - built-in examples that run automatically on startup

## Requirements

- Python 3.6 or higher
- No external libraries (uses only `datetime` and `calendar` from the standard library)
- No dataset or input file required

## How to Run

### VS Code / Terminal

```bash
python date_time_utility.py
```

### Google Colab

1. Create a new notebook.
2. Paste the full contents of `date_time_utility.py` into a code cell.
3. Run the cell and type your inputs in the box shown below the cell.

## Usage

When the program starts, it first prints the sample calculations, then shows a menu:

```
DATE AND TIME UTILITY
1. Calculate age
2. Days between two dates
3. Working days between two dates
4. Show date and time in different formats
5. Add days to a date
6. Check leap year
7. Show sample calculations
0. Exit
```

Enter the number of the operation you want. Dates must be entered in `YYYY-MM-DD` format, for example `2000-02-29`.

## Sample Calculations

Reference date: `2026-10-15`

| Operation | Result |
|---|---|
| Age of someone born on 2000-02-29 | 26 years, 7 months, 16 days |
| Days between 2026-10-01 and 2026-10-31 | 30 days |
| Working days from 2026-10-01 to 2026-10-31 | 22 |
| 100 days after 2026-10-15 | 2027-01-23 |
| Day of the week for 2026-10-15 | Thursday |
| Leap years check | 1900: no, 2000: yes, 2024: yes, 2026: no |

## Supported Date Formats (Output)

| Name | Example |
|---|---|
| ISO | 2026-10-15 17:32:45 |
| Long | Thursday, 15 October 2026 |
| Short | 15/10/2026 |
| US style | 10-15-2026 |
| 12-hour time | 05:32 PM |
| 24-hour time | 17:32:45 |

## Input Validation

- Invalid dates such as `2000-13-45` or `2023-02-30` are rejected and the program asks again.
- A birth date in the future is rejected.
- Non-numeric input where a number is expected is rejected and re-requested.
- Invalid menu choices show a message instead of crashing.

## Leap Year Handling

Leap years are handled by Python's `datetime` and `calendar` modules, so dates like 29 February are calculated correctly. For example, a person born on 2000-02-29 gets the correct age on any reference date.

## Project Structure

```
.
├── date_time_utility.py
└── README.md
```

## Concepts Covered

- The `datetime` module (`date`, `datetime`, `timedelta`)
- Parsing and formatting dates with `strptime` and `strftime`
- Calculating the difference between two dates
- Input validation with `try` / `except`
- Why standard libraries are preferred over manual date calculations

## Interview Questions

**What is the datetime module?**
A built-in Python module for working with dates and times. It provides classes such as `date`, `time`, `datetime` and `timedelta`.

**How do you calculate the difference between two dates?**
Subtract one date from the other. The result is a `timedelta` object, and `.days` gives the number of days.

**Why should date calculations use standard libraries?**
They correctly handle leap years, different month lengths and invalid dates, which are easy to get wrong with manual calculations.
