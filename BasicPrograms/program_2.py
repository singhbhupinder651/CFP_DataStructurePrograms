'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 18-12-2022
    @Title: Write a Python program which accepts a sequence of comma-separated numbers from user
            and generate a list and a tuple with those numbers.
            Sample data : 3, 5, 7, 23
            Output :
            List : ['3', ' 5', ' 7', ' 23']
            Tuple : ('3', ' 5', ' 7', ' 23')
'''

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


def generate_list_tuple(data):
    """
        Description:
            Takes the parameter as data of comma separated string or integer return with list and tuple.
        Parameter:
            Passed parameter data as comma separated string or integer. 
        Return:
            Returns the list and tuple data.
        """
    try:
        my_list = data.split(",")
        my_tuple = tuple(my_list)
        return my_list, my_tuple
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    sample_data = input('Enter the value: ')
    list_data, tuple_data = generate_list_tuple(sample_data)
    lg.info(f'sequence of list data: {list_data}')
    lg.info(f'sequence of tuple data: {tuple_data}')
