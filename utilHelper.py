import logging


class utilHelper:
    def __init__(self):
        # Set up logger
        logging.basicConfig(format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s',level=logging.DEBUG)
        self.logger = logging.getLogger()

    def getLogger(self):
        return self.logger

    def getUpDictionaryList(self, filePath):
        dictionaryList = []
        try:
            with open(filePath) as fp:
                line = fp.readline()
                while line:
                    line = line.strip('\n')
                    dictionaryList.append(line)
                    line = fp.readline()

        except Exception, e:
            self.logger.error(str(e))

        return dictionaryList
