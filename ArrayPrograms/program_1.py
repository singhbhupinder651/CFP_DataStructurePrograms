'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to create an array of 5 integers and display the array items.
            Access individual element through indexes.
'''

from array import *
from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class Array:
    """
    Array manipulations.
    """

    def search_element(self, array_num):
        """
        Description:
            Takes the parameter as list of array and printing individual items.
        Parameter:
            Passed parameter array_num as array
        Return:
            Returns nothing but prints the accessed items.
        """
        try:
            lg.info("Accessing items individually")
            lg.info(array_num[0])
            lg.info(array_num[1])
            lg.info(array_num[2])
            lg.info(array_num[3])

            lg.info("Accessing items individually using for loop")
            for element in array_num:
                lg.info(element)
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    array_num = array('i', [1, 3, 5, 9])
    print(type(array_num))  # <class 'array.array'>
    array_obj = Array()
    array_obj.search_element(array_num)
