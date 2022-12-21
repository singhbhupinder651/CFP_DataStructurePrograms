'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python script to generate and print a dictionary that contains a
            number (between 1 and n) in the form (x, x*x).
            Sample Dictionary ( n = 5) :
            Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def power_of_two(self, number):
        """
        Description:
            Takes the parameter as number and looping over the dictionaries to generate power of two.
        Parameter:
            Passed parameter number as integer.
        Return:
            Returns nothing but prints the power of two of input numbers.
        """
        try:
            my_dict = {num: num*num for num in range(1, number+1)}
            lg.info(f"Dictionary:{my_dict}")
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    number = int(input("Enter the number: "))
    dict_obj = Dictionary()
    dict_obj.power_of_two(number)
