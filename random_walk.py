import math
import random
from scipy.stats import levy

from rules import Rules


class RandomWalk(object):

    @staticmethod
    def random_start_pos() -> dict:
        """ generates a random position inside the map """
        x = random.randint(0, Rules.map_size - 1)
        y = random.randint(0, Rules.map_size - 1)
        return {
            "x": x,
            "y": y
        }

    @staticmethod
    def levy_flight(old_pos: dict) -> dict:
        """ generate a new position by doing a levy flight from the old position """
        angle = random.random() * 2 * math.pi
        distance = pow(random.random(), -1 / Rules.levy_alpha)
        new_x = (old_pos["x"] + round(distance * math.sin(angle))) % Rules.map_size
        new_y = (old_pos["y"] + round(distance * math.cos(angle))) % Rules.map_size
        return {
            "x": new_x,
            "y": new_y
        }
