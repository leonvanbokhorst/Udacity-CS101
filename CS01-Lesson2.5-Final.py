# Credit goes to Websten from forums / Udacity
#
# Use Dave's suggestions to finish your days_between_dates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def date_is_before(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def is_leap_year(year):
    if year % 4. != 0.0:
        return False
    elif year % 100. != 0.0:
        return True
    elif year % 400. != 0.0:
        return False
    else:
        return True


def days_in_month(year, month):
    """Returns the number of days given the year and month"""

    assert year > 0
    assert 0 < month <= 12

    common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        return leap_year[month - 1]

    return common_year[month - 1]


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not date_is_before(year2, month2, day2, year1, month1, day1)

    days = 0
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585 ),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print("Test with data:", args, "failed: ", result, answer)
        else:
            print("Test case days_between_dates passed!")


test()


def test_is_leap_year():
    assert (is_leap_year(2012) == True)
    assert (is_leap_year(2013) == False)
    assert (is_leap_year(2016) == True)
    print("Test is_leap_year finished")


test_is_leap_year()


def test_days_in_month():
    test_cases = [((2012, 2), 29),
                  ((2013, 2), 28),
                  ((2016, 3), 31),
                  ((2015, 4), 30)]

    for (args, answer) in test_cases:
        result = days_in_month(*args)
        if result != answer:
            print("Test days_in_month with data:", args, "failed: ", result, answer)
        else:
            print("Test case days_in_month passed!")


test_days_in_month()