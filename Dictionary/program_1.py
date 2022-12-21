'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python script to sort (ascending and descending) a dictionary by value.
'''

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def sort_element(self, my_dict):
        """
        Description:
            Takes the parameter as dictionary and printing in ascending and descending order after sorting.
        Parameter:
            Passed parameter my_dict as dictionary. 
        Return:
            Returns nothing but prints the ascending and descending order after sorting.
        """
        try:
            lg.info(f"dictionary before sorting: {my_dict}")
            asc_sorting = sorted(my_dict.items())
            lg.info(f"dictionary sorting in ascending order: {asc_sorting}")
            desc_sorting = sorted(my_dict.items(), reverse=True)
            lg.info(f"dictionary sorting in descending order: {desc_sorting}")
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    my_dict = {4: 2, 3: "Bhupinder", 2: "Singh", 1: 1.3}
    dict_obj = Dictionary()
    dict_obj.sort_element(my_dict)
