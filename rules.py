class Rules(object):

    # VIRUS PARAMETERS

    days_exposure_till_infectous = 5
    """ how many days until a person can infect other people"""

    days_exposure_till_recovered = 14
    """ how many days until a person is recovered"""

    # SIMULATION PARAMETERS

    map_size = 20
    """ number of tiles in vertical and horizontal direction """

    ticks_per_day = 10
    """ number of ticks that needs to be passed to complete one day """

    levy_alpha = 2
    """ parameter alpha for the levi fligth """

    spread_probability = 0.003
    """ probability that an infectous entity infects an other unimmune entity that is nearby. """

    start_spreaders = 10
    """ number of entities being infected at the beginning. """

    stop_spreaders = 5
    """ simulation stops when the number of currently infected is lower than this number. """

    number_entities = 5000
    """ number of entities """

    contact_reduction = 0.5
    """ contact reduction in percent """

    follow_rules = 1
    """ percentage of people following contact reduction rule """
