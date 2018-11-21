import random

from .Pool import Pool
from .evaluation import FitnessEvaluation
from .selection import FitnessSelection
from .mutation import IntMutation
from .genome import IntGenotype
from .shared import Table


class Evolution:

    def __init__(self, pool=None, genotypes=None, evaluation=None, selection=None, mutation=None,
                 rng=None):
        self.pool = pool or Pool()
        self.rng = rng or random.Random()
        self.genotypes = genotypes or [IntGenotype()]
        self.selection = selection or FitnessSelection()
        self.evaluation = evaluation or FitnessEvaluation()
        self.mutation = mutation or IntMutation()

    def init_pool(self, num):
        self.pool.clear()
        for i in range(num):
            new_genotype = random.choice(self.genotypes).copy()
            self.mutation.init(new_genotype)
            new_phenotype = new_genotype.create_phenotype()
            self.pool.add_phenotype(new_phenotype)

    def evaluate(self):
        eval_pool = self.pool.copy()
        eval_pool.mutate(self.mutation)
        self.evaluation.clear()
        self.evaluation.evaluate_pool(self.pool)
        self.evaluation.evaluate_pool(eval_pool)

    def dump_evaluation(self):
        table = Table(["genotype", "phenotype", "fitness"])
        for phenotype in self.evaluation.fitness:
            table.add_row([
                phenotype.genotype, phenotype, self.evaluation.fitness[phenotype]
            ])
        table.sort_by_column(-1, key=lambda x: -x)
        table.dump()

    def create_new_generation(self, num):
        pheno_f = self.selection.sorted_pheno_fitness_list(self.evaluation)
        selected_phenos = [p for p, f in pheno_f[:num]]
        self.pool.clear()
        self.pool.add_phenotypes(selected_phenos)
        #for i in range(num):
        #    phenotype = self.selection.get_candidate(self.evaluation).copy()
        #    self.pool.add_phenotype(phenotype)

