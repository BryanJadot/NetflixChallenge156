import numpy as np
NUM_FEATURES = 40
NUM_MOVIES = 17000
NUM_USERS = 500000

movie_aspects = np.empty((NUM_FEATURES, NUM_MOVIES))
movie_aspects[:] = 0.1

user_aspects = np.empty((NUM_FEATURES, NUM_USERS))
user_aspects[:] = 0.1

def train(user, movie, rating):
    
