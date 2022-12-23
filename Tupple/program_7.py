'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to convert a list to a tuple.
'''

from data_log import get_logger

lg = get_logger(name="(program_7)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def list_to_tuple(self, my_list):
        """
        Description:
            Takes the parameter as my_tuple and return list to a tuple.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns list to a tuple.
        """
        try:
            my_tuple = tuple(my_list)
            return lg.info(f'type of my_tuple: {type(my_tuple)} and data: {my_tuple}')
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [1, 2.0, 'Bhupinder', True, 2+5j]
    tuple_obj = Tuples()
    result = tuple_obj.list_to_tuple(my_list)
