# Import modules
import matplotlib.pyplot as plt
import numpy as np
# from IPython.display import Image
# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour, plot_surface)

import csv

# Set-up hyperparameters

# Call instance of PSO

def LoadData(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ",")
        max_bound = 5.12 * np.ones(2)
        # print(max_bound)
        min_bound = - max_bound
        # print(min_bound)
        bounds = (min_bound, max_bound)
        velocity_clamp=(0, 15)

        options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
        for i in readCSV:
            variable= i[0]
            print('--------------------Testing on different',variable + '----------------------' )
            i=i[1:]
            for n in i:
                if variable=='Num_Iterations':
                    optimizer = ps.single.GlobalBestPSO(n_particles=20 , dimensions=2, options=options, 
                                                        bounds=bounds, velocity_clamp=velocity_clamp)
                    cost, pos = optimizer.optimize(fx.sphere, iters=int(n))
                elif variable=='Num_Particles':
                    optimizer = ps.single.GlobalBestPSO(n_particles=int(n) , dimensions=2, options=options,
                                                        bounds=bounds, velocity_clamp=velocity_clamp)
                    cost, pos = optimizer.optimize(fx.sphere, iters=50)
                elif variable=='Num_dimensions':
                    max_bound= 5.12* np.ones(int(n))
                    min_bound= -max_bound
                    bounds=(min_bound,max_bound)
                    optimizer = ps.single.GlobalBestPSO(n_particles=20 , dimensions=int(n), options=options, 
                                                        bounds=bounds, velocity_clamp=velocity_clamp)
                    cost, pos = optimizer.optimize(fx.sphere, iters=50)
            print()
    csvfile.close()
LoadData("TestValues.csv")