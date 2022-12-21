'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to check whether an element exists within a tuple.
'''

from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def tuple_exists(self, my_tuple: tuple):
        """
        Description:
            Takes the parameter as my_tuple and prints after checking an element exists within a tuple.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns nothing but prints after checking an element exists within a tuple
        """
        try:
            lg.info(f'{"Bhupinder" in my_tuple} Bhupinder value is avaialable in tuple')
            lg.info(f'{2+5j in my_tuple} 2+5j value is avaialable in tuple')
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = (1, 2.0, 'Bhupinder', True, 2+5j)
    tuple_obj = Tuples()
    result = tuple_obj.tuple_exists(my_tuple)
