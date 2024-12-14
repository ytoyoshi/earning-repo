"""Utils to display to be returned to the user on the console."""
import os
import string

import termcolor

import configparser

config = configparser.ConfigParser()

def get_template_path():
    """Return the pass of template's directory"""
    tempalte_dir_path = None
    
    try:
        import roboter.settings as SETTINGS
        tempalte_dir_path = SETTINGS.TEMPLATE_PATH
    except: ImportError

    if not tempalte_dir_path:
        basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tempalte_dir_path = os.path.join(basedir, "template")
    
    return tempalte_dir_path

class NoTemplateError(Exception):
    """Not exists tempalete error"""

def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path

    Raises:
        NoTemplateError: If the file does not exists.
    """
    template_dir_path = get_template_path()
    template_file_path = os.path.join(template_dir_path,temp_file)
    if not os.path.exists(template_file_path):
        raise NoTemplateError
    return template_file_path

def get_template(template_file_name,color=None):
    """Return the pass of the template

    Args:
      template_file_name(str) : The template file name
      color(str) : Color formatting for outoput in terminal
       See in more details : https://pypi.python.org/pypi/termcolor
    
    Return:
      string.template : Return templates with characters in template
    """
    template = find_template(template_file_name)
    with open (template,'r',encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents = contents , splitter = '#'*60, sep = os.linesep)
        contents = termcolor.colored(contents,color)
        return string.Template(contents)

