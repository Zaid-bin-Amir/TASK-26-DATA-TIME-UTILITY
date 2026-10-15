import calendar
from datetime import date, datetime, timedelta

DATE_FORMAT = "%Y-%m-%d"


def parse_date(text):
    try:
        return datetime.strptime(text.strip(), DATE_FORMAT).date()
    except ValueError:
        raise ValueError(f"Invalid date '{text}'. Use YYYY-MM-DD and a real calendar date.")


def is_leap_year(year):
    return calendar.isleap(year)


def calculate_age(birth_date, today=None):
    today = today or date.today()
    if birth_date > today:
        raise ValueError("Birth date cannot be in the future.")

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        previous_month = today.month - 1 or 12
        previous_year = today.year if today.month > 1 else today.year - 1
        days += calendar.monthrange(previous_year, previous_month)[1]

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def days_between(first, second):
    return abs((second - first).days)


def working_days_between(start, end):
    if start > end:
        start, end = end, start

    total_days = (end - start).days + 1
    count = 0
    for offset in range(total_days):
        if (start + timedelta(days=offset)).weekday() < 5:
            count += 1
    return count


def add_days(start, number_of_days):
    return start + timedelta(days=number_of_days)


def day_of_week(target):
    return calendar.day_name[target.weekday()]


def format_datetime(value):
    return {
        "ISO": value.strftime("%Y-%m-%d %H:%M:%S"),
        "Long": value.strftime("%A, %d %B %Y"),
        "Short": value.strftime("%d/%m/%Y"),
        "US style": value.strftime("%m-%d-%Y"),
        "12-hour time": value.strftime("%I:%M %p"),
        "24-hour time": value.strftime("%H:%M:%S"),
    }


def read_date(prompt):
    while True:
        try:
            return parse_date(input(prompt))
        except ValueError as error:
            print(error)


def read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")


def run_sample_calculations():
    reference = date(2026, 10, 15)
    birth = date(2000, 2, 29)
    start = date(2026, 10, 1)
    end = date(2026, 10, 31)

    print("=" * 50)
    print("SAMPLE CALCULATIONS (reference date: 2026-10-15)")
    print("=" * 50)

    years, months, days = calculate_age(birth, reference)
    print(f"1. Age of someone born on {birth}: {years} years, {months} months, {days} days")

    print(f"2. Days between {start} and {end}: {days_between(start, end)} days")

    print(f"3. Working days (Mon-Fri) from {start} to {end}: {working_days_between(start, end)}")

    print("4. Formatted values for 2026-10-15 17:32:45:")
    for name, text in format_datetime(datetime(2026, 10, 15, 17, 32, 45)).items():
        print(f"   {name:<14}: {text}")

    print(f"5. 100 days after {reference}: {add_days(reference, 100)}")

    print(f"6. {reference} falls on a {day_of_week(reference)}")

    for year in (1900, 2000, 2024, 2026):
        status = "leap year" if is_leap_year(year) else "not a leap year"
        print(f"7. {year} is {status}")
    print("=" * 50)


def show_menu():
    print("\nDATE AND TIME UTILITY")
    print("1. Calculate age")
    print("2. Days between two dates")
    print("3. Working days between two dates")
    print("4. Show date and time in different formats")
    print("5. Add days to a date")
    print("6. Check leap year")
    print("7. Show sample calculations")
    print("0. Exit")


def main():
    run_sample_calculations()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            birth = read_date("Enter birth date (YYYY-MM-DD): ")
            try:
                years, months, days = calculate_age(birth)
                print(f"Age: {years} years, {months} months, {days} days")
            except ValueError as error:
                print(error)

        elif choice == "2":
            first = read_date("Enter first date (YYYY-MM-DD): ")
            second = read_date("Enter second date (YYYY-MM-DD): ")
            print(f"Days between: {days_between(first, second)}")

        elif choice == "3":
            first = read_date("Enter start date (YYYY-MM-DD): ")
            second = read_date("Enter end date (YYYY-MM-DD): ")
            print(f"Working days: {working_days_between(first, second)}")

        elif choice == "4":
            for name, text in format_datetime(datetime.now()).items():
                print(f"{name:<14}: {text}")

        elif choice == "5":
            start = read_date("Enter start date (YYYY-MM-DD): ")
            amount = read_int("Number of days to add (negative to subtract): ")
            print(f"Result: {add_days(start, amount)} ({day_of_week(add_days(start, amount))})")

        elif choice == "6":
            year = read_int("Enter a year: ")
            if year < 1:
                print("Year must be positive.")
            else:
                print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}")

        elif choice == "7":
            run_sample_calculations()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from the menu.")


if __name__ == "__main__":
    main()