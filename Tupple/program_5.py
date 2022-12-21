'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to find the repeated items of a tuple.
'''

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def count_tuples(self, my_tuple: tuple):
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
            count = my_tuple.count(7)
            return lg.info(f"num 7 is repeated {count} nos of times")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = (2, 7, 5, 6, 2, 3, 7, 6, 7)
    tuple_obj = Tuples()
    result = tuple_obj.count_tuples(my_tuple)
