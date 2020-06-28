# Import modules

import numpy as np

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import time

# setting hyperparameters
max_bound = 5.12 * np.ones(2)
# print(max_bound)
min_bound = - max_bound
# print(min_bound)
bounds = (min_bound, max_bound)
velocity_clamp = (0, 15)
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
# calling PSO
optimizer = ps.single.GlobalBestPSO(n_particles=20, dimensions=2, options=options, bounds=bounds, velocity_clamp=velocity_clamp)
# optimizing
optimizer.optimize(fx.rastrigin, 50)

# THIS PART OF CODE HELPS IN VALIDATION OF OUR IMPLEMENTED PSO WITH PYSWARMS
# 
# for validation on basis of varying number of particles RANGE [10,500]
# for K in range (10, 510, 10):
#     runtime=[]
#     for i in range (0,10):
#         start = time.time()
#         max_bound = 5.12 * np.ones(2)
#         # print(max_bound)
#         min_bound = - max_bound
#         # print(min_bound)
#         bounds = (min_bound, max_bound)
#         velocity_clamp = (0, 15)
#         options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
#         optimizer = ps.single.GlobalBestPSO(n_particles=K, dimensions=2, options=options, bounds=bounds, velocity_clamp=velocity_clamp)
#         optimizer.optimize(fx.rastrigin, 50)
#         end=time.time()
#         runtime.append(end-start)
#         # print(runtime)
#     for j in runtime:
#         print(int(j*1000000))


# # for validation on basis of varying number of dimensions RANGE [2,25]
# for K in range (2, 26):
#     runtime=[]
#     for i in range (0,10):
#         start = time.time()
#         max_bound = 5.12 * np.ones(K)
#         # print(max_bound)
#         min_bound = - max_bound
#         # print(min_bound)
#         bounds = (min_bound, max_bound)
#         velocity_clamp = (0, 15)
#         options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
#         optimizer = ps.single.GlobalBestPSO(n_particles=20, dimensions=K, options=options, bounds=bounds, velocity_clamp=velocity_clamp)
#         optimizer.optimize(fx.rastrigin, 50)
#         end=time.time()
#         runtime.append(end-start)
#         # print(runtime)
#     for j in runtime:
#         print(int(j*1000000))


# for validation on basis of varying number of iters RANGE [100,3000]
# for K in range (100, 3100, 100):
#     runtime=[]
#     for i in range (0,10):
#         start = time.time()
#         max_bound = 5.12 * np.ones(K)
#         # print(max_bound)
#         min_bound = - max_bound
#         # print(min_bound)
#         bounds = (min_bound, max_bound)
#         velocity_clamp = (0, 15)
#         options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
#         optimizer = ps.single.GlobalBestPSO(n_particles=20, dimensions=K, options=options, bounds=bounds, velocity_clamp=velocity_clamp)
#         optimizer.optimize(fx.rastrigin, 50)
#         end=time.time()
#         runtime.append(end-start)
#         # print(runtime)
#     for j in runtime:
#         print(int(j*1000000))
