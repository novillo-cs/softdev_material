## Exercise 1

1. Use the billboard.csv data.
2. Save the data in a df and parse the date column as date.
   
   ```df_billboard = pd.read_csv("billboard.csv", parse_dates=["date"])```
3. Use matplotlib theme ggplot.
4. Make a horizontal bar chart to show the top ten artists from the billboard data set with the number of weeks they have spent at number one where rank is one (#1). 
5. Figure size 8x6.
6. Add the x-axis label.
7. The bars should have a black edge with a width of 3.
