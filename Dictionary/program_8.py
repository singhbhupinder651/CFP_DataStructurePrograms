'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to create a dictionary from a string.
            Note: Track the count of the letters from the string.
            Sample string : 'w3resource'
            Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

from data_log import get_logger

lg = get_logger(name="(program_8)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def create_dict(self, data):
        """
        Description:
            Takes the parameter as string and print a dictionary from a string.
        Parameter:
            Passed parameter data as string.
        Return:
            Returns nothing but prints a dictionary from a string.
        """
        try:
            my_dict = {}
            for letter in data:
                my_dict[letter] = my_dict.get(letter, 0)+1
            lg.info(f'unique value in dictionary: {my_dict}')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    data = input("Enter the value")
    dict_obj = Dictionary()
    dict_obj.create_dict(data)
