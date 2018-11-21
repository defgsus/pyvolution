

class Evaluation:

    def __init__(self):
        pass

    def clear(self):
        raise NotImplementedError

    def evaluate_phenotypes(self, phenotypes):
        raise NotImplementedError

    def evaluate_pool(self, pool):
        self.evaluate_phenotypes(pool.phenotypes)
