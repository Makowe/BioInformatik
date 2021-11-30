from typing import Dict, List

from entity import Entity
from rules import Rules


class Statistics(object):
    def __init__(self):
        self.exposed_now: list = []
        self.infectous_now: list = []
        self.infected_now: list = []
        self.infected_cum: list = []
        self.infected_new: list = []
        self.population: list = []

    def save_data_day(self, day: int, entities: List[Entity]):
        self.population.append(len(entities))
        infections = 0
        infections_new = 0
        exposed = 0
        infectous = 0
        for entity in entities:
            if entity.days_since_exposure >= 0:
                infections += 1
                if entity.recovered == 0 and entity.days_since_exposure == 1:
                    infections_new += 1
                if entity.infectous:
                    infectous += 1
                else:
                    exposed += 1
        self.exposed_now.append(exposed)
        self.infectous_now.append(infectous)
        self.infected_now.append(infections)
        self.infected_new.append(infections_new)
        self.infected_cum.append(self.calc_cumulative(infections_new))

    def calc_cumulative(self, infections_new) -> int:
        if len(self.infected_cum) == 0:
            return infections_new
        else:
            return infections_new + self.infected_cum[-1]

    def print_last(self) -> str:
        return f"day {len(self.exposed_now)-1}: " \
               f"ex: {self.exposed_now[-1]} " \
               f"is: {self.infectous_now[-1]} " \
               f"id: {self.infected_now[-1]} " \
               f"id_n: {self.infected_new[-1]} " \
               f"id_c: {self.infected_cum[-1]} " \
               f"p: {self.population[-1]}"
