'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to get a string from a given string where all occurrences of its
            first char have been changed to '$', except the first char itself.
            Sample String : 'restart'
            Expected Result : 'resta$t'
'''

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def change_char(self, my_string):
        """
        Description:
            Function that return printing char to $ symobol.
        Parameter:
            Passed parameter my_string as string. 
        Return:
            Returns printing char to $ symobol.
        """
        try:
            char = my_string[0]
            my_string = my_string.replace(char, '$')
            # slicing from 1st index excluding r from 0 index
            my_string = char + my_string[1:]
            return lg.info(f"changing second occurrances of 'r' :{my_string}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_string = "restart"
    string_obj = String()
    result = string_obj.change_char(my_string)
