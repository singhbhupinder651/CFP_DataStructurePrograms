'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to lowercase first n characters in a string.
'''
from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def lowercase_n_string(self, my_string: str, num):
        """
        Description:
            Takes the parameter as my_string and return lowercase first n characters in a string.
        Parameter:
            Passed parameter my_string as string.
        Return:
            Returns lowercase first n characters in a string.
        """
        try:
            return lg.info(
                f"lower case of n string :{my_string[:num].lower()+ my_string[num:]} ")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    my_string = 'Bhupinder'
    string_obj = String()
    result = string_obj.lowercase_n_string(my_string, num)
