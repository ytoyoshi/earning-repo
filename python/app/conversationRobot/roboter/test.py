import configparser

conf = configparser.ConfigParser()

conf.read('config.ini')
print(conf['FILE_PATH'])