import webbrowser

# Media file has a class Movie which is a template for each movie
# Eash movie has title, story line, image and trailer video
class Movie():
	def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image
		self.trailer_youtube_url = movie_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
