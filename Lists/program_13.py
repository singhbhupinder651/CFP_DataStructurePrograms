'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to append a list to the second list.
'''


from data_log import get_logger
lg = get_logger(name="(program_13)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def append_list(self, list_1, list_2):
        """
        Description:
            Takes the parameter as list_1 and list_2 and return a list appending to the second list.
        Parameter:
            Passed parameter list_1 and list_2 as list.
        Return:
            returns a list appending to the second list.
        """
        try:
            for element in list_2:
                list_1.append(element)
            return lg.info(f'After appending the list: {list_1}')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    list_1 = [1, 3, 5, 7, 9]
    list_2 = ['Bhupinder', 'Singh', 'Ghai']
    list_obj = List()
    list_obj.append_list(list_1, list_2)
