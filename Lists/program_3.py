'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to get the smallest number from a list..
'''

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def mimimum_number(self, my_list: list):
        """
        Description:
            Takes the parameter as list and print the smallest number from a list.
        Parameter:
            Passed parameter my_list as list. 
        Return:
            Returns nothing but print the smallest number from a list.
        """
        try:
            lg.info(f"original list: {my_list}")
            my_list.sort()
            lg.info(f"after soting list: {my_list}")
            lg.info(f"minimum number in a list: {my_list[0]}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [5, 8, 3, 1, 4]
    list_obj = List()
    list_obj.mimimum_number(my_list)
