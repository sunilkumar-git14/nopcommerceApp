import logging


class LogGen:
    # static method is called by using class name
    @staticmethod
    def loggen():
        logging.basicConfig(filename="Logs/automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%y %I:%M:%S %p",
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
