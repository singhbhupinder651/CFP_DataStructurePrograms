'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to get the difference between the two lists.
'''


from data_log import get_logger
lg = get_logger(name="(program_12)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def difference_two_lists(self, list_1, list_2):
        """
        Description:
            Takes the parameter as list_1 and list_2 and return the difference between the two lists.
        Parameter:
            Passed parameter list_1 and list_2 as list.
        Return:
            returns the print of difference between the two lists.
        """
        try:
            diff_list1_list2 = list(set(list_1) - set(list_2))
            diff_list2_list1 = list(set(list_2) - set(list_1))
            total_diff = diff_list1_list2 + diff_list2_list1
            return lg.info(f'The total difference between the two lists are: {total_diff}')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6]
    list_2 = [1, 3, 5, 7, 9]
    list_obj = List()
    list_obj.difference_two_lists(list_1, list_2)
