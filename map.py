from typing import List

from entity import Entity


class Map(object):
    def __init__(self, size: int, universe: 'Universe'):
        """ a quadradic map of tiles. The coordinates reach from [0 : size-1].
        E.g. a size of 100 will have the maximum tile [99, 99] and therefore a total of 100*100 tiles. """
        self.size = size

        self.universe: 'Universe' = universe
        """ reference to the universe """

    def get_near_susceptibles(self, entity_a: Entity) -> List[Entity]:
        """ returns a list of entities near entity_a.
        entity_a itself is also included in the list.
        """
        near_entities = []
        for entity_b in self.universe.entities:
            if entity_b.susceptible and self.same_pos(entity_a.pos, entity_b.pos):
                near_entities.append(entity_b)
        return near_entities

    @staticmethod
    def same_pos(pos1, pos2) -> bool:
        return pos1["x"] == pos2["x"] and pos1["y"] == pos2["y"]