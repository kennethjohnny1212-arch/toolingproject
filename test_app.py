import pandas as pd
from main import get_recommendation_based_on_movie_name

def test_get_recommendation_based_on_movie_name():
    # Get recommendations for a known movie, e.g., 'Avatar'
    # The project uses a specific movie title, so make sure to use one from the dataset.
    recommendations = get_recommendation_based_on_movie_name('Avatar')

    # Check if the function returns a non-empty list of recommendations
    assert len(recommendations) > 0

    # Check if the output is a pandas DataFrame as expected
    assert isinstance(recommendations, pd.DataFrame)
