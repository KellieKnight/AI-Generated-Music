#
# Genetic Algorithm
#
from random import randint
from random import random

list_of_notes = ['C3','D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4','A4', 'B4', 'C5', 'D5', 'E5',
                 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6']

test = ( ('c', 4), ('e', 4), ('g', 4), ('c5', 1) )

def initialize(population, population_size):
    for numb_of_indiviuals in range(0, population_size):
        an_individual = []
        for length_of_genome in range(0, len(test)):
            random_note = randint(-8, 8)
            an_individual.append(random_note)
        population.append(an_individual)
    return population


def fitness(individual):
    fitness = 1
    for x in range(len(individual)):

        if individual[x] == 2 or individual[x] == -2:
            fitness += 0
        else:
            if fitness >= .1:
                fitness -= .1
                # the 1/3 is the "best" interval

    return fitness

def evaluate(population):
    evaluated_population = []
    for individual in population:
        evaluated_population.append({"chromosome":individual,"fitness":fitness(individual)})

    return evaluated_population

def select(population):
    sum = 0
    for individual in population:
        sum += individual['fitness']

    population_with_probability = []
    sum_of_probability = 0
    for individual in population:
        probability = sum_of_probability + (individual['fitness']/sum)
        population_with_probability.append((individual,probability))
        sum_of_probability += probability

    fittest_parents = []
    while len(fittest_parents)!= 2:
        random_num = random()
        for individual in range(0,len(population_with_probability)):
            if individual != len(population_with_probability)-1:
                if random_num > population_with_probability[individual][1] \
                        and random_num < population_with_probability[individual+1][1]:
                    fittest_parents.append(population_with_probability[individual][0])

    parent1 = fittest_parents[0]['chromosome']
    parent2 = fittest_parents[1]['chromosome']

    return parent1, parent2

def crossover(parent1, parent2, population):

    maxlength = len(parent1)-1
    crosspoint = randint(0,maxlength)
    child1 = []
    child2=[]


    for i in range(0,len(parent1)):
        child1.append(0)
        child2.append(0)

    if crosspoint == 0:
        child1[0] = parent1[0]
        child2[0] = parent2[0]
    else:
        for i in range(0,crosspoint):
            child1[i] = parent1[i]
            child2[i] = parent2[i]

    if crosspoint == maxlength:
        child1[maxlength] = parent1[maxlength]
        child2[maxlength] = parent2[maxlength]
    else:
        for i in range (crosspoint,len(parent1)):
            child1[i] = parent1[i]
            child2[i] = parent2[i]

    population.append(child1)
    population.append(child2)


def mutation(individual):
    for x in range(len(individual)):
        random_num = randint(0, 100)
        if random_num >= 95:
            individual[x] = randint(-8, 8)


if __name__ == '__main__':

    cur_generation = 0
    max_generations = 100
    pop_size = 10
    #mutation_rate = 0.05

    starting_population = []

    # Randomly initialize the population
    population = initialize(starting_population, pop_size)

    while cur_generation < max_generations:

        # Select the best individual of the population using a fitness function

        evaluated_population = evaluate(population)
        Parent1, Parent2 = select(evaluated_population)
        #print(Parent1,Parent2)
        # Apply crossover operation to the selected population
        crossover(Parent1,Parent2, population)

        # Apply mutation operation to the selected population
        for individual in population:
            mutation(individual)

        # Update current population with selected population

        cur_generation += 1

    evolution_done = evaluate(population)
    evolution_done = sorted(evolution_done, key=lambda individual: individual["fitness"], reverse=True)
    for x in evolution_done:
        print(x)
