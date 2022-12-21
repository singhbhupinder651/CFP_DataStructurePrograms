'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to get the number of occurrences of a specified element in an array.
'''
from array import *
from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class Array:
    """
    Array manipulations.
    """

    def number_occurrences(self, array_num: array):
        """
        Description:
            Takes the parameter as list of array and printing number of occurrences of a specified element in an array.
        Parameter:
            Passed parameter array_num as array
        Return:
            Returns nothing but prints the number of occurrences of a specified element in an array.
        """
        try:
            lg.info(f'original array: {str(array_num)}')
            lg.info(
                f'number of occurrences of number 3 in array: {str(array_num.count(3))}')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    array_num = array('i', [1, 3, 5, 9, 6, 3, 8, 2])
    array_obj = Array()
    array_obj.number_occurrences(array_num)
