'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python script to add a key to a dictionary.
            Sample Dictionary : {0: 10, 1: 20}
            Expected Result : {0: 10, 1: 20, 2: 30}
'''

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def add_dict(self, my_dict):
        """
        Description:
            Takes the parameter as dictionary and print new key and value to dictionary.
        Parameter:
            Passed parameter my_dict as dictionary. 
        Return:
            Returns nothing but prints the new key and value to dictionary.
        """
        try:
            lg.info(f"dictionary before adding new key: {my_dict}")
            my_dict.update({4: '6i+7j'})
            lg.info(f"dictionary after adding new key: {my_dict}")
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    dict_1 = {1: 2, 2: "Bhupinder", 3: "Singh"}
    dict_obj = Dictionary()
    dict_obj.add_dict(dict_1)
