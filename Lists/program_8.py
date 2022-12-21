'''
    @@Author: Bhupinder Singh
    @Date: 19-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 19-12-2022
    @Title: Write a Python program to find the list of words that are longer than n from a
            given list of words.
'''


from data_log import get_logger
lg = get_logger(name="(program_8)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def __init__(self, my_dict):
        self.sentence = my_dict.get("sentence")
        self.num = my_dict.get("num")

    def longer_words(self):
        """
        Description:
            Takes the parameter as list and return print with copied list.
        Parameter:
            Passed parameter my_list as list.
        Return:
            Returns print with copied list.
        """
        try:
            result_list = []
            words = sentence.split(' ')
            for element in words:
                if len(element) > self.num:
                    result_list.append(element)
            return lg.info(f"the words greater than given numbers are: {result_list}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    sentence = 'KodeKloud Will Help You To Build A Successful DevOps Career'
    num = int(input("Enter the n number: "))
    my_dict = {"sentence": sentence, "num": num}
    list_obj = List(my_dict)
    list_obj.longer_words()
