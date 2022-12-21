'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to count the values associated with key in a dictionary.
            Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
                            False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
            Expected result: Count of how many dictionaries have success as True
'''

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def count_dict(self, data):
        """
        Description:
            Takes the parameter as dictionary and print a count of dictionaries which has success as True.
        Parameter:
            Passed parameter as data as dict.
        Return:
            Returns nothing but print a count of dictionaries which has success as True.
        """
        try:
            count = sum(d['success'] for d in data)
            lg.info(f'{count} no of dictionaries have success as True')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":

    data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
            False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    dict_obj = Dictionary()
    dict_obj.count_dict(data)
