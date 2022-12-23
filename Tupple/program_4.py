'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to create the colon of a tuple.
'''
from copy import deepcopy
from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def create_tuples(self, my_tuple):
        """
        Description:
            Takes the parameter as my_tuple and return creating the colon of a tuple.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns with creating the colon of a tuple.
        """
        try:
            lg.info(f'original tuples: {my_tuple}')
            # if we use shallow copy my_tuple value will be also changed
            # but if we use deep copy my_tuple value will be not be affected
            tuple_colon = deepcopy(my_tuple)
            tuple_colon[2].append(50)
            return lg.info(f"tuple_colon: {tuple_colon} and my_tuple: {my_tuple}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = ("HELLO", 5, [], True)
    tuple_obj = Tuples()
    result = tuple_obj.create_tuples(my_tuple)
