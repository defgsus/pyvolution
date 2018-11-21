import uuid


class Genotype:

    def __init__(self):
        self._id = "gen-%s" % uuid.uuid4()

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, str(self))

    def __str__(self):
        return self._id

    @property
    def id(self): return self._id

    def copy(self):
        return self.__class__()

    def randomize(self):
        raise NotImplementedError

    def create_phenotype(self):
        raise NotImplementedError

