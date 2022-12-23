'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to find common items from two lists.
'''


from data_log import get_logger
lg = get_logger(name="(program_15)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def common_items(self, list_1, list_2):
        """
        Description:
            Takes the parameter as list_1 and list_2 and prints the common items from two lists.
        Parameter:
            Passed parameter list_1 and list_2 as list.
        Return:
            returns nothing but print the common items from two lists.
        """
        try:
            
            lg.info(
                f'common item from the pair of list are: {set(list_1) & set(list_2)}')
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    list_1 = [1, 2, 3, 134, 4, 5, 9]
    list_2 = [2, 5, 7, 134]
    list_obj = List()
    list_obj.common_items(list_1, list_2)
