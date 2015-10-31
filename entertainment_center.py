import movies
import fresh_tomatoes

toy_story = movies.Movie("Toy Story",
                         "Storyline of the trailer",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movies.Movie("Toy Story",
                      "Storyline of the avatar",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# here what we see movies is the file name anf in that class movie is called in that class
# init function is called which creates an instance or object of the class Movie
# init function also called a constructor because it creates an space in the memory
# self is aded by default

three_idiots = movies.Movie("3 idiots",
                      "Storyline of the movie 3 idiots",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc")

three_idiots = movies.Movie("3 idiots",
                      "Storyline of the movie 3 idiots",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc")

three_idiots = movies.Movie("3 idiots",
                      "Storyline of the movie 3 idiots",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc")

three_idiots = movies.Movie("3 idiots",
                      "Storyline of the movie 3 idiots",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc")

#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#three_idiots.show_trailer()
movies_arr = [toy_story, avatar, three_idiots, three_idiots, three_idiots, three_idiots]
#fresh_tomatoes.open_movies_page(movies_arr)
#print(movies.Movie.VALID_RATINGS)
print(movies.Movie.__doc__)
