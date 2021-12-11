from typing import Dict, List
from matplotlib import pyplot as plt

from entity import Entity
from rules import Rules


class Statistics(object):
    def __init__(self):
        # data at the moment
        self.exposed: list = []
        self.infectous: list = []

        self.susceptible: list = []
        self.infected: list = []
        self.recovered: list = []

        self.infected_follow: list = []
        self.infected_break: list = []

        # cumulative data
        self.infected_cum: list = []

    def save_data_day(self, day: int, entities: List[Entity]):
        susceptible = 0
        exposed = 0
        infectous = 0
        infected = 0
        infected_follow = 0
        infected_break = 0
        recovered = 0

        for entity in entities:
            if entity.susceptible: susceptible += 1
            if entity.recovered: recovered += 1
            if entity.infectous: infectous += 1

            if entity.days_since_exposure >= 0:
                infected += 1
                if entity.follows_rules:
                    infected_follow += 1
                else:
                    infected_break += 1
                if not entity.infectous: exposed += 1

        self.exposed.append(exposed)
        self.infectous.append(infectous)
        self.infected.append(infected)
        self.infected_follow.append(infected_follow)
        self.infected_break.append(infected_break)
        self.recovered.append(recovered)
        self.infected_cum.append(recovered+infected)
        self.susceptible.append(susceptible)

    def get_headline_str(self):
        """ used for csv export """
        return "day;exposed;infectous;infected;recovered;susceptible;infected_cum,infected_follow,infected_break\n"

    def get_single_day_str(self, day):
        """ used for csv export """
        return f"{day};" \
               f"{self.exposed[day]};" \
               f"{self.infectous[day]};" \
               f"{self.infected[day]};" \
               f"{self.recovered[day]};" \
               f"{self.susceptible[day]};" \
               f"{self.infected_cum[day]};" \
               f"{self.infected_follow[day]};" \
               f"{self.infected_break[day]}\n"

    def print_last(self) -> str:
        return f"day {len(self.exposed) - 1}: " \
               f"exposed: {self.exposed[-1]} " \
               f"infectous: {self.infectous[-1]} " \
               f"infected: {self.infected[-1]} " \
               f"recovered: {self.recovered[-1]} " \
               f"susceptible: {self.susceptible[-1]} " \
               f"cumulative: {self.infected_cum[-1]} "

    def plot(self):
        plt.plot(self.susceptible)
        plt.plot(self.infected)
        plt.plot(self.recovered)
        plt.plot(self.infected_cum)
        plt.show()
