## Exercise 1

Save your work here: ```your_repo/unit_7/05_matplotlib_pandas/la_liga/YOUR_FILES_HERE```

1. Find the 5 teams that had the most "Red Cards".
2. Find the average number of "Long passes" made by each Position (Goalkeeper, Forward, etc).
3. Find the 10 Shirt numbers that scored the most goals.
4. Use agg to create a new dataframe that contains:
   - A "total" column containing the total "Shots" taken by each team (all the players for the team).
   - A "on_target" column containing the total "Shots on target" taken by each team.
   - An accuracy column "on_target" / "total".
   - It should look like the following dataframe (for all the teams in the dataset).
5. Using the new dataframe, create the following figure:

![image](https://github.com/novillo-cs/softdev_material/assets/123229891/d6844b7e-7d47-4d4a-b234-a55930f6f95d)


**Notes:**

- There are two charts in the figure (2 rows by 1 column)
- The top chart shows the top 5 most accurate teams (highest on-target shot pecentage)
- The bottom chart shows the 5 least accurate teams (lowest on-target shot pecentage)
- Both plots share the same x-axis ```sharex=True```
- Notice how the data is sorted within each plot.


![image](https://github.com/novillo-cs/softdev_material/assets/123229891/0ed37da7-82ee-4fc7-9629-1f6fa0962c97)
