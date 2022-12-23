'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to reverse a tuple.
'''

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def reverse_tuple(self, my_tuple: tuple):
        """
        Description:
            Takes the parameter as my_tuple and return print with reverse order.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns nothing but prints the reverse order of tuple data.
        """
        try:
            lg.info(f"original tuple: {my_tuple}")
            tuple_data1 = my_tuple[::-1]
            return lg.info(f"reverse order: {tuple_data1}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = (1, 2.0, 'Bhupinder', True, 2+5j)
    tuple_obj = Tuples()
    result = tuple_obj.reverse_tuple(my_tuple)
