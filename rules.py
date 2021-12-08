class Rules(object):

    # VIRUS PARAMETERS

    recover_effect: float = 1.0
    """ probability that a not immune person gets immune by recovering
     0: no recovered person gets immune
     1: every recovered person gets immune """

    days_exposure_till_infectous = 5
    """ how many days until a person can infect other people"""

    days_exposure_till_recovered = 14
    """ how many days until a person is recovered"""

    # SIMULATION PARAMETERS

    map_size = 300
    """ number of tiles in vertical and horizontal direction """

    ticks_per_day = 5
    """ number of ticks that needs to be passed to complete one day """

    levy_alpha = 1.5
    """ parameter alpha for the levi fligth """

    max_distance_spread = 1
    """ maximum distance between two entities to allow exposure """

    spread_probability = 0.5
    """ probability that an infectous entity infects an other unimmune entity that is nearby. """

    # POPULATION PARAMETERS

    number_entities = 2000
    """ number of starting entities """
