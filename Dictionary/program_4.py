'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to iterate over dictionaries using for loops.
'''

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def iterate_dict(self, my_dict):
        """
        Description:
            Takes the parameter as dictionary and iterate over dictionaries using for loops.
        Parameter:
            Passed parameter my_dict as dictionary.
        Return:
            Returns nothing but prints the key and values details in dictionary.
        """
        try:
            for key, value in my_dict.items():
                lg.info({"key": key, "value": value})
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    my_dict = {'red': 1, 'blue': 10, 2: 20}
    dict_obj = Dictionary()
    dict_obj.iterate_dict(my_dict)
