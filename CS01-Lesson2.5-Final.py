# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def isLeapYear(year):
    if year % 4. != 0.0:
        return False
    elif year % 100. != 0.0:
        return True
    elif year % 400. != 0.0:
        return False
    else:
        return True


def daysInMonth(year, month):
    """Returns the number of days given the year and month"""

    assert year > 0
    assert 0 < month <= 12

    common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeapYear(year):
        return leap_year[month - 1]

    return common_year[month - 1]


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
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
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed: ", result, answer)
        else:
            print("Test case daysBetweenDates passed!")


test()


def test_isLeapYear():
    assert (isLeapYear(2012) == True)
    assert (isLeapYear(2013) == False)
    assert (isLeapYear(2016) == True)
    print("Test isLeapYear finished")

test_isLeapYear()


def test_daysInMonth():
    test_cases = [((2012, 2), 29),
                  ((2013, 2), 28),
                  ((2016, 3), 31),
                  ((2015, 4), 30)]

    for (args, answer) in test_cases:
        result = daysInMonth(*args)
        if result != answer:
            print("Test daysInMonth with data:", args, "failed: ", result, answer)
        else:
            print("Test case daysInMonth passed!")


test_daysInMonth()