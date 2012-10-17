def predict_rating(user, movie):
    return sum([movie * user for movie, user in izip(movie_features[user], user_features[movie]])

def train(user, movie, rating):
    
