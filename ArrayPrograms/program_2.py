'''
    @@Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to reverse the order of the items in the array.
'''
from array import *
from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class Array:
    """
    Array manipulations.
    """

    def reverse_order(self, array_num: array):
        """
        Description:
            Takes the parameter as list of array and printing reverse the order of the items in the array.
        Parameter:
            Passed parameter array_num as array
        Return:
            Returns nothing but prints the reverse order of the items in the array.
        """
        try:
            lg.info(f'original array: {str(array_num)}')
            array_num.reverse()
            lg.info(f'array after reversing: {str(array_num)}')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    array_num = array('i', [1, 3, 5, 9, 6, 3, 8, 2])
    array_obj = Array()
    array_obj.reverse_order(array_num)
