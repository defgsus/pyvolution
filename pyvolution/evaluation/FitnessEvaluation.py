from .Evaluation import Evaluation


class FitnessEvaluation(Evaluation):

    def __init__(self):
        super().__init__()
        self._fitness = dict()

    @property
    def fitness(self):
        """Mapping from phenotype to fitness value"""
        return self._fitness

    def clear(self):
        self._fitness = dict()

    def evaluate_phenotypes(self, phenotypes):
        for phenotype in phenotypes:
            self._fitness[phenotype] = self.calculate_fitness(phenotype)

    def calculate_fitness(self, phenotype):
        raise NotImplementedError
