'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to get a list, sorted in increasing order by the last
            element in each tuple from a given list of non-empty tuples.
            Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
            Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def sort_increase_order(self, my_list: list):
        """
        Description:
            Takes the parameter as list and print sorted in increasing order by the last
            element in each tuple from a given list.
        Parameter:
            Passed parameter my_list as list.
        Return:
            Returns print sorted in increasing order by the last element in each tuple from a given list..
        """
        try:
            lg.info(f"original list: {my_list}")
            l_length = len(my_list)

            for count in range(l_length):  # Accessing to list
                for count_2 in range(l_length-1):  # Accessing to tuple
                    sec_value = my_list[count_2][1]
                    sec_value_next = my_list[count_2+1][1]
                    # sorting
                    if sec_value > sec_value_next:
                        temp = my_list[count_2]
                        my_list[count_2] = my_list[count_2+1]
                        my_list[count_2+1] = temp
            return lg.info(f"final list after sorting in ascending order: {my_list} ")

        except Exception as e:
            lg.exception(e)

    # def order(element):
    #     return (element[1])


if __name__ == "__main__":
    my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    list_obj = List()
    list_obj.sort_increase_order(my_list)
    # print("sorted list:", sorted(my_list, key=order))
