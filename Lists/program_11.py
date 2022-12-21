'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to generate all permutations of a list in Python.
'''


import itertools
from data_log import get_logger
lg = get_logger(name="(program_11)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def permutation_of_list(self, my_list: list):
        """
        Description:
            Takes the parameter as my_list and return the permutation of list.
        Parameter:
            Passed parameter my_list as list.
        Return:
            returns the print of permutation of list
        """
        try:
            lg.info(f'original list: {my_list}')
            new_list = list(itertools.permutations(my_list))
            return lg.info(f'list after permuations: {new_list}')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [1, 2, 3]
    list_obj = List()
    list_obj.permutation_of_list(my_list)
