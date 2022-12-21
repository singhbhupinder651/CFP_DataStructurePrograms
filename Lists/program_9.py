'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python function that takes two lists and returns True if they have at
            least one common member.
'''


from data_log import get_logger
lg = get_logger(name="(program_9)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def common_member(self, list_1, list_2):
        """
        Description:
            Takes the parameter as list1 and list2 and return print with copied returns True if they have at
            least one common member.
        Parameter:
            Passed parameter list_! and list_2 as list.
        Return:
            returns True if they have at least one common member.
        """
        try:
            lg.info(f'list1: {list_1}')
            lg.info(f'list2: {list_2}')
            for element in list_1:
                if element in list_2:
                    return lg.info(f'True the list has one common member: {element}.')
            return lg.info(f'False the list doesn"t have atleat one common member.')

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    list_1 = [10, 20, 30, 40, 50, 60]
    list_2 = [15, 20, 35, 45]
    list_obj = List()
    list_obj.common_member(list_1, list_2)
