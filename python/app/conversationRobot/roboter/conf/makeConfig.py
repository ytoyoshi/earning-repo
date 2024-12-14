import configparser

config = configparser.ConfigParser()
config['FILE_PATH'] ={
    'TEMPLATE_PATH': 'roboter/tmp/template',
    'CSV_PATH': 'none'
}

with open('roboter/config.ini','w') as config_file:
    config.write(config_file)