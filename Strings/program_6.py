'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python script that takes input from the user and displays that input back in
            upper and lower cases.
'''

from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def case_changing(self, my_word):
        """
        Description:
            Takes the parameter as my_string and return with adding string to it.
        Parameter:
            Passed parameter my_word as string. 
        Return:
            Returns printing with adding string to it.
        """
        try:
            return lg.info(f"upper case :{my_word.upper()}, lower case :{my_word.lower()}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_word = input('Enter any string to convert in upper and lower case: ')
    string_obj = String()
    result = string_obj.case_changing(my_word)
