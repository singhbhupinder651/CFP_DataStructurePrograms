'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to check whether a file exists.
'''

import os
from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


def file_exists(file_name):
    """
        Description:
            Takes the parameter as file_name and print whether file exist or not.
        Parameter:
            Passed parameter file_name. 
        Return:
            Returns nothing but prints whether the file exist in the directory or not.
    """
    lg.info(os.listdir())
    if file_name in os.listdir():
        lg.info('file is available in directory')
    else:
        lg.info('file is not available in directory')


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    file_exists(file_name)
