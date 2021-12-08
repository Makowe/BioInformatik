import random
from typing import List

from entity import Entity
from map import Map
from rules import Rules
from statistics import Statistics
from timer import Timer


class Universe(object):
    """ master class that includes the map and the entities and runs the simulation"""
    def __init__(self):
        self.entities: List['Entity'] = []
        self.timer: Timer = Timer()
        self.map: Map = Map(Rules.map_size, self)
        self.statistics: Statistics = Statistics()

        self.running = False

    def simulation_setup(self):
        """ sets up the simulation """
        # generate entities
        for i in range(0, Rules.number_entities):
            entity = Entity(self.map)
            self.entities.append(entity)

        # infect single person
        spreader = self.entities[0]
        spreader.days_since_exposure = 0

        self.running = True

    def simulation_loop(self):
        """ runs the simulation and repeats the same steps until a stop condition is satisfied """
        while self.running:
            new_day = self.timer.tick()
            # stuff that should be done every tick

            # all entities walk
            for entity in self.entities:
                entity.walk()

            # all entities spread virus if they are infectous
            for entity in self.entities:
                entity.spread()

            if new_day:
                # stuff that should be done every day

                # increase day_since_exposure for all infected
                for entity in self.entities:
                    if entity.days_since_exposure >= 0:
                        entity.days_since_exposure += 1
                    if entity.days_since_exposure > Rules.days_exposure_till_infectous:
                        entity.infectous = True
                    if entity.days_since_exposure > Rules.days_exposure_till_recovered:
                        entity.end_infection()

                self.statistics.save_data_day(self.timer.day, self.entities)
                self.running = not self.stop_condition()
                print(self.statistics.print_last())
        self.simulation_end()

    def simulation_end(self):
        # analysis
        self.statistics.plot()
        return

    def stop_condition(self) -> bool:
        """ condition is sataisfied if no more entities are infected"""
        return self.statistics.infected[-1] == 0
