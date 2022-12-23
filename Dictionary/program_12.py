'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to check multiple keys exists in a dictionary.
'''

from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def check_multiple_dict(self, my_dict):
        """
        Description:
            Takes the parameter as dictionary and print to check if multiple keys exists in a dictionary or not.
        Parameter:
            Passed parameter as my_dict as dictionary.
        Return:
            Returns nothing but print if multiple keys exists in a dictionary or not.
        """
        try:
            if len(my_dict) > 1:
                lg.info(f'multiple keys are exists in a dictionary')
            else:
                lg.info(f'multiple keys are not exists in a dictionary')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    my_dict = {'name': 'Alex', 'class': 'V', 'roll_id': '2'}
    dict_obj = Dictionary()
    dict_obj.check_multiple_dict(my_dict)
