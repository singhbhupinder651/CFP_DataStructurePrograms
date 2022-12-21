'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to add member(s) in a set.
'''

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def add_member(self, size):
        """
        Description:
            Takes the parameter as size of set and print set values after adding new member.
        Parameter:
            Passed parameter size as integer. 
        Return:
            Returns nothing but prints the set values after adding new member.
        """
        try:
            set_values = set()
            for element in range(size):
                set_values.add(int(input("Enter the elements: ")))
            lg.info(f"before updating set values: {set_values}")
            set_values.update([75, 89])
            lg.info(f"after updating set values: {set_values}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    size = int(input("Enter the size of set: "))
    set_obj = Set()
    set_obj.add_member(size)
