'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python script to concatenate following dictionaries to create a new one.
            Sample Dictionary :
            dic1={1:10, 2:20}
            dic2={3:30, 4:40}
            dic3={5:50,6:60}
            Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def __init__(self, my_dict: dict):
        self.dict_1 = my_dict.get('dict1')
        self.dict_2 = my_dict.get('dict2')
        self.dict_3 = my_dict.get('dict3')

    def add_dict(self):
        """
        Description:
            Takes the parameter as dictionary and adding new key and value to dictionary.
        Parameter:
            Passed parameter my_dict as dictionary. 
        Return:
            Returns nothing but prints the updating key and value to existing dictionary.
        """
        try:
            main_dict = {}
            for dictionary in (self.dict_1, self.dict_2, self.dict_3):
                main_dict.update(dictionary)
                lg.info(f"after concatenating dictionary: {main_dict}")
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    my_dict = {'dict1': {1: 10, 2: 20}, 'dict2': {
        3: 30, 4: 40},  'dict3': {5: 50, 6: 60}}
    dict_obj = Dictionary(my_dict)
    dict_obj.add_dict()
