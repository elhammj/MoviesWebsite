import media
import fresh_tomatoes
# Entertaiment file has movie obejcts which has title, story line, images and trailer
# A quite Place Movie
# Information has been taken from 
# https://www.rottentomatoes.com/m/a_quiet_place_2018/
# https://www.imdb.com/ 
# https://www.youtube.com/
# https://en.wikipedia.org/wiki/
quiet_Place = media.Movie("A Quiet Place",
						"In the modern horror thriller A QUIET PLACE, a family of four must navigate their lives in silence after mysterious creatures that hunt by sound threaten their survival. If they hear you, they hunt you.", 
						"img/quitePlace.jpg",
						"https://www.youtube.com/watch?v=p9wE8dyzEJE")
wonder = media.Movie("Wonder",
						"Based on the New York Times bestseller, WONDER tells the incredibly inspiring and heartwarming story of August Pullman, a boy with facial differences who enters 5th grade, attending a mainstream elementary school for the first time.", 
						"img/wonder.jpg",
						"https://www.youtube.com/watch?v=ngiK1gQKgK8")
getOut = media.Movie("Dunkirk",
						"In May 1940, Germany advanced into France, trapping Allied troops on the beaches of Dunkirk. Under air and ground cover from British and French forces, troops were slowly and methodically evacuated from the beach using every serviceable naval and civilian vessel that could be found. At the end of this heroic mission, 330,000 French, British, Belgian and Dutch soldiers were safely evacuated.",
						"img/dunkirk.jpg",
						"https://www.youtube.com/watch?v=F-eMt3SrfFU")
traffik = media.Movie("Traffik",
						"Brea and John embark on a romantic weekend getaway to an isolated estate in the mountains. They are pleasantly surprised when two of their friends, Darren and Malia, also show up unexpectedly. Their plans for fun soon give way to terror when members of a violent biker gang invade the peaceful countryside. Banded together, they now find themselves in a fight for their lives as their assailants will stop at nothing to protect their secrets from the outside world.",
						"img/traffik.jpg",
						"https://www.youtube.com/watch?v=oz-XiYNCo7o")
peterRabbit = media.Movie("Peter Rabbit",
						"Peter Rabbit and his three sisters -- Flopsy, Mopsy and Cotton-Tail -- enjoy spending their days in Mr. McGregor's vegetable garden. When one of McGregor's relatives suddenly moves in, he's less than thrilled to discover a family of rabbits in his new home. A battle of wills soon breaks out as the new owner hatches scheme after scheme to get rid of Peter -- a resourceful rabbit who proves to be a worthy and wily opponent.",
						"img/peterRabbit.jpg",
						"https://www.youtube.com/watch?v=7Pa_Weidt08")
passengers = media.Movie("Passengers",
						"On a routine journey through space to a new home, two passengers, sleeping in suspended animation, are awakened 90 years too early when their ship malfunctions. As Jim and Aurora face living the rest of their lives on board, with every luxury they could ever ask for, they begin to fall for each other, unable to deny their intense attraction until they discover the ship is in grave danger. With the lives of 5,000 sleeping passengers at stake, only Jim and Aurora can save them all.",
						"img/passengers.jpg",
						"https://www.youtube.com/watch?v=7BWWWQzTpNU")
#list of movies
movies = [quiet_Place, wonder, getOut, traffik,peterRabbit,passengers]
#lunch the page 
fresh_tomatoes.open_movies_page(movies)
