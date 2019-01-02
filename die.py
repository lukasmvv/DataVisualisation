from random import randint

class Die():
    """Class for a single die"""

    def __init__(self, num_sides=6):
        """Initialise with default 6 sides"""

        self.num_sides = num_sides

    def roll(self):
        """Rolling one die"""

        return randint(1, self.num_sides)