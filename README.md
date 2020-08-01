# Evolving Strings

## Table of Contents

- [Overview](#Overview)
- [Demo](#Demo)
- [How to Load Project](#how-to-load-project)
- [Features](#Features)
- [Technologies Used](#technologies-used)
- [Acknowledgements](#acknowledgements)

## Overview

Evolving Strings is a simple project that showcases the Genetic Algorithm. The idea behind this project is to possess a population of strings that consist of at least a single individual that matches the target string. 

Initially, the population will consist of individuals with a chromosome (the string) with random genes (individual characters). The fitness value is calculated by how many characters differ from the target string. In my case, a lower fitness is considered better where the best fitness value is 0. After fitness values are calculated for each individual in the population, the offsprings for the next generation are produced. The best 10% of individuals from the current gernation will automatically move on to the next generation and no changes will be made. For the remaining 90%, the top 50% of individuals from the current generation will be randomly chosen as parents and mated (cross-over in the Genetic Algorithm). There is equal opportunity for either parent to pass on their genes (character) to their child but there is a 20% chance that a completely random gene will be passed on (mutation). 

Overtime, the generations will possess on average a better fitness score until eventually a generation possesses an individual who meets the target string.

## Demo

<img src="gifs/1.gif?raw=true"/> <img src="gifs/2.gif?raw=true"/> <img src="gifs/3.gif?raw=true"/>

## How to Load Project

Simply clone the Github repository to a local directory and open and run the `main.py` file using an IDE or from the terminal.

## Features

- See how a population of strings evolve towards a goal 
- Can alter the target string to see how many generations it takes to reach the target string
- Edit parameters such as population size, chromosome length, gene set and fitness calculation to make the population more sophisticated
- Implemented the Genetic Algorithm from scratch (fitness calculation, natural selection, cross-over, mutation)
- Use of OOP in Python can be used as template for future projects

## Technologies Used

- [Visual Studio Code](https://code.visualstudio.com/) - IDE used to build the project
- [Python 3.8.3](https://www.python.org/downloads/) - Programming language used

## Acknowledgements

- Thanks to [GeeksforGeeks](https://www.geeksforgeeks.org/genetic-algorithms/) for providing this idea and teaching me about this algorithm!
