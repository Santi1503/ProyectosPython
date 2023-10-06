import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies = pd.read_csv('/Proyectos/movies.csv')
ratings = pd.read_csv('/Proyectos/ratings.csv')


movie_ratings = pd.merge(ratings, movies, on='movieId')


tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies['genres'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(genre, cosine_sim=cosine_sim):
    genre_movies = movies[movies['genres'].str.contains(genre)]
    movie_indices = pd.Series(genre_movies.index, index=genre_movies['title'])

    cosine_scores = list(enumerate(cosine_sim[movie_indices['title']]))

    cosine_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)

    top_movies_indices = [i[0] for i in cosine_scores[1:11]]
    top_movies = movies.iloc[top_movies_indices]

    return top_movies['title']

user_genre = input("Ingresa el género de película que deseas ver: ")

recommendations = get_recommendations(user_genre)

print("\nTop 10 películas recomendadas del género", user_genre, ":\n")
print(recommendations)
