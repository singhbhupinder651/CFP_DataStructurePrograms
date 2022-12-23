'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to create a set.
'''

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def create_set(self, size):
        """
        Description:
            Takes the parameter as size of set and print set values.
        Parameter:
            Passed parameter size as integer. 
        Return:
            Returns nothing but prints the set values.
        """
        try:
            set_values = set()
            for element in range(size):
                set_values.add(int(input("Enter the elements: ")))
            lg.info(set_values)
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    size = int(input("Enter the size of set: "))
    set_obj = Set()
    set_obj.create_set(size)
