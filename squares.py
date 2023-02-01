"""A module creating the Square class"""


class Square():

    """A class to define a single square in the game, including location and status"""

    def __init__(self, location):
        """Init method setting the location, status (empty, X or O), and to_print attributes"""
        self.location = location
        self.status = "empty"
        self.to_print = ""

    def change_status(self, value):
        """updates the status of a given square"""
        self.status = value
