import logging


class utilHelper:
    def __init__(self):
        # Set up logger
        logging.basicConfig(format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s',level=logging.DEBUG)
        self.logger = logging.getLogger()

    def getLogger(self):
        return self.logger

    def setUpDictionary(self, file):
        with open("file.txt", "r") as file:
            for line in file:
                print line
