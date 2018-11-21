import copy

from pyvolution import Phenotype, Evolution
from pyvolution.genome import IntGenotype
from pyvolution.evaluation import FitnessEvaluation
from pyvolution.mutation import IntMutation


class WordGenotype(IntGenotype):

    def __init__(self):
        super().__init__(
            minimum_length=3,
            maximum_length=20,
            minimum_value=32,
            maximum_value=127,
        )

    def create_phenotype(self):
        return WordPhenotype(self)

    def copy(self):
        g = WordGenotype()
        g.values = copy.copy(self.values)
        return g


class WordPhenotype(Phenotype):

    def __str__(self):
        return self.to_string()

    def to_string(self):
        return "".join(chr(v) for v in self.genotype.values)


class WordEvaluation(FitnessEvaluation):

    goal = "Hello World!"

    def calculate_fitness(self, phenotype):
        s = phenotype.to_string()
        fitness = 0
        for i in range(min(len(s), len(self.goal))):
            dif = abs(ord(s[i]) - ord(self.goal[i]))
            fitness += max(0, 100-dif)
        fitness -= abs(len(s) - len(self.goal))
        return max(0, fitness)

    def calculate_fitness_xx(self, phenotype):
        s = phenotype.to_string()
        dif = 0.
        for i in range(min(len(s), len(self.goal))):
            dif += abs(ord(s[i]) - ord(self.goal[i]))
        fitness = 1. / dif if dif else 1.
        fitness /= 1 + abs(len(s) - len(self.goal))
        return fitness


if __name__ == "__main__":

    evolution = Evolution(
        genotypes=[WordGenotype()],
        evaluation=WordEvaluation(),
        mutation=IntMutation(mutate_probability=.1),
    )

    evolution.init_pool(5)
    evolution.evaluate()
    evolution.dump_evaluation()

    for i in range(2000):
        evolution.create_new_generation(5)
        evolution.evaluate()
        if i % 100 == 0:
            print("---- generation %s ----" % (i+1))
            evolution.dump_evaluation()

