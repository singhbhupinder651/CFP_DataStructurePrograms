'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a python program to call an external command in Python.
'''

import os
from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


if __name__ == "__main__":
    os.system("dir *.md")


