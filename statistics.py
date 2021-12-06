from typing import Dict, List
from matplotlib import pyplot as plt

from entity import Entity
from rules import Rules


class Statistics(object):
    def __init__(self):
        self.population: list = []

        # data at the moment
        self.exposed: list = []
        self.infectous: list = []
        self.infected: list = []
        self.recovered: list = []
        self.immune: list = []

        # cumulative data
        self.infected_cum: list = []
        self.deaths_cum: list = []

        # new data
        self.infected_new: list = []

    def save_data_day(self, day: int, entities: List[Entity]):
        population = len(entities)
        exposed = 0
        infectous = 0
        infected = 0
        recovered = 0
        immune = 0

        infected_new = 0
        deaths_cum = Rules.number_entities - len(entities)

        for entity in entities:
            if entity.immune: immune += 1
            if entity.recovered: recovered += 1
            if entity.infectous: infectous += 1

            if entity.days_since_exposure >= 0:
                infected += 1
                if not entity.infectous: exposed += 1
                if entity.recovered == 0 and entity.days_since_exposure == 1:
                    infected_new += 1
        infected_cum = self.calc_cumulative(self.infected_cum, infected_new)

        self.population.append(population)

        self.exposed.append(exposed)
        self.infectous.append(infectous)
        self.infected.append(infected)
        self.recovered.append(recovered)
        self.immune.append(immune)

        self.infected_cum.append(infected_cum)
        self.deaths_cum.append(deaths_cum)

        self.infected_new.append(infected_new)

    def calc_cumulative(self, time_series, new) -> int:
        if len(time_series) == 0:
            return new
        else:
            return new + time_series[-1]

    def print_last(self) -> str:
        return f"day {len(self.exposed) - 1}: " \
               f"ex: {self.exposed[-1]} " \
               f"is: {self.infectous[-1]} " \
               f"id: {self.infected[-1]} " \
               f"id_n: {self.infected_new[-1]} " \
               f"id_c: {self.infected_cum[-1]} " \
               f"p: {self.population[-1]}"

    def plot(self):
        plt.plot(self.infected)
        plt.plot(self.recovered)
        plt.plot(self.deaths_cum)
        plt.show()

