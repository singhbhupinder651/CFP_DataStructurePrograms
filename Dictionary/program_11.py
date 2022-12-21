'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to convert a list into a nested dictionary of keys.
'''

from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def create_nested_dict(self, num_list):
        """
        Description:
            Takes the parameter as list and print a list into a nested dictionary of keys.
        Parameter:
            Passed parameter as num_list as list.
        Return:
            Returns nothing but print a list into a nested dictionary of keys.
        """
        try:
            tree_dict = {}
            for key in num_list[::-1]:
                tree_dict = {key: tree_dict}
            lg.info(f'final dictionary is {tree_dict}')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    num_list = [1, 2, 3, 4]
    dict_obj = Dictionary()
    dict_obj.create_nested_dict(num_list)
