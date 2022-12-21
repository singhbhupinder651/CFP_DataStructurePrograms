'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to find out the number of CPUs using.
'''

import os
from data_log import get_logger

lg = get_logger(name="(program_13)", file_name="data_log.log")


def find_cpu_count():
    """
        Description:
            Takes the parameter as nothing and return with printing the number of cpu's using.
        Parameter:
            Passed parameter nothing. 
        Return:
            Returns the number of cpu's using.
    """
    return lg.info(f'Number of cpus using: {os.cpu_count()}')


if __name__ == "__main__":
    find_cpu_count()
