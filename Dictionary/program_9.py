'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to print a dictionary in table format.
'''

from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def dict_table(self, data):
        """
        Description:
            Takes the parameter as dictionary and print a dictionary in table format.
        Parameter:
            Passed parameter as data as dict.
        Return:
            Returns nothing but print a dictionary in table format.
        """
        try:
            lg.info("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
            for key, value in data.items():
                name, age, course = value
                lg.info("{:<10} {:<10} {:<10}".format(name, age, course))
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    dict1 = {
        1: ["Samuel", 21, 'Data Structures'],
        2: ["Richie", 20, 'Machine Learning'],
        3: ["Lauren", 21, 'OOPS with java'],
    }
    dict_obj = Dictionary()
    dict_obj.dict_table(dict1)
