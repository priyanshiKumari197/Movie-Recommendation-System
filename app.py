import pickle

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):

    if movie not in movies["title"].values:
        print("Movie not found!")
        return

    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended Movies:\n")

    for i in movie_list:
        print(movies.iloc[i[0]].title)


if __name__ == "__main__":
    movie_name = input("Enter Movie Name: ")
    recommend(movie_name)