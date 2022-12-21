'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to remove item(s) from set
'''

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def remove_item(self, size):
        """
        Description:
            Takes the parameter as size of set and print set values after removing set item.
        Parameter:
            Passed parameter size as integer. 
        Return:
            Returns nothing but prints the set values after removing set item.
        """
        try:
            set_values = set()
            for element in range(size):
                set_values.add(int(input("Enter the elements: ")))
            lg.info(f"before removing set item: {set_values}")
            set_values.remove(3)
            lg.info(f"after removing set item: {set_values}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    size = int(input("Enter the size of set: "))
    set_obj = Set()
    set_obj.remove_item(size)
