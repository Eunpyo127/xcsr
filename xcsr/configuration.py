# Brodderick Rodriguez
# Auburn University - CSSE
# july 12 2019

import numpy as np


class Configuration:
    def __init__(self):

        # the maximum number of steps in each problem (replication)
        self.episodes_per_replication = 10 ** 4

        self.steps_per_episode = 1

        self.is_multi_step = False

        self.predicate_1 = 0.29

        # the maximum size of the population (in micro-classifiers)
        self.N = 100

        # learning rate for payoff, epsilon, fitness, and action_set_size
        self.beta = np.random.uniform(0.1, 0.9)

        # used to calculate the fitness of a classifier
        self.alpha = 0.1
        self.epsilon_0 = 0.01
        self.v = 5

        # discount factor
        self.gamma = np.random.uniform(0.9, 0.99)

        # the GA threshold. GA is applied in a set when the average time
        # since the last GA in the set is greater than theta_ga
        self.theta_ga = np.random.uniform(25, 50)

        # the probability of applying crossover in the GA
        self.chi = 0.8

        # specifies the probability of mutating an allele in the offspring
        self.mu = np.random.uniform(0.01, 0.05)

        # subsumption threshold. experience of a classifier must be greater
        # than theta_sub in order to be able to subsume another classifier
        self.theta_sub = 20

        # probability of using '#' (Classifier.WILDCARD_ATTRIBUTE_VALUE)
        # in one attribute in the condition of a classifier when covering
        self.p_sharp = 0.33

        # used as initial values in new classifiers
        self.p_1 = np.random.uniform(0, 10 ** -4)
        self.epsilon_1 = np.random.uniform(0, 10 ** -4)
        self.F_1 = np.random.uniform(0, 10 ** -4)

        # probability during action selection of choosing the
        # action uniform randomly
        self.p_explr = 0.5

        # the minimum number of actions that must be present in match_set
        # or else covering will occur
        # "to cause covering to provide classifiers for every action, set
        # equal to number of available actions"
        self.theta_mna = 1

        # boolean parameter. specifies if offspring are to be tested
        # for possible subsumption by parents
        self.do_ga_subsumption = True
