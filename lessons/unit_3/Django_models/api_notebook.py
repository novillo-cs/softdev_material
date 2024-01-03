# %%
import os
os.chdir("..")

# %%
import django
# In case that we need it later
#from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater.settings')
# This is for async, in case we are going to see it later (maybe)
#os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

# %%
import json
import http.client

# %%
conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "your key",
    'X-RapidAPI-Host': "imdb8.p.rapidapi.com"
}

conn.request("GET", "/auto-complete?q=game%20of%20thr", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

dico_data = json.loads(data.decode('utf-8'))


# %%
movie_id = dico_data['d'][2]["id"]
print(movie_id)

# %%
apikey="your key"
conn1 = http.client.HTTPSConnection("www.omdbapi.com")

# %%

conn1.request("GET", "/?apikey={apikey}&i={movie_id}&plot=full".format(
    apikey=apikey, movie_id=movie_id), headers=headers)

res = conn1.getresponse()
data = res.read()


# %% [markdown]
# 

# %%
data

# %%
