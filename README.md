## AI-Generated-Music
Project for Game AI class. 
Takes a base MIDI song, and uses a genetic algorithm and fitness function to "evolve" the song into something new. 
Implemented in Python using PySynth.

PySynth converts text representation of generated song into a .wav file

Fitness function is based on basic music theory concepts. 
Selects for melodic patterns based the following properties:

-Patterns that start on I/VIII or V note in the current C major scale

-Patterns that contain more stepwise motions (notes move by interval of 1)

-Patterns that don't have huge leap, or

-Patterns that have a stepwise motion in the opposite direction before or after a leap. 
