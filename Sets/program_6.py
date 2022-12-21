'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to create an intersection of sets.
'''

from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def intersection_fun(self, set1: set, set2: set):
        """
        Description:
            Takes the parameter as pair of set and print intersection of sets.
        Parameter:
            Passed parameter set1 and set2. 
        Return:
            Returns the print of intersection of pair of sets.
        """

        try:

            lg.info(f'set1: {set1}')
            lg.info(f'set2: {set2}')
            lg.info(
                f'Intersection of given sets are {set1.intersection(set2)}')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    set1 = set([1, 2, 3, 4, 5, 6, 7])
    set2 = set([9, 8, 5, 4, 7, 3])
    set_obj = Set()
    set_obj.intersection_fun(set1, set2)
