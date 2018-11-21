import copy

from .Genotype import Genotype


class SequenceGenotype(Genotype):

    def __init__(self, values=None,
                 minimum_length=None, maximum_length=None,
                 minimum_value=None, maximum_value=None):
        super().__init__()
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.minimum_length = minimum_length
        self.maximum_length = maximum_length
        self.values = values or []

    def copy(self):
        return SequenceGenotype(
            values=copy.copy(self.values),
            minimum_length=self.minimum_length,
            maximum_length=self.maximum_length,
            minimum_value=self.minimum_value,
            maximum_value=self.maximum_value,
        )


