'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to print a specified list after removing the 0th, 4th and
            5th elements.
            Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
            Expected Output : ['Green', 'White', 'Black']
'''


from data_log import get_logger
lg = get_logger(name="(program_10)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def remove_specified_elements(self, my_list: list):
        """
        Description:
            Takes the parameter as my_list and return the specified list after removing the 0th, 4th and
            5th elements.
        Parameter:
            Passed parameter my_list as list.
        Return:
            returns the specified list after removing the 0th, 4th and 5th elements.
        """
        try:
            lg.info(f'original list: {my_list}')
            index_list = [0, 4, 5]
            new_list = []
            for element in my_list:
                if my_list.index(element) not in index_list:
                    new_list.append(element)

            return lg.info(f'list after removing 0, 4th and 5th index: {new_list}')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    list_obj = List()
    list_obj.remove_specified_elements(my_list)
