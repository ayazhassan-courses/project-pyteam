# Import modules
# import matplotlib.pyplot as plt
import numpy as np
# from IPython.display import Image
# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
# from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)

import csv


def LoadData(filename):
    with open(filename) as csvfile:
        # loading the test value file
        readCSV = csv.reader(csvfile, delimiter = ",")
        # setting hyperparameters 
        max_bound = 5.12 * np.ones(2)
        min_bound = - max_bound
        bounds = (min_bound, max_bound)
        velocity_clamp=(0, 15)

        options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
        # looping over different set of values
        for i in readCSV:
            # first variable is the indicator of the values in the list
            variable= i[0]
            print('----------------------Testing on different',variable + '------------------------' )
            i=i[1:]
            for n in i:
                if variable=='Num_Iterations':
                    # optimizes function on different numver of iterations
                    optimizer = ps.single.GlobalBestPSO(n_particles=20 , dimensions=2, options=options, 
                                                        bounds=bounds, velocity_clamp=velocity_clamp)
                    cost, pos = optimizer.optimize(fx.sphere, iters=int(n))
                elif variable=='Num_Particles':
                    # optimizes function on different numver of particles
                    optimizer = ps.single.GlobalBestPSO(n_particles=int(n) , dimensions=2, options=options,
                                                        bounds=bounds, velocity_clamp=velocity_clamp)
                    cost, pos = optimizer.optimize(fx.sphere, iters=50)
                elif variable=='Num_dimensions':
                    # optimizes function on different numver of dimensions
                    max_bound= 5.12* np.ones(int(n))
                    min_bound= -max_bound
                    bounds=(min_bound,max_bound)
                    optimizer = ps.single.GlobalBestPSO(n_particles=20 , dimensions=int(n), options=options, 
                                                        bounds=bounds, velocity_clamp=velocity_clamp)
                    cost, pos = optimizer.optimize(fx.sphere, iters=50)
            print()
    csvfile.close()
LoadData("TestValues.csv")