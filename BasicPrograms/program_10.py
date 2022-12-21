'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to print out a set containing all the colors from color_list_1 which
            are not present in color_list_2.
            Test Data :
            color_list_1 = set(["White", "Black", "Red"])
            color_list_2 = set(["Red", "Green"])
'''

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


def color_difference(color_list_1: set, color_list_2: set):
    """
        Description:
            Takes the parameter as list of colors and returns with printing out a set containing all the colors from color_list_1 which
            are not present in color_list_2
        Parameter:
            Passed parameter list of color_list as list. 
        Return:
            Returns nothing the set containing all the colors from color_list_1 which are not present in color_list_2
        """

    try:
        return color_list_1.difference(color_list_2)
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    lg.info(color_difference(color_list_1, color_list_2))
