'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to create a symmetric difference..
'''

from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def symmetric_fun(self, set1: set, set2: set):
        """
        Description:
            Takes the parameter as pair of set and print symmetric difference of sets.
        Parameter:
            Passed parameter set1 and set2. 
        Return:
            Returns the print of symmetric difference of pair of sets.
        """

        try:
            lg.info(f'set1: {set1}')
            lg.info(f'set2: {set2}')
            lg.info(
                f'Symmetric difference of given sets are {set1.symmetric_difference(set2)}')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    set1 = set([1, 2, 3, 4, 5, 6, 7])
    set2 = set([9, 8, 5, 4, 7, 3])
    set_obj = Set()
    set_obj.symmetric_fun(set1, set2)
