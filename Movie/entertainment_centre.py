import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy",
                        "http://3.bp.blogspot.com/_Y-DbBvf7R5Y/TB4RQEeWchI/AAAAAAAActE/dF0nYpbAd3A/s1600/toy-story-3-1893.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avater = media.Movie("Avater",
                     "Marine in an alien planet",
                     "data:image/jpeg;base64,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",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
school_of_rock=media.Movie("School of Rock",
                           "Using rock music to learn",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=oP7kExN8LFA")


movies = [toy_story,avater,school_of_rock]
fresh_tomatoes.open_movies_page(movies)
