import uuid

from pyvolution.shared import Table


class Pool:

    def __init__(self):
        self._id = "pool-%s" % uuid.uuid4()
        self._phenotypes = dict()

    @property
    def id(self): return self._id

    @property
    def phenotypes(self):
        return list(self._phenotypes.values())

    def copy(self):
        pool = self.__class__()
        for p in self.phenotypes:
            pool.add_phenotype(p.copy())
        return pool

    def add_phenotype(self, phenotype):
        self._phenotypes[phenotype.id] = phenotype

    def add_phenotypes(self, phenotypes):
        for p in phenotypes:
            self.add_phenotype(p)

    def pop_phenotype(self, phenotype_or_id):
        if phenotype_or_id in self._phenotypes:
            return self._phenotypes.pop(phenotype_or_id)
        return self._phenotypes.pop(phenotype_or_id.id)

    def clear(self):
        self._phenotypes = dict()

    def count(self):
        return len(self._phenotypes)

    def mutate(self, mutation):
        for p in self.phenotypes:
            mutation.mutate(p.genotype)
