'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python function that takes a list of words and returns the length of the longest one.
'''

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def longest_word(self, words):
        """
        Description:
            Takes the parameter as words and returns the length of the longest one.
        Parameter:
            Passed parameter words as string. 
        Return:
            Returns printing the length of the longest one.
        """
        try:
            word_list = []
            for element in words:
                word_list.append(element)
                reversed_list = sorted(word_list, key=len, reverse=True)
            return lg.info(f"length of longest string :{len(reversed_list[0])}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    word = ['Bhupinder', 'Singh', 'Ghai', 'Machine', 'learning', 'exposure']
    string_obj = String()
    result = string_obj.longest_word(word)
