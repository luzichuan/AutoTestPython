import ConfigParser
import os

'''
    To get phone start-up config
'''

class Config:

    def getDesiredcapList(self):

        configFilePath = '../res/PhoneInfo.ini'
        configReader = ConfigParser.SafeConfigParser()
        configReader.read(configFilePath)

        return configReader

    def getDesiredCap(self,phoneName):
        desiredCaps = {}
        configList = self.getDesiredcapList()

        desiredCaps['deviceName'] = configList.get(phoneName,'deviceName')
        desiredCaps['platformName'] = configList.get(phoneName,'platformName')
        desiredCaps['appPackage'] = configList.get(phoneName,'appPackage')
        desiredCaps['appActivity'] = configList.get(phoneName,'appActivity')
        desiredCaps['platformVersion'] = configList.get(phoneName,'platformVersion')
        desiredCaps['unicodeKeyboard'] = configList.get(phoneName,'unicodeKeyboard')
        desiredCaps['resetKeyboard'] = configList.get(phoneName,'resetKeyboard')
        desiredCaps['udid'] = configList.get(phoneName,'udid')
        desiredCaps['url'] = configList.get(phoneName,'url')

        return desiredCaps