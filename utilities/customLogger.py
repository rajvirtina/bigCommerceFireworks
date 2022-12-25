import logging


class LogGen:
    @staticmethod
    def logger():
        logger = logging.getLogger()
        filehandler = logging.FileHandler(filename=".\\Logs\\automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
