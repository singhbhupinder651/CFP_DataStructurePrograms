'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to reverse a string.
'''

from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def reverse_string(self, my_string: str):
        """
        Description:
            Takes the parameter as my_string and return reverse a string.
        Parameter:
            Passed parameter my_string as string.
        Return:
            Returns reverse a string.
        """
        try:
            return lg.info(
                f"text :{my_string} and reverse of string: {my_string[::-1]} ")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_string = 'Bhupinder'
    string_obj = String()
    result = string_obj.reverse_string(my_string)
