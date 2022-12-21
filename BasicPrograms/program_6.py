'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to calculate number of days between two dates.
            Sample dates : (2014, 7, 2), (2014, 7, 11)
            Expected output : 9 days
'''

from datetime import date
from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


def difference_date(date_1, date_2):
    """
    Description:
        Takes the parameter as as dates and return difference between two dates.
    Parameter:
        Passed parameter are date_1 and date_2. 
    Return:
        Returns with finding the difference between these two dates.
    """

    try:
        return date_2 - date_1
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    date_1 = date(year=2014, month=7, day=2)
    date_2 = date(year=2014, month=7, day=11)
    diff_obj = difference_date(date_1, date_2)
    lg.info(f'difference between two dates are {diff_obj.days} days')
