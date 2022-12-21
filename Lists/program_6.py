'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to remove duplicates from a list.
'''


from data_log import get_logger

lg = get_logger(name="(program_6)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def remove_duplicates(self, my_list: list):
        """
        Description:
            Takes the parameter as list and print after removing duplicates from a list.
        Parameter:
            Passed parameter my_list as list.
        Return:
            Returns print after removing duplicates from a list.
        """
        try:
            lg.info(f"original list: {my_list}")
            unique_list = []
            for element in my_list:
                if element not in unique_list:
                    unique_list.append(element)
            return lg.info(f'final list after removing dupliactes: {unique_list}')

            

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    list_obj = List()
    list_obj.remove_duplicates(my_list)
