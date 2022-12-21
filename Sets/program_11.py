'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to use of frozensets..
'''

from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def add_element(self, my_set, value):
        """
        Description:
            Takes the parameter as size of set and print the set values.
        Parameter:
            Passed parameter size as integer. 
        Return:
            Returns the set values.
        """
        try:
            my_set.add(value)
        except:
            lg.info("You cannot add element in this set becaues it is forzen set")
        return my_set


if __name__ == "__main__":
    set_obj1 = Set()
    set_obj2 = Set()

    set_1 = set([7, 5, 3, 4, 5, 6, 1])
    lg.info(f'Before adding the element: {set_1}')
    value = (int(input("Enter value to add again in set: ")))
    set_obj1.add_element(set_1, value)
    lg.info(f'after adding elements: {set_1}')

    set_2 = frozenset(set([7, 5, 3, 4, 5, 6, 1]))
    lg.info(f'Before adding the element: {set_2}')
    value = (int(input("Enter value to add again in set: ")))
    set_obj2.add_element(set_2, value)
    lg.info(f'after adding elements: {set_2}')
