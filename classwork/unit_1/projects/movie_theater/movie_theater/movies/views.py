from django.shortcuts import render
from django.http import HttpResponse

import datetime
# Create your views here.

def index(request):
   #return HttpResponse("Hello, world. You're at the movies index.")
   print("Hey!!! You are in the movie index view now.")
   title_page = "Movie Index"
   movie_list = [
       {"name": "Movie 1", "show": True},
       {"name": "Movie 2", "show": False},
       {"name": "Movie 3", "show": True},
       {"name": "Movie 4", "show": False}]
   
   return render(request, "movies/index.html",
                 context={'title_page': title_page,
                          'movie_list': movie_list})
  
  
# Setting up cookies
# def cookies(request):
#     response = render(request, "movies/cookies.html")
#     response.set_cookie(key="Hi", value="Bonjour")
#     response.set_cookie(key="Bye", value="Au revoir")
#     return response


def cookies(request):
   dico_cookies = request.COOKIES
   visit_nbr = 0
   if 'visit_nbr' in dico_cookies:
       try:
           visit_nbr = int(dico_cookies['visit_nbr']) + 1
       except:
           visit_nbr = 1
   else:
       visit_nbr = 1
   response = render(request, "movies/cookies.html",
                     context={'visit_nbr': visit_nbr})
   response.set_cookie(key="visit_nbr", value=visit_nbr)
#    response.set_cookie(key="visit_nbr", value=visit_nbr,
#                        max_age=datetime.timedelta(seconds=10))
#    response.set_cookie(key="visit_nbr", value=visit_nbr,
#                        expires=datetime.datetime(2023, 10, 2, 14, 5))


   return response
