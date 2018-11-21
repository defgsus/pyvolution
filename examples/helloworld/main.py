import copy

from pyvolution import Phenotype, Evolution
from pyvolution.genome import SequenceGenotype
from pyvolution.evaluation import FitnessEvaluation
from pyvolution.mutation import IntSequenceMutation


class WordGenotype(SequenceGenotype):

    def __init__(self):
        super().__init__(
            minimum_length=3,
            maximum_length=200,
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

    def to_string(self): return self.to_string_complicated()

    def to_string_easy(self):
        return "".join(chr(v) for v in self.genotype.values)

    def to_string_complicated(self):
        s = ""
        c = self.genotype.minimum_value
        last_v = 0
        for v in self.genotype.values:
            if v > last_v:
                c += 1
            elif v < last_v:
                c -= 1
            else:
                s += chr(32 + (c % (127-32)))
                c = 0
            last_v = v
        return s


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


if __name__ == "__main__":

    evolution = Evolution(
        genotypes=[WordGenotype()],
        evaluation=WordEvaluation(),
        mutation=IntSequenceMutation(
            mutate_probability=.07,
            mutate_amount=1,
        ),
    )

    POOL_SIZE = 100

    evolution.init_pool(POOL_SIZE)
    evolution.evaluate()
    evolution.dump_evaluation()

    for i in range(20000):
        evolution.create_new_generation(POOL_SIZE)
        evolution.evaluate()
        if i % 100 == 0:
            print("---- generation %s ----" % (i+1))
            evolution.dump_evaluation()

