'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program to display formatted text (width=50) as output.
'''
import textwrap

from numpy import safe_eval
from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def format_text(self, sample_text):
        """
        Description:
            Takes the parameter as my_string and return displaying formatted text (width=50) as output.
        Parameter:
            Passed parameter sample_text as string.
        Return:
            Returns displaying formatted text (width=50) as output.
        """
        try:
            return lg.info(
                f"displaying formated text :{textwrap.fill(sample_text, width=50)}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    sample_text = '''In the world of programming, Python is known as one of the most popular 
    and fastest-growing programming languages. It can be defined as a high-level, interpreted, 
    object-oriented scripting language, and a general-purpose language. 
    There are various programming languages in the modern IT market space, but only Python has
    become quite widespread,why so? This is a fact, and a question raised by many people around the world. '''

    string_obj = String()
    result = string_obj.format_text(sample_text)
