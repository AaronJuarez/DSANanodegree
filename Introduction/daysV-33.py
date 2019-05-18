def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    def nextDay(year, month, day):
        daysInCurrentMonth = daysInMonth(year, month)
        if day < daysInCurrentMonth:
            day += 1 
        else:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        return year, month, day

    def dateIsBefore(year1, month1, day1, year2, month2, day2):
        """Returns True if year1-month1-day1 is before
           year2-month2-day2. Otherwise, returns False."""
        if year1 < year2:
            return True
        if year1 == year2:
            if month1 < month2:
                return True
            if month1 == month2:
                return day1 < day2
        return False  

    def isLeapYear(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def daysInMonth(year, month):
        #thirty = [4,6,9,11]
        thirtyOne = [1,3,5,7,8,10,12]

        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        elif month in thirtyOne:
            return 31
        else:
            return 30
    

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
    

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()
