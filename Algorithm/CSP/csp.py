from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Dict, Any
from random import choice, randint, random, sample, choices
from copy import deepcopy


V = TypeVar('V')
D = TypeVar('D')


class Constraint(ABC, Generic[V, D]):
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment) -> bool:
        ...


class CSP(Generic[V, D]):
    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in variables:
            self.constraints[variable] = []
            if variable not in domains:
                raise LookupError("Every variable should have a domain assign it")

    def add_constraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint but not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if constraint.satisfied(assignment):
                return True
        return False

    def back_tracking_search(self, assignment=None):
        if assignment is None:
            assignment = {}
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.back_tracking_search(local_assignment)
                if result is not None:
                    return result
        return None

    def genetic_algorithm(self, population_size = 100, mutate_rate: float = 0.1, crossover_rate: float = 0.7,
                          max_generations: int = 1000):
        population = self.initial_population(population_size)
        best_solution = None
        best_fitness = -1
        current_best_solution = None

        for generation in range(max_generations):
            fitness_scores = [self.evaluate_fitness(individual) for individual in population]
            current_best_fitness = max(fitness_scores)
            current_best_solution = population[fitness_scores.index(current_best_fitness)]

            if current_best_fitness > best_fitness:
                best_solution = current_best_solution
                best_fitness = current_best_fitness

            if best_fitness == len(self.constraints):
                return best_solution

            selected_parents = self.select_parents(population, fitness_scores)
            next_generation = []
            while len(next_generation) < population_size:
                parent1, parent2 = sample(selected_parents, 2)

                if random() < crossover_rate:
                    child = self.crossover(parent1, parent2)
                else:
                    child = deepcopy(parent1)
                next_generation.append(self.mutate(child, mutate_rate))
            population = next_generation
        return current_best_solution

    def initial_population(self, population_size):
        return [
            {variable: choice(self.domains[variable]) for variable in self.variables}
            for _ in range(population_size)
        ]

    def evaluate_fitness(self, individual):
        satisfied_constraint = sum(
            1 for constraint in self.constraints.values() for var in constraint if var.satisfied(individual)
        )
        return satisfied_constraint

    def select_parents(self, population, fitness_scores):
        total_fitness = sum(fitness_scores)
        probabilities = [score / (total_fitness + 1) for score in fitness_scores]
        return choices(population, weights=probabilities, k=len(population) // 2)

    def crossover(self, parent1, parent2):
        child = {}
        for variable in parent1.variables:
            child[variable] = parent1[variable] if random() < 0.5 else parent2[variable]
        return child

    def mutate(self, individual, mutate_rate):
        for variable in self.variables:
            if random() < mutate_rate:
                individual[variable] = choice(self.domains[variable])
        return individual
