
from .Selection import Selection


class FitnessSelection(Selection):

    def __init__(self, rng=None):
        super().__init__(rng=rng)

    def sorted_pheno_fitness_list(self, evaluation):
        pheno_fitness_list = [
            (pheno, evaluation.fitness[pheno])
            for pheno in evaluation.fitness
        ]
        pheno_fitness_list.sort(key=lambda p_f: -p_f[1])
        return pheno_fitness_list

    def get_candidate(self, evaluation):
        pheno_fitness_list = self.sorted_pheno_fitness_list(evaluation)
        if not pheno_fitness_list:
            raise RuntimeError("get_canditate called without evaluated phenotypes")
        count = len(pheno_fitness_list) // 3
        x = self.rng.randrange(len(pheno_fitness_list))
        for i in range(count):
            x = self.rng.randrange(max(1, x))
        return pheno_fitness_list[x][0]

