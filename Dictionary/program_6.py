'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to remove a key from a dictionary.
'''

from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def remove_key(self, dict_1: dict):
        """
        Description:
            Takes the parameter as dictionary and remove a key from a dictionary.
        Parameter:
            Passed parameter dict_1 as dictionary.
        Return:
            Returns nothing but prints the popped key and final dictionary.
        """
        try:
            popped_key = dict_1.pop(1)
            lg.info(
                f"poped key is {popped_key} and final dictionary is {dict_1}")
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    dict_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    dict_obj = Dictionary()
    dict_obj.remove_key(dict_1)
