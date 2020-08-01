import random
from individual import Individual

class Population:

    def __init__(self, size):
        self.target_string = "abcdefg!fedcba()"
        self.possible_genes = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
                                 QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
        self.size = size
        values = [''.join(random.choice(self.possible_genes) for _ in range(len(self.target_string))) for i in range(size)]
        self.population = [Individual(s) for s in values]
        self.generation = 1
        self.found = False

    def calculate_fitness_and_sort(self):
        for s in self.population:
            s.calculate_fitness(self.target_string)
        self.population = sorted(self.population, key = lambda x: x.fitness)

    def check_if_target_reached(self):
        return self.get_current_best_individual_fitness() == 0
        
    def set_new_population(self, new_population):
        self.population = new_population

    def get_top_10_percent(self):
        return self.population[:int(0.1 * self.size)]

    def get_current_best_individual_chromosome(self):
        return self.population[0].chromosome

    def get_current_best_individual_fitness(self):
        return self.population[0].fitness
    
    def produce_and_mutate_offspring(self):
        top_50 = self.population[:self.size // 2]
        new_offsprings = []
        remaining_spots_to_fill = int(0.9 * self.size)

        for _ in range(remaining_spots_to_fill):
            parent_1 = random.choice(top_50)
            parent_2 = random.choice(top_50)
            off_spring = parent_1.mate(parent_2, self.possible_genes)
            new_offsprings.append(off_spring)
        
        self.generation += 1
        
        return new_offsprings

