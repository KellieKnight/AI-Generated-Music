import pysynth
from random import randint

test = ( ('c', 4), ('e', 4), ('g', 4), ('c5', 1) )

list_of_notes = ['C3','D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4','A4', 'B4', 'C5', 'D5', 'E5',
                 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6']


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


#The intialization
population = []
for numb_of_indiviuals in range(0,10):
    an_individual = []
    for length_of_genome in range(0,len(test)):
        random_note = randint(-8,8)
        an_individual.append(random_note)
    population.append({"chromosome":an_individual,"fitness":fitness(an_individual)})


print(len(population))

for numb_of_indiviuals in range(0,10):
    print(population[numb_of_indiviuals]["fitness"])

print("Break")

for numb_of_indiviuals in population:
    print(numb_of_indiviuals["fitness"])