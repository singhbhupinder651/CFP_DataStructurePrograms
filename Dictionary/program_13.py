'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to count number of items in a dictionary value that is a list.
'''

from data_log import get_logger

lg = get_logger(name="(program_13)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def count_items(self, my_dict: dict):
        """
        Description:
            Takes the parameter as dictionary and print the number of items in a dictionary value that is a list.
        Parameter:
            Passed parameter as my_dict as dictionary.
        Return:
            Returns nothing but print the number of items in a dictionary value that is a list.
        """
        try:
            count = 0
            for index in my_dict:
                if isinstance(my_dict[index], list):
                    count += len(my_dict[index])
            lg.info(
                f'{count} number of items in a dictionary value that is a list')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    my_dict = {
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B': 34,
        'C': 12,
        'D': [7, 8, 9, 6, 4]
    }
    dict_obj = Dictionary()
    dict_obj.count_items(my_dict)
