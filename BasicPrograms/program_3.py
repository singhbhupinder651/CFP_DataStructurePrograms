'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to display the first and last colors from the following list.
            color_list = ["Red","Green","White" ,"Black"]
'''

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


def color_slice(*args):
    """
        Description:
            Takes the parameter as list of color and return the first and last colors from the list.
        Parameter:
            Passed parameter *args as list of colors. 
        Return:
            Returns the first and last colors from the list.
        """
    try:
        first_color = args[0][0]
        last_color = args[0][-1]
        return first_color, last_color
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    color_list = ['Red', 'Green', 'WHite', 'Black']
    first_color, last_color = color_slice(color_list)
    lg.info(f'The first color from list: {first_color}')
    lg.info(f'The last color from list: {last_color}')
