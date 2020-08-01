from population import Population

def main():
    size = 200
    population = Population(size)

    while not population.found:
        population.calculate_fitness_and_sort()
        print("Generation: {}\tString: {}\tFitness: {}".format(population.generation, population.get_current_best_individual_chromosome(), population.get_current_best_individual_fitness()))

        if population.check_if_target_reached():
            population.found = True
            continue

        new_generation = []
        new_generation.extend(population.get_top_10_percent())
        new_generation.extend(population.produce_and_mutate_offspring()) # fill all remaining spots with offsprings from crossover and mutation

        population.set_new_population(new_generation)
    
    print('Found!')

if __name__ == "__main__":
    main()