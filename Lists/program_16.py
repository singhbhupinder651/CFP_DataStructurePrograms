'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to split a list based on first character of word.
'''

from itertools import groupby
from operator import itemgetter
from data_log import get_logger
lg = get_logger(name="(program_16)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def split_list(self, word_list):
        """
        Description:
            Takes the parameter as word_list and prints list based on first character of word.
        Parameter:
            Passed parameter word_list as list.
        Return:
            returns nothing but prints the list based on first character of word.
        """
        try:
            for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
                lg.info(f'letter: {letter}')
                for word in words:
                    lg.info(word)
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
    list_obj = List()
    list_obj.split_list(word_list)
