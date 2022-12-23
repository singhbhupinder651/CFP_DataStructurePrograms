'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to clone or copy a list.
'''


from data_log import get_logger
lg = get_logger(name="(program_7)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def copy_list(self, my_list: list):
        """
        Description:
            Takes the parameter as list and return print with copied list.
        Parameter:
            Passed parameter my_list as list.
        Return:
            Returns print with copied list.
        """
        try:
            lg.info(f"original list: {my_list}")
            cloned_list = []
            for element in my_list:
                cloned_list.append(element)

            return lg.info(f"Final list after copying: {cloned_list}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    list_obj = List()
    list_obj.copy_list(my_list)
