'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to slice a tuple.
'''

from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def slice_tuple(self, my_tuple: tuple):
        """
        Description:
            Takes the parameter as my_tuple and print the sliced data.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns nothing but prints the sliced data
        """
        try:
            lg.info(f"original tuple: {my_tuple}")
            tuple_data1 = my_tuple[::-1]
            lg.info(f"reverse order: {tuple_data1}")
            tuple_data2 = my_tuple[0:3]
            lg.info(f'slice from 0 to 3 :{tuple_data2}')
            tuple_data3 = my_tuple[-1]
            lg.info(f'accessing last value:{tuple_data3}')
            tuple_data4 = my_tuple[::2]
            lg.info(
                f'accessing all the values with the step of 2:{tuple_data4}')
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = (1, 2.0, 'Bhupinder', True, 2+5j)
    tuple_obj = Tuples()
    result = tuple_obj.slice_tuple(my_tuple)
