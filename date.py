# Author: Owethu Kgatitsoe

"""
This function calculates and returns the name of the day of the week for that month, day, and year.

:param: day, month and year
:return: returns the name of day of that specific date
"""

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def get_day_of_the_week(month, day, year):
    # Step 1: Divide the last two digits by 12
    last_two_digits = year % 100
    step1 = last_two_digits // 12

    # Step 2: We find the remainder
    step2 = last_two_digits % 12

    # Step 3: We divide the remainder by 4
    step3 = step2 // 4

    # Step 4: We use the day of the month
    step4 = day

    # Step 5: We use month codes from the assignment
    month_codes = {
        1: 1, 2: 4, 3: 4, 4: 0,
        5: 2, 6: 5, 7: 0, 8: 3,
        9: 6, 10: 1, 11: 4, 12: 6
    }
    step5 = month_codes[month]

    # Add the leap-year adjustment for January and February
    if is_leap_year(year) and month in (1, 2):
        step5 += 6

    # Add the century offset
    century = year // 100
    century_offsets = {0: 6, 1: 4, 2: 2, 3: 0}
    century_offset = century_offsets[century % 4]

    # Step 6: Add the values and calculate modulo 7
    total = ( step1 + step2 + step3 + step4 + step5 + century_offset)
    
    result = total % 7

     # Convert the result into a weekday
    days = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }

    return days[result]


def main():
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))


if __name__ == "__main__":
    main()
# southern_labs-activity_5
