'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to sum all the items in a list.
'''

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def sum_list(self, my_list):
        """
        Description:
            Takes the parameter as list and return sum of all the items in a list.
        Parameter:
            Passed parameter my_list as list. 
        Return:
            Returns sum of all the items in a list.
        """
        try:
            total_sum = 0
            for item in my_list:
                total_sum += item
            return total_sum
            # return sum(my_list)
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    list_obj = List()
    result = list_obj.sum_list(my_list)
    lg.info(f'sum of all items in a list: {result}')
