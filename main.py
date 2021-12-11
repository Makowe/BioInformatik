from export import Export
from rules import Rules
from universe import Universe

for contact_reduction in [0.5, 0.4, 0.3, 0.2, 0.1]:
    for follow_rules in [0.7, 0.8, 0.9, 1.0]:

        Rules.contact_reduction = contact_reduction
        Rules.follow_rules = follow_rules

        universe = Universe()
        universe.simulation_setup()
        universe.simulation_loop()
        universe.simulation_end()
        Export.save(universe.statistics, f"{contact_reduction}_{follow_rules}")
