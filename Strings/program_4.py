'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to add 'ing' at the end of a given string (length should be at
            least 3). If the given string already ends with 'ing' then add 'ly' instead. 
            If the string length of the given string is less than 3, leave it unchanged.
            Sample String : 'abc'
            Expected Result : 'abcing'
            Sample String : 'string'
            Expected Result : 'stringly'
'''

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def add_string(self, my_string):
        """
        Description:
            Takes the parameter as my_string and return with adding string to it.
        Parameter:
            Passed parameter my_string as string. 
        Return:
            Returns printing with adding string to it.
        """
        try:
            if len(my_string) > 2:
                if my_string[-3:] == 'ing':
                    my_string += 'ly'
                else:
                    my_string += 'string'

            return lg.info(f"after adding 'ing' or 'ly' :{my_string}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_string_1 = input("Enter the string: ")
    string_obj = String()
    result = string_obj.add_string(my_string_1)
