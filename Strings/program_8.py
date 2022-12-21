'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to get the last part of a string before a specified character.
            
'''

from data_log import get_logger

lg = get_logger(name="(program_8)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def last_part_special_char(self, my_word: str):
        """
        Description:
            Takes the parameter as my_string and return printing the last part of a string before a specified character.
        Parameter:
            Passed parameter my_word as string.
        Return:
            Returns printing the last part of a string before a specified character.
        """
        try:
            lg.info(
                f"getting part of string before '/' :{my_word.rsplit('/', 1)[0]}")
            lg.info(
                f"getting part of string before '-' :{my_word.rsplit('-', 1)[0]}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_word = 'https://www.w3resource.com/python-exercises'
    string_obj = String()
    result = string_obj.last_part_special_char(my_word)
