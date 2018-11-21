import random


class Mutation:

    def __init__(self, rng=None):
        self.rng = rng or random.Random()

    def init(self, genotype):
        raise NotImplementedError

    def mutate(self, genotype):
        raise NotImplementedError

    def cross(self, genotype1, genotype2):
        raise NotImplementedError

