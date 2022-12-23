'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to print the calendar of a given month and year.
            Note : Use 'calendar' module.
'''

import calendar
from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


def print_calendar(year, month):
    """
    Description:
        Takes the parameter as year, month and return calender for the same.
    Parameter:
        Passed parameter date and month. 
    Return:
        Returns with calender.
    """

    try:
        calender_ = calendar.month(theyear=year, themonth=month)
        return calender_
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    calendar_obj = print_calendar(year, month)
    lg.info(calendar_obj)
