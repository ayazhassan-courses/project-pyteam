import random
import math
import csv
from datetime import datetime
# Test function 1: fitness function of the swarm which has to be optimized (minimized)

def sphere(x):
    fitness = 0
    for i in range(len(x)):
        fitness += x[i]**2
    return fitness

# function to update the fitness value of every particle in each iteration

def Calculate_fitness(X, fitness_i, Num_Particles):
    for p in range(Num_Particles):
        fitness_i[p] = sphere(X[p])
    return fitness_i

# function to update the personal best of each particle and global best value of entire swarm


def update_pbest_and_gbest(X, fitness_i, Num_particles, gbest_val, gbest_pos, pbest_pos_i, pbest_val_i):
    for p in range(Num_particles):
        # updates the global best
        if fitness_i[p] < gbest_val:
            gbest_val = fitness_i[p]
            gbest_pos = X[p]
        # updates the personal best
        elif fitness_i[p] < pbest_val_i[p]:
            pbest_val_i[p] = fitness_i[p]
            pbest_pos_i[p] = X[p]
    return gbest_val, gbest_pos, pbest_pos_i, pbest_val_i


def initial_velocity(Num_Particles, Num_dimensions, vMin, vMax):
    V = []      # list containing velocity of each particle in n dimensions
    for p in range(Num_Particles):
        temp_V = []
        for i in range(Num_dimensions):
            temp_V.append(random.uniform(vMin,vMax))
        V.append(temp_V)
    return V


def initial_position(Num_Particles, Num_dimensions, xMin, xMax):
    X = []      # list containing position of each particle in n dimensions
    for p in range(Num_Particles):
        temp_X = []
        for i in range(Num_dimensions):
            temp_X.append(random.uniform(xMin,xMax))
        X.append(temp_X)
    return X

# function to update the velocity of each particle


def update_velocity(X, V, Num_Particles, Num_dimensions, w, vMin, vMax, pbest_pos_i, gbest_pos, c1, c2):
    for p in range(Num_Particles):
        for i in range(Num_dimensions):
            # random number genration strategy is different from the referenced code
            r1 = random.uniform(0,1)
            r2 = random.uniform(0,1)
            # equation to calculate new velocity of particle for next iteration
            V[p][i] = w * V[p][i] + (r1*c1*(pbest_pos_i[p][i] - X[p][i])) + (r2*c2 * (gbest_pos[i] - X[p][i]))
            # strategy of controlling the out of bound velocity is different from referenced code
            if V[p][i] > vMax or V[p][i] < vMin:
                V[p][i] = random.uniform(vMin,vMax)
    return V

# function to update the position of each particle


def update_position(X, Num_Particles, Num_dimensions, xMin, xMax, V):
    for p in range(0, Num_Particles):
        for i in range(0, Num_dimensions):
            # calculates the new position of particle
            X[p][i] = X[p][i] + V[p][i]
            # strategy of controlling the out of bound position is different from referenced code
            if X[p][i] > xMax or X[p][i] < xMin:
                X[p][i] = random.uniform(xMin,xMax)
    return X

#  Main PSO() functions that calls other helper functions and handles initialization and updations


def PSO(Num_Iterations, Num_Particles,Num_dimensions):
    # Initialization of parameters
    # note: the referenced code randomly updated inertia in iterating loop. In this code it will remain constant.
    w = 0.9                  # constant weight inertia
    c1 = 0.5                 # cognitive/individual constant parameter
    c2 = 0.3                 # social constant parameter
    xMin, xMax = -5.12, 5.12   # lower and upper bound of search space
    vMin, vMax = 0, 15         # initial lower and upper bound of velocity

    # setting global best value of swarm to infinity
    gbest_val = float('inf')
    # setting personal best value for each particle
    pbest_val_i = [float('inf') for i in range(Num_Particles)]
    # personal best position of each particle in each dimension
    pbest_pos_i = [[0 for i in range(Num_dimensions)]
                   for j in range(Num_Particles)]
    # global best position of the swarm
    gbest_pos = [0 for i in range(Num_dimensions)]

    # current/initial position of each particle
    X = initial_position(Num_Particles, Num_dimensions, xMin, xMax)
    # current/initial velocity of each particle
    V = initial_velocity(Num_Particles, Num_dimensions, vMin, vMax)
    # fitness of each particle at initial position
    fitness_i = [sphere(X[i]) for i in range(Num_Particles)]

    i = 1
    # iterating the swarm N number of times (N generations of swarm)
    while i < Num_Iterations:
        # updates the position in search space
        X = update_position(X, Num_Particles, Num_dimensions, xMin, xMax, V)

        # To update the fitness value of each particle with Calculate_fitness()
        # Note:
        #  In the referenced code, updation of fitness,gbest, and pbest
        #  was done by the same function,updateFitness(), while our code does it
        #  using two separate function: Calculate_fitness() and update_pbest_and_gbest()
        fitness_i = Calculate_fitness(X, fitness_i, Num_Particles)

        # updates personal best of each particle and global best value of the swarm
        gbest_val, gbest_pos, pbest_pos_i, pbest_val_i = update_pbest_and_gbest(X, fitness_i, Num_Particles,
                                                                                gbest_val, gbest_pos, pbest_pos_i, pbest_val_i)

        V = update_velocity(X, V, Num_Particles, Num_dimensions,
                            w, vMin, vMax, pbest_pos_i, gbest_pos, c1, c2)
        i += 1
    print("Global Best Value: {}".format(gbest_val))
    print("Global Best Position: {}".format(gbest_pos))

#  This function loads data in the file TEST VALUES and passes it to PSO function
def main():
    #  passing test values for varying number of dimensions
    for i in range (2, 26):
        runtime=[]
        for j in range (0,10):
            start=datetime.now()
            PSO( 50 , 20 , i)
            runtime.append(datetime.now()-start)
        print(runtime)
    #  passing test values for varying number of iterations
    for i in range (100, 3100, 100):
        runtime=[]
        for j in range (0,10):
            start=datetime.now()
            PSO( i , 20 , 2)
            runtime.append(datetime.now()-start)
        print(runtime)
    #  passing test values for varying number of particles
    for i in range (10, 510, 10):
        runtime=[]
        for j in range (0,10):
            start=datetime.now()
            PSO( 50 , i , 2)
            runtime.append(datetime.now()-start)
        print(runtime)
main()

# Code Reference:
# https://github.com/rgreen13/PSO-Python.git
