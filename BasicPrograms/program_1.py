'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 18-12-2022
    @Title: Write a Python program which accepts the user's first and last name and print them in
            reverse order with a space between them.
'''

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class Reverse:
    """
    printing the reverse order.
    """

    def __init__(self, name_dict):
        self.first_name = name_dict.get("first_name")
        self.last_name = name_dict.get("last_name")

    def reverse_name(self):
        """
        Description:
            Takes the parameter name_dict as dictionary and getting first and last name and return in reverse order.
        Parameter:
            Passed parameter name_dict as dictionary 
        Return:
            Returns the name after reversing the order with space between them.
        """
        try:
            full_name = self.first_name + " " + self.last_name
            lg.info(f"name before reversing the order {full_name}")
            return lg.info(f"name after reversing the order {full_name[::-1]}")
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    name_dict = {"first_name": first_name, "last_name": last_name}
    name_obj = Reverse(name_dict)
    name_obj.reverse_name()
