import movie
from fresh_tomatoes import open_movies_page

if __name__ == "__main__":
    movies = []
    raw_movies_data = [
        (
            'Deadpool',
            'http://s3.foxfilm.com/foxmovies/production/films/103/images/posters/464-film-page-large.jpg',
            'https://www.youtube.com/watch?v=Xithigfg7dA',
            'Deadpool is a 2016 American superhero film based on the Marvel Comics character of the same name. It is the eighth installment of the X-Men film series, and is directed by Tim Miller. Written by Rhett Reese and Paul Wernick, the film stars Ryan Reynolds, Morena Baccarin, Ed Skrein, T. J. Miller, Gina Carano, Brianna Hildebrand, and Stefan Kapičić. In Deadpool, Wade Wilson hunts the man who gave him an accelerated healing factor, but also a scarred physical appearance.'
        ),
        (
            'Dark Circles',
            'http://gdj.gdj.netdna-cdn.com/wp-content/uploads/2012/03/movies-poster-50.jpg',
            'https://www.youtube.com/watch?v=K0HVeqjqs9E',
            'Alex (Johnathon Schaech) and Penny (Pell James) have decided to uproot themselves from their hectic city lives and move out to the country, believing that it will be better for their baby. The move is not without hesitation, as Penny is concerned that she will not be a fit mother for her baby while Alex can\'t help but wonder if it would have been better to remain in the city with his bandmates. Soon after they move, strange things begin to occur that cause them to wonder if the move was really the best idea.'
        ),
        (
            'Avengers',
            'http://interhost.hu/stuff/pics/posters/Avengers.jpg',
            'https://www.youtube.com/watch?v=eOrNdBpGMv8',
            'Marvel\'s The Avengers[4] (classified under the name Marvel Avengers Assemble in the United Kingdom and Ireland),[1][5] or simply The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.1 It is the sixth film in the Marvel Cinematic Universe. The film was written and directed by Joss Whedon and features an ensemble cast that includes Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Tom Hiddleston, Clark Gregg, Cobie Smulders, Stellan Skarsgård, and Samuel L. Jackson. In the film, Nick Fury, director of the peacekeeping organization S.H.I.E.L.D., recruits Iron Man, Captain America, the Hulk, and Thor to form a team that must stop Thor\'s brother Loki from subjugating Earth.'
        ),
        (
            'Avengers',
            'http://interhost.hu/stuff/pics/posters/Avengers.jpg',
            'https://www.youtube.com/watch?v=eOrNdBpGMv8',
            'Marvel\'s The Avengers[4] (classified under the name Marvel Avengers Assemble in the United Kingdom and Ireland),[1][5] or simply The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.1 It is the sixth film in the Marvel Cinematic Universe. The film was written and directed by Joss Whedon and features an ensemble cast that includes Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Tom Hiddleston, Clark Gregg, Cobie Smulders, Stellan Skarsgård, and Samuel L. Jackson. In the film, Nick Fury, director of the peacekeeping organization S.H.I.E.L.D., recruits Iron Man, Captain America, the Hulk, and Thor to form a team that must stop Thor\'s brother Loki from subjugating Earth.'
        )
    ]

    for data in raw_movies_data:
        movie_to_add = movie.Movie(data[0], data[1], data[2], data[3])
        movies.append(movie_to_add)

    open_movies_page(movies)