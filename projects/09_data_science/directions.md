# Unit 7: Data Science Project

### Due date:

Tuesday, May 21 at 10:00 pm.

## Specifications

- You may work solo or with a parner.
- You must create a private repo for this project and add your partner and the teacher as colaborators.
- You must use Pandas and Matplotlib.
- You must work on a Python notebook.
- You must add a readme file with your name and your partner's name. If you forget about this, I will take points off.
  
## Regression

You will calculate a few regressions, so let's define what is a regression:

A regression is a technique used to model the relationship between a dependent variable and one or more independent variables. It helps in understanding how the value of the depent variable changes when one or more independent variables are varied.

## Directions

1. Read the file airlines.xlsx in a dataframe ```df_data```.
2. Clean the data in ```df_data```. This means remove all rows that have at least one empty value.
4. Write a line of code to double check you do not have any null values in ```df_data```.
5. Convert the columns that store date and time from string (object) to data and time respectively.
6. Add the following columns to ```df_data```: 'Journey_day', 'Journey_month', 'Journey_year', 'Dep_Time_hour', 'Dep_Time_minute', 'Arrival_Time_hour', 'Arrival_Time_minute' and fill it with the corresponding data.
7. Create a new column 'dep_description' where depature time between:
  - 4am and 8am returns "Early Morning"
  - between 8am and 12pm return "Morning"
  - between 12pm and 4pm return "Noon"
  - between 4pm and 8pm return "Evening"
  - between 8pm and 12am return "Nigth"
  - between 12 am and 4am return "Late Night"
8. Build a bar chart where the x-axis represents the 'dep_description' and the y-axis the corresponding number of flights.
9. Create 3 new columns: 'Duration_hours', 'Duration_mins' and 'Duration_total_mins'.
10. Build a scatter plot with x-axis: 'Duration_total_mins' and y-axis 'Price'.
11. Let's add a simple regression line on top of the chart you created on number 10. For this regression use: ```numpy.polyfit with degree 1```
    Analyze the result (relationship between variables) and write your comments about it.
12. Build a scatter plot with x-axis 'Duration_total_mins' and y-axis 'Price', but add different colors for the different stops. Analyze the result and write your comments about it.
13. Determine which route Jet Airways is the most used (write yor answer on the notebook). Create a bar chart with these most used routes (for Jet Airways) in descending order: x-axis must represent the routes, and y-axis must represent the number of routes.
14. Another regression (a little bit more challenging) is coming on Monday...
