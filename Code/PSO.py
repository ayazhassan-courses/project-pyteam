from random import randint
import math

# fitness function


def sphere(x):
    fitness = 0
    for i in range(len(x)):
        fitness += x[i]**2
    return fitness


def Calculate_fitness(X, fitness_i, Num_Particles, pbest_pos_i, pbest_val_i, gbest_pos, gbest_val):
    for p in range(Num_Particles):
        fitness_i[p] = sphere(X[p])
        if fitness_i[p] < gbest_val:
            gbest_val = fitness_i[p]
            gbest_pos = X[p]

        if fitness_i[p] < pbest_val_i[p]:
            pbest_val_i[p] = fitness_i[p]
            pbest_pos_i[p] = X[p]

    return gbest_val, gbest_pos, pbest_pos_i, pbest_val_i, fitness_i


def initial_velocity(Num_Particles, Num_dimensions, vMin, vMax):
    V = []
    for p in range(Num_Particles):
        temp_V = []
        for i in range(Num_dimensions):
            temp_V.append(vMin + randint(0, 1)*(vMax-vMin))
        V.append(temp_V)
    return V


def initial_position(Num_Particles, Num_dimensions, xMin, xMax):
    X = []
    for p in range(Num_Particles):
        temp_X = []
        for i in range(Num_dimensions):
            temp_X.append(xMin + randint(0, 1)*(xMax-xMin))
        X.append(temp_X)
    return X


def update_velocity(X, V, Num_Particles, Num_dimensions, i, w, vMin, vMax, pbest_pos_i, gbest_pos, c1, c2):
    for p in range(Num_Particles):
        for i in range(Num_dimensions):
            r1 = randint(0, 1)
            r2 = randint(0, 1)
            V[p][i] = w * V[p][i] + (r1 * c1 * (pbest_pos_i[p]
                                                [i] - X[p][i])) + (r2*c2 * (gbest_pos[i] - X[p][i]))
            if V[p][i] > vMax:
                V[p][i] = vMax
            if V[p][i] < vMin:
                V[p][i] = vMin
    return V


def update_position(X, Num_Particles, Num_dimensions, xMin, xMax, V):
    for p in range(0, Num_Particles):
        for i in range(0, Num_dimensions):
            X[p][i] = X[p][i] + X[p][i]
            if X[p][i] > xMax:
                X[p][i] = xMax
            if X[p][i] < xMin:
                X[p][i] = xMin
    return X


def PSO():
    # initialization of all parameters
    Num_Iterations = 50      # number of iterations to be performed
    Num_Particles = 25       # number of particles in search space
    Num_dimensions = 5      # variables in function
    w = 0                    # constant weight inertia to vary the velocity in each iteration
    # lower and upper bound of weight inertia to increase or decrease velocity in search space
    wMin, wMax = 0.5, 0.9
    c1 = 1                    # cognitive/individual constant parameter
    c2 = 2                    # social constant parameter
    xMin, xMax = -50, 50       # lower and upper bound of search space
    vMin, vMax = -12.5, 12.5   # initial lower and upper bound of velocity
    gbest_val = 1000000  # setting global best value of swarm to infinity
    # setting personal best value for each particle
    pbest_val_i = [1000000 for i in range(Num_Particles)]
    pbest_pos_i = [[0 for i in range(Num_dimensions)] for i in range(
        Num_Particles)]  # personal best position of each
    # particle in each dimension
    # global best position of the swarm
    gbest_pos = [0 for i in range(Num_dimensions)]

    # current/initial position of each particle
    X = initial_position(Num_Particles, Num_dimensions, xMin, xMax)
    # current/initial velocity of each particle
    V = initial_velocity(Num_Particles, Num_dimensions, vMin, vMax)
    # fitness of each particle at initial position
    fitness_i = [sphere(X[i]) for i in range(Num_Particles)]

    i = 0
    while i < Num_Iterations:
        X = update_position(X, Num_Particles, Num_dimensions, xMin, xMax, V)
        fitness_i, gbest_val, gbest_pos, pbest_pos_i, pbest_val_i = Calculate_fitness(
            X, fitness_i, Num_Particles, pbest_pos_i, pbest_val_i, gbest_pos, gbest_val)
        w = wMax - ((wMax-wMin)/Num_Iterations)*i
        V = update_velocity(X, V, Num_Particles, Num_dimensions,
                            i, w, vMin, vMax, pbest_pos_i, gbest_pos, c1, c2)
    print(gbest_pos, gbest_val)


PSO()
