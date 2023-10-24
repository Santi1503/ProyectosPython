import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv('../../Proyectos/BOTS/netflix_titles.csv')

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(data['sinopsis'])
consine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def GetRecommendations(title):
    idx = data[data['title'] == title].index[0]
    sim_scores = list(enumerate(consine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return data['title'].iloc[movie_indices]

while True:
    print("Bienvenido al sistema de recomendación de peluculas")
    movie_title = input("Ingrese el título de la pelicula que te guste (o escribe 'salir' para salir)")

    if movie_title.lower() == 'salir':
        print("Hasta luego :)")
        break

    if movie_title in data['title'].values:
        recommendations = GetRecommendations(movie_title)
        print("\nPeliculas similares a ", movie_title , " son : ")
        print(recommendations)
    else:
        print("No se encontro una película con ese titulo")