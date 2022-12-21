'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to unpack a tuple in several variables.
'''

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def create_tuples(self, my_tuple):
        """
        Description:
            Takes the parameter as my_tuple and return with unpacking a tuple in several variables.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns with unpacking a tuple in several variables.
        """
        try:
            num_1, num_2, num_3 = my_tuple
            return lg.info(f"sum of unpacked value: {num_1+num_2+num_3}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = 1, 2, 3
    tuple_obj = Tuples()
    result = tuple_obj.create_tuples(my_tuple)
