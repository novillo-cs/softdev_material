## Exercise 3

```Save your work here: your_repo/unit_7/03_pandas_movies/YOUR_FILES_HERE(CSV AND NOTEBOOK)```

1. Read the csv files and store the content in dataframes.
2. Create a new dataframe movies_tags_df by merging movies & tags dataframes with a left join on movieId
3. Use the merged dataframe movies_tags_df to select the movies with no tags.
4. Create a new dataframe tags_ratings_df by merging tags & ratings dataframes using the movie ID and the user ID.
5. Get rating counts: ```rating_counts = ratings_df.movieId.value_counts().rename("rating_count")```, and then merge movies dataframe & rating_counts series using outer join with the left dataframe on movieId & the right series on its index.
6. Use the previous dataframe you created to select the movies with no ratings.
