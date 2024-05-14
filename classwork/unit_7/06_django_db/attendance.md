# Django, db, pandas & matplotlib

# Part 1

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

3. Create a django project ```attendance```
4. Create an app ```daily_attendance```
5. Create a model for a table ```daily_attendance```
6. Inside the foder where you have your django project, you must create a ```notebooks``` folder:
   
   ![image](https://github.com/novillo-cs/softdev_material/assets/123229891/55d2db48-b68c-4570-9356-03ebfbb52bde)


8. Create a new notebook inside the ```notebooks``` folder to start working, add these lines to import django to the notebook:
   ```
   import django
   os.chdir("..")
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance.settings')
   os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true" 
   django.setup()
   ```

   **IMPORTANT: ** This ```os.chdir("..")``` smust be executed once because it changes the directory. If by any reason you need to run it again, you must reset the notebook and then execute it.
   
9. In  your notebook, read the attendance csv with pandas
10. Using a dataframe insert the data in the database
   
   **Hints:**

   - Use bulk_create
   - This could be useful to have the data from the df saved in the db: ```df_attendance.to_dict('records')```
   - Use batch_size. If working on lisa batch_size=100, if working on your own pc try batch_size=1000
     
## Part 2

Use the df_join explained in class and work on the following exercises:

1. Create a ```df_insert```. It must contain any new records that were not found in the database.
2. Write a few lines of code to insert the data from ```df_insert``` to the database.
3. Create a ```df_update```. It must contain the records that should be updated in the database.
2. Write a few lines of code to update the records in the database with the new values from ```df_update```.
