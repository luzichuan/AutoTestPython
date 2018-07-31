import sys
from appium import webdriver
from util.Config import Config

class BaseSetup:
    
    desiredCap = None
    androidDriver = None

    def getDriver(self,phoneName):

        global desireCap
        global androidDriver

        configReader = Config()
        desireCap = configReader.getDesiredCap(phoneName)
        androidDriver = webdriver.Remote(desireCap['url'],desireCap)
        return androidDriver

if __name__ == '__main__':
    test = BaseSetup()
    print(test.getDriver('MX6'))
