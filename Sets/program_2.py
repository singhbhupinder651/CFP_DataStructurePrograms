'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to iteration over sets.
'''

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class Set:
    """
    Set Manipulations
    """

    def iterate_set(self, size):
        """
        Description:
            Takes the parameter as size of set and print set values after iteration process.
        Parameter:
            Passed parameter size as integer. 
        Return:
            Returns nothing but prints the set values after iteration process.
        """
        try:
            set_values = set()
            for element in range(size):
                set_values.add(int(input("Enter the elements: ")))
            lg.info(set_values)

            for values in set_values:
                lg.info(f'after iterating from loop: {values}')
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    size = int(input("Enter the size of set: "))
    set_obj = Set()
    set_obj.iterate_set(size)
