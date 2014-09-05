# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 


# returns array with number of days per month
# and the total number of days in that year
def get_year_data(year):
    common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    common_year_total = 365
    leap_year_total = 366

    if year % 4. != 0.0:
        return common_year, common_year_total
    elif year % 100. != 0.0:
        return leap_year, leap_year_total
    elif year % 400. != 0.0:
        return common_year, common_year_total
    else:
        return leap_year, leap_year_total


def days_between_dates(year1, month1, day1, year2, month2, day2):
    current_year = year1
    current_month = month1
    current_day = day1
    num_of_months = 12
    result = 0
    counter = 0

    while current_year <= year2:
        year_data, year_total = get_year_data(current_year)

        while current_month <= num_of_months:

            if current_year < year2 and current_month == 1 and current_day == 1:
                result += year_total  # add full year
                break

            if current_year == year2 and current_month > month2:
                break

            while current_day <= year_data[current_month - 1]:
                counter += 1
                if current_year < year2 and current_month != month2 and current_day == 1:
                    result += year_data[current_month - 1]  # add full month
                    break

                if current_year == year2 and current_month == month2 and current_day >= day2:
                    break

                result += 1
                current_day += 1

            current_day = 1  # reset day
            current_month += 1

        current_month = 1  # reset month
        current_year += 1

    return result


# Test routine

def test():
    test_cases = [((2011, 6, 30, 2012, 6, 30), 366)]
    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print("Test with data:", args, answer, "failed with result " + str(result))
        else:
            print("Test case passed! Result " + str(result))


test()
