import webbrowser
class Movie():
    # name init is reserved in python so we use two underscores before and after init
    # self is the object being created
    # below is the class variable
    """ this file gives a little information about different movies"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # instance variables are movie_title and other three also
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
