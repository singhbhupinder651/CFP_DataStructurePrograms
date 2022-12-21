'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to count occurrences of a substring in a string.
'''

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def count_sub_string(self, sample_text: str):
        """
        Description:
            Takes the parameter as my_string and return count occurrences of a substring in a string.
        Parameter:
            Passed parameter sample_text as string.
        Return:
            Returns count occurrences of a substring in a string.
        """
        try:
            return lg.info(
                f"text :{sample_text} and count of sub-string 'for': {sample_text.count('and')} ")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    sample_text = 'You are given a text, which contains different english letters and punctuation symbols.'
    string_obj = String()
    result = string_obj.count_sub_string(sample_text)
