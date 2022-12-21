'''
    @Author: Bhupinder Singh
    @Date: 18-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to print all unique values in a dictionary.
            Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
            Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

from data_log import get_logger

lg = get_logger(name="(program_7)", file_name="data_log.log")


class Dictionary:
    """
    Dictionary Manipulations
    """

    def unique_values(self, data):
        """
        Description:
            Takes the parameter as list of dictionary and print all unique values in a dictionary.
        Parameter:
            Passed parameter data as list of dictionary.
        Return:
            Returns nothing but prints the all unique values in a dictionary.
        """
        try:
            lg.info(f'Original list: {data}')
            unique_data = set(
                value for dictionary in data for value in dictionary.values())
            lg.info(f'unique value in dictionary: {unique_data}')
        except Exception as e:
            lg.error(e)


if __name__ == "__main__":
    data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
        "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    dict_obj = Dictionary()
    dict_obj.unique_values(data)
