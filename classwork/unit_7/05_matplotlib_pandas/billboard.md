## Exercise 1

1. Use the billboard.csv data.
2. Save the data in a df and parse the date column as date.
   
   ```df_billboard = pd.read_csv("billboard.csv", parse_dates=["date"])```
3. Use matplotlib theme ggplot.
4. Make a horizontal bar chart to show the top ten artists from the billboard data set with the number of weeks they have spent at number one where rank is one (#1). 
5. Figure size 8x6.
6. Add the x-axis label.
7. The bars should have a black edge with a width of 2.


## Exercise 2

1. Use the billboard.csv data.
2. Replicate the following chart.
3. Create a line plot that shows the performance (rank) of the following songs:
   - All I Want For Christmas Is You by Mariah Carey
   - Rockin' Around The Christmas Tree by Brenda Lee
   - Jingle Bell Rock by Bobby Helms
4. The date range spans from 2016-12-25 to 2021-01-01

Hints:

- Select data in the date range ```df_billboard[df_billboard["date"].between("2016-12-25", "2021-01-01")]```
  
- Invert y axis
```plt.gca().invert_yaxis()```

![image](https://github.com/novillo-cs/softdev_material/assets/123229891/845ec510-9ef1-40d7-b049-192313cdf432)
