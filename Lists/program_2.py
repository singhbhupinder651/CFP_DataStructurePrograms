'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to multiplies all the items in a list.
'''

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def multiplication_list(self, my_list):
        """
        Description:
            Takes the parameter as list and return multiplication value of all the items in a list.
        Parameter:
            Passed parameter my_list as list. 
        Return:
            Returns multiplication value of all the items in a list.
        """
        try:
            result = 1
            for item in my_list:
                result *= item
            return result
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    list_obj = List()
    result = list_obj.multiplication_list(my_list)
    lg.info(f'multiplication value of all items in a list: {result}')
