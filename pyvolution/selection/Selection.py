import random


class Selection:

    def __init__(self, rng=None):
        self.rng = rng or random.Random()

    def get_candidate(self, evaluation):
        raise NotImplementedError

    def get_candidates(self, evaluation, num):
        candis = set()
        num_tries = 0
        while len(candis) < num:
            candis.add(self.get_candidate(evaluation))
            num_tries += 1
            if num_tries > num * 10:
                raise RuntimeError("Got not enough candidates")
        return candis
