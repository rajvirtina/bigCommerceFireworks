import configparser

config=configparser.RawConfigParser()
config.read(".\\Configaration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getHostName():
        hostName = config.get('common info', 'MailHost')
        return hostName

    @staticmethod
    def getMailId():
        mailId = config.get('common info', 'MailId')
        return mailId

    @staticmethod
    def getMailPassword():
        mailPassword = config.get('common info', 'MailPassword')
        return mailPassword