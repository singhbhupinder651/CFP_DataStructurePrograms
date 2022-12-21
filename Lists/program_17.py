'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to remove duplicates from a list of lists.
            Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
            New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

from re import I
from data_log import get_logger
lg = get_logger(name="(program_17)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def remove_duplicates(self, my_list):
        """
        Description:
            Takes the parameter as my_list and prints the new list after removing duplicates.
        Parameter:
            Passed parameter my_list as list.
        Return:
            returns nothing but prints the list new list after removing duplicates.
        """
        try:
            lg.info(f'original list: {my_list}')
            new_list = []
            my_list.sort()
            for element in my_list:
                if element not in new_list:
                    new_list.append(element)
            lg.info(f"new list after removing duplicates: {new_list}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    list_obj = List()
    list_obj.remove_duplicates(my_list)
