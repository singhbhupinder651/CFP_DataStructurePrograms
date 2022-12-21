'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to create a histogram from a given list of integers.
'''

from data_log import get_logger

lg = get_logger(name="(program_8)", file_name="data_log.log")


def histogram(data):
    """
    Description:
        Takes the parameter data for creating a histogram from a given list of integers.
    Parameter:
        Passed parameter data as list of integers. 
    Return:
        Returns with histogram from a given list of integers.
    """

    try:
        for element in data:
            output = ''
            times = element
            while (times > 0):
                output += '*'
                times = times - 1
            lg.info(f'Histogram: {output}')
    except Exception as e:
        lg.error(e)


if __name__ == '__main__':
    data = [3, 5, 2, 8]
    histogram(data)
