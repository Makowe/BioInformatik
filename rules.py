class Rules(object):

    # VIRUS PARAMETERS

    vac_immunity: float = 0.6
    """ describes how the immunity is increased with a vaccination. """

    recover_immunity: float = 1
    """ describes how the immunity is increased by recovering"""

    vac_reduce_spread: float = 0.5
    """ describes how the probabilty of infecting an other entity is decreased """

    days_exposure_till_infectous = 5
    """ describes how many days until a person can infect other people"""

    days_exposure_till_recovered = 14
    """ describes how many days until a person is recovered"""

    mortality = 0.05
    """ describes the probabilty that a infected person dies after the infection """

    # SIMULATION PARAMETERS

    map_size = 200
    """ number of tiles in vertical and hrizontal direction """

    ticks_per_day = 10
    """ number of ticks that needs to be passed to complete one day """

    levy_alpha = 1.5
    """ parameter alpha for the levi fligth """

    max_distance_spread = 3
    """ maximum distance between two entities to allow exposure """

    spread_probability = 0.2
    """ probability that an infectous entity is directly at a uninfected entity. The probability is
     further decreased by:
     - distance between entities
     - vaccination of the spreader
     - immunity rate of the receiver
     """

    # POPULATION PARAMETERS

    number_entities = 1000
    """ number of starting entities """

    vaccination_rate = 0.5
    """ probability of a single entity to be vaccinated """
