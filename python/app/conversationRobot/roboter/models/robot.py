"""Definded a Robot model"""
from roboter.view import console

DEFOLT_ROBOT_NAME = "TOYOBOT"


class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFOLT_ROBOT_NAME, user_name="", speak_color="blue"):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color
    
    def hello(self):
        """Return to the user that the robot speaks at the biggining."""
        while True:
            template = console.get_template('hello.txt',self.speak_color)
            substitute = {'robot_name':self.name}
            user_name = input(template.substitute(substitute))

            if user_name:
                self.user_name = user_name.title()
                break
    
    def _hello_decorater(func):
        """Decorator to say a greeting if you are not gretting the user."""
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func
        return wrapper
    
    def goodbye(self):
        """Return to the user that the robot finishes talking.""" 
        template = console.get_template('goodbye.txt',self.speak_color)
        substitute ={'user_name':self.user_name}
        print(template.substitute(substitute))
