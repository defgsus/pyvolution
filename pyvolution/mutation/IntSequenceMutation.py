from .Mutation import Mutation


class IntSequenceMutation(Mutation):

    def __init__(
            self,
            mutate_probability=0.1,
            mutate_amount=1,
            insert_probability=0.1,
            remove_probability=0.1,
            rng=None
    ):
        super().__init__(rng=rng)
        self.mutate_probability = mutate_probability
        self.mutate_amount = mutate_amount
        self.insert_probability = insert_probability
        self.remove_probability = remove_probability

    def init(self, genotype):
        min_val = 0 if genotype.minimum_value is None else genotype.minimum_value
        max_val = 1 if genotype.maximum_value is None else genotype.maximum_value
        length = self.rng.randint(
            1 if genotype.minimum_length is None else genotype.minimum_length,
            10 if genotype.maximum_length is None else genotype.maximum_length
        )
        genotype.values = [
            self.rng.randint(min_val, max_val)
            for i in range(length)
        ]

    def mutate(self, genotype):
        for i, v in enumerate(genotype.values):
            if self.rng.random() < self.mutate_probability:
                new_v = v + self.rng.randint(-self.mutate_amount, self.mutate_amount)
                new_v = max(genotype.minimum_value, min(genotype.maximum_value, new_v))
                genotype.values[i] = new_v

        if self.rng.random() < self.remove_probability:
            if len(genotype.values) > (genotype.minimum_length or 0):
                genotype.values.pop(
                    self.rng.randrange(len(genotype.values))
                )

        if self.rng.random() < self.insert_probability:
            if not genotype.maximum_length or len(genotype.values) < genotype.maximum_length:
                genotype.values.insert(
                    self.rng.randrange(len(genotype.values)),
                    self.rng.randint(
                        0 if genotype.minimum_value is None else genotype.minimum_value,
                        1 if genotype.maximum_value is None else genotype.maximum_value,
                    )
                )

    def cross(self, genotype1, genotype2):
        raise NotImplementedError

