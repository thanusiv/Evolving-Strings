import random

class Individual:

    def __init__(self, s):
        self.chromosome = s
        self.fitness = None

    def calculate_fitness(self, target_string):
        score = 0
        for chromosome_letter, target_letter in zip(self.chromosome, target_string):
            if chromosome_letter != target_letter:
                score += 1
        self.fitness = score
    
    def mate(self, parent_2, possible_genes):
        child_chromosome_list = []

        for gene_1, gene_2 in zip(self.chromosome, parent_2.chromosome):
            prob = random.random()
            if prob < 0.40:
                child_chromosome_list.append(gene_1)
            elif prob < 0.80:
                child_chromosome_list.append(gene_2)
            else:
                child_chromosome_list.append(random.choice(possible_genes))
        
        child_chromosome_string = ''.join(child_chromosome_list)
        return Individual(child_chromosome_string)
