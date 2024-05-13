## Django, db, pandas & matplotlib

Save your work here: ```your_repo/unit_7/06_django_db/YOUR_FILES_HERE(CSV AND NOTEBOOK)```

1. Create a python environment
2. You need the following in your requirements:

```
nodeenv
pgadmin4
django-extensions
jupyter
pandas
matplotlib
```

3. Create a django project attendance
4. Create an app daily_attendance
5. Create a model for a table daily_attendance
6. Inside the django project you can create a notebooks folder
   
   ![image](https://github.com/novillo-cs/softdev_material/assets/123229891/55d2db48-b68c-4570-9356-03ebfbb52bde)


8. Create a new notebook to start working, add these lines to link django and the notebook:
   ```
   import django
   os.chdir("..")
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance.settings')
   os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true" 
   django.setup()
   ```
9. Read the attendance csv with pandas
10. Using a dataframe insert the data in the database
   
   **Hints:**

   - Use bulk_create
   - This could be useful to have the data from the df to save it in the db ```df_attendance.to_dict('records')```
   - Use batch_size. If working on lisa batch_size=100, if working on your on pc try batch_size=1000
     
