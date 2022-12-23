'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to check whether a specified value is contained in a group of values.
            Test Data :
            3 -> [1, 5, 8, 3] : True
            -1 -> [1, 5, 8, 3] : False
'''

from data_log import get_logger

lg = get_logger(name="(program_7)", file_name="data_log.log")


def check_specific_value(test_data, data):
    """
        Description:
            Takes the parameter as list of integer number and printing the existiance whether a specified value is contained in a group of values.
        Parameter:
            Passed parameter is list of integer numbers. 
        Return:
            Returns nothing but prints existiance whether a specified value is contained in a group of values.
        """

    try:
        if data in test_data:
            lg.info("the number you're searching is available")
        else:
            lg.info("the number you're searching is not available")
    except Exception as e:
        lg.error(e)


if __name__ == "__main__":
    test_data = [1, 5, 8, 3]
    data = int(input("Enter the number to find its existance in list: "))
    check_specific_value(test_data, data)
