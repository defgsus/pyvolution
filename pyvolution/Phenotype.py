import uuid


class Phenotype:

    def __init__(self, genotype):
        self._id = "phen-%s" % uuid.uuid4()
        self._genotype = genotype

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, str(self))

    def __str__(self):
        return self._id

    @property
    def id(self): return self._id

    @property
    def genotype(self): return self._genotype

    def copy(self):
        return self.__class__(self.genotype.copy())


