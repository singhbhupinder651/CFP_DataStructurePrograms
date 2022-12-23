'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to remove the first occurrence of a specified element from an array.
'''
from array import *
from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class Array:
    """
    Array manipulations.
    """

    def remove_first_occurrences(self, array_num: array):
        """
        Description:
            Takes the parameter as list of array and removing first occurrences from an array.
        Parameter:
            Passed parameter array_num as array.
        Return:
            Returns nothing but prints the removed element and final array.
        """
        try:
            lg.info(f'original array: {str(array_num)}')
            lg.info("Remove the first occurrence of 3 from the said array:")
            array_num.remove(3)
            lg.info(
                f'after removing first occured element in an array: {str(array_num)}')

        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    array_num = array('i', [1, 3, 5, 9, 6, 3, 8, 2])
    array_obj = Array()
    array_obj.remove_first_occurrences(array_num)
