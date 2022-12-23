'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to find maximum and the minimum value in a set.
'''

from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def max_min_set(self, my_list: set):
        """
        Description:
            Takes the parameter as set and print maximum and the minimum value in a set.
        Parameter:
            Passed parameter my_set as set. 
        Return:
            Returns the print of maximum and minimum value in set.
        """

        try:
            for i in range(len(my_list)):
                for j in range(i, len(my_list)):
                    if my_list[j] < my_list[i]:
                        temp = my_list[i]
                        my_list[i] = my_list[j]
                        my_list[j] = temp
            return my_list

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [1, 9, 5, 8, 2, 4]
    set_obj = Set()
    my_list = set_obj.max_min_set(my_list)
    my_set = set(my_list)
    
    lg.info(f'set details {my_set}')
    lg.info(f'maximum value: {my_list[-1]}')
    lg.info(f'minimum value: {my_list[0]}')
