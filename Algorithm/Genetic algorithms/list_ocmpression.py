from typing import Tuple, List, Any, Type
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import shuffle, sample
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps


PEOPLE: List[str] = ["Michael", "Sarah", "Joshua", "Narine", "David", "Sajid", "Melanie", "Daniel", "Wei", "Dean",
                     "Brian", "Murat", "Lisa"]


class ListCompression(Chromosome):
    def __init__(self, lst: List[Any]) -> None:
        self.lst = lst

    @property
    def bytes_compressed(self) -> int:
        return getsizeof(compress(dumps(self.lst)))

    def fitness(self) -> float:
        return 1 / self.bytes_compressed

    @classmethod
    def random_instance(cls) -> 'ListCompression':
        my_list: List[str] = deepcopy(PEOPLE)
        shuffle(my_list)
        return ListCompression(my_list)

    def crossover(self, other: 'ListCompression') -> Tuple['ListCompression', 'ListCompression']:
        child1: ListCompression = deepcopy(self)
        child2: ListCompression = deepcopy(other)
        idx1, idx2 = sample(range(len(self.lst)), 2)
        l1, l2 = child1.lst[idx1], child2.lst[idx2]
        child1.lst[child1.lst.index(l2)], child1.lst[idx2] = child1.lst[idx2], l2
        child2.lst[child2.lst.index(l1)], child2.lst[idx1] = child2.lst[idx1], l1
        return child1, child2

    def mutate(self) -> None:
        idx1, idx2 = sample(range(len(self.lst)), 2)
        self.lst[idx1], self.lst[idx2] = self.lst[idx2], self.lst[idx1]

    def __str__(self) -> str:
        return f"Order: {self.lst} Bytes: {self.bytes_compressed}"


if __name__ == "__main__":
    initial_population: List[ListCompression] = [ListCompression.random_instance() for _ in range(1000)]
    ga: GeneticAlgorithm[ListCompression] = GeneticAlgorithm(initial_population, threshold=1.0, max_generations=10000,
                                                             mutation_chance=0.2, crossover_chance=0.7,
                                                             selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT)
    result = ga.run()
    print(result)
