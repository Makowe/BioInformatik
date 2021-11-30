import random
from typing import List

from random_walk import RandomWalk
from rules import Rules


class Entity(object):
    def __init__(self, map: 'Map'):
        self.pos = RandomWalk.random_start_pos()
        self.infectous: bool = False
        """ person can infect others"""

        # self.sympthomatic: bool = False
        self.vaccinated: bool = False
        self.recovered: bool = False
        self.dead: bool = False

        self.immunity: float = 0
        self.days_since_exposure: int = -1
        """ how many days have passed since exposure.
        -1: person is not infected
         0: the person has been infected today
        """
        self.map = map

    def vaccinate(self):
        self.vaccinated = True
        self.increase_immunity(Rules.vac_immunity)

    def recover(self):
        self.recovered = True
        self.increase_immunity(Rules.recover_immunity)

    def kill(self):
        self.dead = True

    def end_infection(self):
        self.days_since_exposure = -1
        self.infectous = 0
        if random.random() < Rules.mortality:
            self.kill()
        else:
            self.recover()

    def walk(self):
        self.pos = RandomWalk.levy_flight(self.pos)

    def cough(self):
        """ if a person is infectous, expose all near entities with a specific probability """
        if self.infectous:
            near_entities: List[dict] = self.map.get_near_entities(self, Rules.max_distance_spread)
            for entity_dict in near_entities:
                entity = entity_dict["entity"]
                distance = entity_dict["distance"]
                probability = 1/(distance + 1) * Rules.spread_probability
                if self.vaccinated:
                    probability *= Rules.vac_reduce_spread
                entity.expose(probability)
        else:
            return

    def expose(self, probability):
        """ expose a person to the virus. The immunity of the person will act as the probabilty of being infected.
        A person that is infected at the moment, can't be infected again.
        """
        if self.days_since_exposure >= 0 or self.immunity >= 0.99:
            # person is already infected or highly immune
            return
        if random.random() < (1 - self.immunity) * probability:
            # infect person
            self.days_since_exposure = 0

    def increase_immunity(self, percentage):
        """ the immunity is increased by the specified percentage
        the percentage is not simply added to the existing immunity but multiplied
        example: percentage = 0.6
        old immunity = 0.0 -> new immunity = 0.6
        old immunity = 0.5 -> new immunity = 0.8
        old immunity = 1.0 -> new immunity = 1 """
        self.immunity += (1 - self.immunity) * percentage
