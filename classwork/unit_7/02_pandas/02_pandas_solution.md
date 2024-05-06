## Solutions Exercise 2 (Day 2)



9.  Calculate the total "Number of Reviews" & average Price for each "weight", "os", and "os_bit" combination.

```
laptop_df.groupby(['weight', 'os', 'os_bit']).agg(
    {'Number of Reviews': 'sum', 'Price': 'mean'}
)
```

10. Calculate the mean Price for each "brand" and subtract it from the individual laptop price to obtain:
    
    the price deviations => laptop price - the price corresponding to the mean of the laptop's brand

    **Hint:** for the second part (after the minus) check the function "groupby transform", you are going to need it. Check the documentation to learn about it.

```
laptop_df.Price - laptop_df.groupby(['brand']).Price.transform('mean')
```

11. Calculate the "weighted average" of laptop prices based on the "Number of Ratings" for each "brand"
    
    **Hints: **

    a. First, do a group by "brand" ```laptop_df.groupby('brand')```
    b. Take a look at the groups  ```laptop_df.groupby('brand').groups.keys() # list group keys```
    c. Yoy may check what data you have for each group to identify which columns you need to calculate the "weighted average" ```laptop_df.groupby('brand').get_group('ASUS')```

       That will give you a dataframe for the brand ASUS.

    d. You will probably need to write a function (you may call it weighted_average) that receives a group as a parameter and calculates the average price but weighted by the "Number of Ratings'.
    
       Check the function np.average and you will see there is an option for the weight.
    
    e. Once you have your function, you just need to apply that function after the the group by ```laptop_df.groupby('brand').apply(weighted_average)```

```
laptop_df.groupby('brand').groups.keys()
laptop_df.groupby('brand').get_group('ASUS')

def weighted_average(group):
    return np.average(group['Price'], weights=group['Number of Ratings'])
    
laptop_df.groupby('brand').apply(weighted_average, include_groups=False)
```


12. Calculate the percentage of laptops with "16 GB" RAM for each "brand" and "ram_type" combination.

```
def ram_percentage(group):
    return (group['ram_gb'] == '16 GB').mean() * 100

laptop_df.groupby(['brand', 'ram_type']).apply(ram_percentage, include_groups=False)
```

13. Calculate minimum and maximum ratings and the difference between those ratings for each "processor_brand" & "processor_name" combination.

    The difference betweeen two numbers is an easy operation. Instead of creating a function to do that, try using lambda.

    For example, ```lambda x: x.max() - x.min()```, which means perform that operation for each row in the dataframe.

    In case you need to rename columns at some point, here is the code:

    ```df.rename(columns={"A": "a", "B": "c"})```
    
```
laptop_df.groupby(['processor_brand', 'processor_name']).agg({'rating': ['min', 'max', lambda x: x.max() - x.min()]})
```

14. Calculate the total number of ratings for each "brand" and "processor_name" combination for laptops that have NO "warranty".

```
laptop_df[laptop_df['warranty'] == 'No warranty'].groupby(['brand', 'processor_name'])['Number of Ratings'].sum()
```
    
15. Group laptops by "brand" and "processor_name", and calculate the percentage of each laptop's price compared to the maximum price within the corresponding (brand - processor_name) group. Use transform for this question.

```
brand_max_price = laptop_df.groupby(['brand', 'processor_name'])['Price'].transform('max')
(laptop_df['Price'] / brand_max_price) * 100
```

