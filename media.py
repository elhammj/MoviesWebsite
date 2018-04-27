import webbrowser

# Media file has a class Movie which is a template for each movie
# It take title, story line, image and trailer video as a parameter
class Movie():
	
	#constructor: when an instance is created, 4 argumenets should be passed title, stoy line,images and trailer url
	def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image
		self.trailer_youtube_url = movie_youtube_url

	# this function takes no argument and it opens a trailer in a webbroswer by calling webbroswer library to show the trailer
	# it takes the url that passed in movie object
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
