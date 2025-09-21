import pandas as pd
from main import recommend

def test_recommend_function_output():
    recommended_movie_names, recommended_movie_posters = recommend('Avatar')

    # Test that names and posters lists are not empty and have a size of 5.
    assert len(recommended_movie_names) == 5
    assert len(recommended_movie_posters) == 5

    # You could also add a check to ensure the outputs are lists of strings.
    assert isinstance(recommended_movie_names[0], str)
    assert isinstance(recommended_movie_posters[0], str)