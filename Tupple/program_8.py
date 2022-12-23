'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to remove an item from a tuple.
'''

from data_log import get_logger

lg = get_logger(name="(program_8)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def remove_item_tuple(self, my_tuple: tuple):
        """
        Description:
            Takes the parameter as my_tuple and return list to a tuple.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns list to a tuple.
        """
        try:
            # tuples are immutable, so you can not remove elements
            lg.info(f"original tuple: {my_tuple}")
            my_list = list(my_tuple)
            my_list.remove(2.0)
            final_tuple = tuple(my_list)
            return lg.info(f'after removing an item: {final_tuple}')
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = (1, 2.0, 'Bhupinder', True, 2+5j)
    tuple_obj = Tuples()
    result = tuple_obj.remove_item_tuple(my_tuple)
