'''
    @Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a python program to check whether two lists are circularly identical.
'''


from data_log import get_logger
lg = get_logger(name="(program_14)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def __init__(self, my_dict):
        self.list_1 = my_dict.get('list_1')
        self.list_2 = my_dict.get('list_2')
        self.list_3 = my_dict.get('list_3')

    def circularly_identical(self):
        """
        Description:
            Takes the parameter as list_1, list_2 and list_3 and check whether two lists are circularly identical.
        Parameter:
            Passed parameter list_1, list_2 and list_3 as list.
        Return:
            returns nothing but prints the whether two lists are circularly identical or not.
        """
        try:
            lg.info('Compare list1 and list2: ')
            lg.info(' '.join(map(str, self.list_2))
                    in ' '.join(map(str, self.list_1 * 2)))
            lg.info('Compare list1 and list3: ')
            lg.info(' '.join(map(str, self.list_3))
                    in ' '.join(map(str, self.list_1 * 2)))

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    list_1 = [10, 10, 0, 0, 10]
    list_2 = [10, 10, 10, 0, 0]
    list_3 = [1, 10, 0, 0, 10]
    my_dict = {'list_1': list_1, 'list_2': list_2, 'list_3': list_3}
    list_obj = List(my_dict)
    list_obj.circularly_identical()
