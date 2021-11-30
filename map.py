from typing import List

from entity import Entity


class Map(object):
    def __init__(self, size: int, universe: 'Universe'):
        """ a quadradic map of fields. The coordinates reach from [0 : size-1].
        A size of 100 will have the maximum tile [99, 99]"""
        self.size = size

        self.universe = universe
        """ reference to the universe """

    def get_near_entities(self, entity_a: Entity, max_distance) -> List[dict]:
        """ returns dictionary of entities near entity_a"""
        near_people = []
        for entity_b in self.universe.entities:
            distance = self.pos_distance(entity_b.pos, entity_a.pos)
            if distance <= max_distance and entity_b is not entity_a:
                near_people.append({
                    "entity": entity_b,
                    "distance": distance})
        return near_people

    @staticmethod
    def pos_distance(pos1, pos2) -> int:
        """ returns the rhombus shaped distance between two points"""
        return abs(pos1["x"] - pos2["x"]) + abs(pos1["y"] - pos2["y"])