## Exercise 2

```Save your work here: your_repo/unit_7/02_pandas_laptops/YOUR_FILES_HERE(CSV AND NOTEBOOK)```

Day 1:

1. Store the data from the file laptops.csv in a dataframe.
2. Display the dataframe to check if the data is correct.
3. Calculate the average price for each processor_brand and brand.
4. Calculate the total number of laptops for each ram_type and warranty
5. Calculate the average rating for each os. Display only an index, the os column and a column 'average_rating'
6. Calculate the minimum laptop price for each warranty plan. Same thing as before, in a dataframe with warranty and minimin_price columns
7. Calculate the average number of reviews & price for laptops per touchscreen option and processor generation.
8. Calculate the maximum and minimum price for each SSD and HDD combination.

Day 2:

```Keep working here: your_repo/unit_7/02_pandas_laptops/YOUR_FILES_HERE(CSV AND NOTEBOOK)```

9.  Calculate the total "Number of Reviews" & average Price for each "weight", "os", and "os_bit" combination.
    
10. Calculate the mean Price for each "brand" and subtract it from the individual laptop price to obtain:
    
    the price deviations => laptop price - the price corresponding to the mean of the laptop's brand

    **Hint:** for the second part (after the minus) check the function "groupby transform", you are going to need it. Check the documentation to learn about it.

11. Calculate the "weighted average" of laptop prices based on the "Number of Ratings" for each "brand"
    
    **Hints: **

    a. First, do a group by "brand" ```laptop_df.groupby('brand')```
    b. Take a look at the groups  ```laptop_df.groupby('brand').groups.keys() # list group keys```
    c. Yoy may check what data you have for each group to identify which columns you need to calculate the "weighted average" ```laptop_df.groupby('brand').get_group('ASUS')```

       That will give you a dataframe for the brand ASUS.

    d. You will probably need to write a function (you may call it weighted_average) that receives a group as a parameter and calculates the average price but weighted by the "Number of Ratings'.
    
       Check the function np.average and you will see there is an option for the weight.
    
    e. Once you have your function, you just need to apply that function after the the group by ```laptop_df.groupby('brand').apply(weighted_average)```

12. Calculate the percentage of laptops with "16 GB" RAM for each "brand" and "ram_type" combination.

13. Calculate minimum and maximum ratings and the difference between those ratings for each "processor_brand" & "processor_name" combination.

    The difference betweeen two numbers is an easy operation. Instead of creating a function to do that, try using lambda.

    For example, ```lambda x: x.max() - x.min()```, which means perform that operation for each row in the dataframe.

    In case you need to rename columns at some point, here is the code:

    ```df.rename(columns={"A": "a", "B": "c"})```
    
14. Calculate the total number of ratings for each "brand" and "processor_name" combination for laptops that have NO "warranty".
    
15. Group laptops by "brand" and "processor_name", and calculate the percentage of each laptop's price compared to the maximum price within the corresponding (brand - processor_name) group.

