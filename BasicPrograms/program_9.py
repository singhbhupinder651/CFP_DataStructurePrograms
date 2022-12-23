'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to concatenate all elements in a list into a string and return it.
'''

from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


def concatenate_list(my_list):
    """
        Description:
            Takes the parameter list of random integer or string and return after concatenating all element.
        Parameter:
            Passed parameter my_list as list. 
        Return:
            Returns after concatenating all elements in a list into a string and return it.
        """

    try:
        result = ''
        for element in my_list:
            result += str(element)
        return result
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    my_list = [3, 5, 7, 8, 'Bhupinder', 'Singh']
    lg.info(concatenate_list(my_list))
