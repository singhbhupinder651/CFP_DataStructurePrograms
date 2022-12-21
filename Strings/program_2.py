'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to count the number of characters (character frequency) in a string.
            Sample String : google.com
            Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def char_frequency(self, my_string):
        """
        Description:
            Takes the parameter as my_string and return printing count the number of characters (character frequency) in a string.
        Parameter:
            Passed parameter my_string as string. 
        Return:
            Returns printing count the number of characters (character frequency) in a string.
        """
        try:
            my_dict = {}
            for element in my_string:
                keys = my_dict.keys()
                if element in keys:
                    my_dict[element] += 1
                else:
                    my_dict[element] = 1
            return lg.info(f"count of string:{my_dict}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_string = "BhupinderSingh"
    string_obj = String()
    result = string_obj.char_frequency(my_string)
