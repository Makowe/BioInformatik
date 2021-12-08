from typing import List

from entity import Entity


class Map(object):
    def __init__(self, size: int, universe: 'Universe'):
        """ a quadradic map of tiles. The coordinates reach from [0 : size-1].
        E.g. a size of 100 will have the maximum tile [99, 99] and therefore a total of 100*100 tiles. """
        self.size = size

        self.universe = universe
        """ reference to the universe """

    def get_near_entities(self, entity_a: Entity, max_distance) -> List[Entity]:
        """ returns a list of entities near entity_a.
        entity_a itself is not included in the list.
        """
        near_people = []
        for entity_b in self.universe.entities:
            distance = self.calc_distance(entity_b.pos, entity_a.pos)
            if distance <= max_distance and entity_b is not entity_a:
                near_people.append(entity_b)
        return near_people

    @staticmethod
    def calc_distance(pos1, pos2) -> int:
        """ returns the rhombus shaped distance between two points"""
        return abs(pos1["x"] - pos2["x"]) + abs(pos1["y"] - pos2["y"])