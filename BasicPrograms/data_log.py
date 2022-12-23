import logging as lg


def get_logger(name=None, file_name=None):
    if file_name is None:
        file_name = "data_log.log"

    lg.basicConfig(filename=file_name, level=lg.DEBUG,
                   format="%(asctime)s %(name)s %(levelname)s %(message)s")

    format = lg.Formatter(
        "%(name)s - %(asctime)s - %(levelname)s - %(message)s")

    #file_handler = lg.FileHandler(file_name)
    #file_handler.setLevel(lg.DEBUG)
    #file_handler.setFormatter(format)
    # stream handler help you to print logging info in our console
    console_log = lg.StreamHandler()
    console_log.setLevel(lg.DEBUG)
    
    console_log.setFormatter(format)

    # create custom logger
    # addHandler helps to create instance of user1or2 label instead of root user
    
    #lg.getLogger("").addHandler(file_handler)
    lg.getLogger("").addHandler(console_log)
    if not name:
        name = ""
    return lg.getLogger(name)
