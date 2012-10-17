import numpy as np                                                                                                                                                                   

NUM_FEATURES = 40 
NUM_USERS = 458293
NUM_MOVIES = 17770

def _read_in_data(path):
    with  open(path) as f:
        data = [tuple(line[-1].split(',')) for line in f]
    return data

def read_in_mu():                                                                                                                                  
    return _read_in_data("mu/all.dta")
    
def read_in_um():
    return _read_in_data("um/all.dta")

movie_aspects = np.empty((NUM_FEATURES, NUM_MOVIES))
movie_aspects[:] = 0.1

user_aspects = np.empty((NUM_FEATURES, NUM_USERS))
user_aspects[:] = 0.1
