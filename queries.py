# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    query = """
    SELECT movies.title, movies.genres,directors.name
    FROM Movies
    JOIN directors ON movies.director_id  = directors.id
    """
    db.execute(query)
    result = db.fetchall()
    result_list = []
    for elem in result:
        result_list.append(elem[0][0])
    return result_list



def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    pass  # YOUR CODE HERE


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    pass  # YOUR CODE HERE


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    pass  # YOUR CODE HERE


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    pass  # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    pass  # YOUR CODE HERE
