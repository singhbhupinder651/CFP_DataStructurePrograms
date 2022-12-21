'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to remove an item from a set if it is present in the set.
'''

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def remove_item(self, size):
        """
        Description:
            Takes the parameter as size of set and print set values after removing set item if it is present in the set.
        Parameter:
            Passed parameter size as integer. 
        Return:
            Returns nothing but prints the set values after removing set item if it is present in the set.
        """

        try:
            set_values = set()
            for element in range(size):
                set_values.add(
                    int(input("Enter the elements to add to set: ")))

            lg.info(f"before removing set item: {set_values}")
            removing_num = int(
                input("Enter the element be removed from set: "))

            if removing_num in set_values:
                set_values.remove(removing_num)
            lg.info(f"after removing set item: {set_values}")  # else

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    size = int(input("Enter the size of set: "))
    set_obj = Set()
    set_obj.remove_item(size)
