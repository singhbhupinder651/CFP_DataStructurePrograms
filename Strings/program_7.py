'''
    @Author: Bhupinder Singh
    @Date: 20-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 20-12-2022
    @Title: Write a Python program that accepts a comma separated sequence of words as input
            and prints the unique words in sorted form(alphanumerically).
            Sample Words: red, white, black, red, green, black
            Expected Result:
'''

from data_log import get_logger

lg = get_logger(name="(program_7)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def unique_words(self, my_word):
        """
        Description:
            Takes the parameter as my_string and return unique words in sorted form.
        Parameter:
            Passed parameter my_word as string.
        Return:
            Returns printing unique words in sorted form.
        """
        try:
            # my_list = []
            # for word in sorted(my_word):
            #     if word not in my_list:
            #         my_list.append(word)

            return lg.info(f"unique word after sorting :{sorted(set(my_word))}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_word = 'red', 'white', 'black', 'red', 'green', 'black'
    string_obj = String()
    result = string_obj.unique_words(my_word)
