*************************************************************************************************************
Exercise 3:

At some point, it would be great if we recreate the form field by field in Vue.js. But for the moment, let's define the movie object as a dictionary in Vue, as well as the actor list (for the multiple choice).

Let's think about a way to do it and implement it.

Hint: Three files should be modified:

movies/views.py => class MovieUpdateView(UpdateView)
Movies_form.html
MovieEdit.vue

*************************************************************************************************************

Solution:

In views.py:

```
class MovieUpdateView(UpdateView):
   model = Movie
   form_class = MovieForm

   def form_valid(self, form):
       response = super().form_valid(form)
       messages.add_message(
           self.request,
           messages.SUCCESS,
           'Movie "{movie_name}" has been updated'.format(
               movie_name=self.object.name
           ),
       )
       return response

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       movie_dico = model_to_dict(self.object)
       movie_dico["running_time"] = movie_dico["running_time"].strftime(
           "%H:%M:%S"
       )
       movie_dico["release_date"] = movie_dico["release_date"].strftime(
           "%Y-%m-%d"
       )
       actors = movie_dico["actors"]
       movie_actor_list = []
       for actor in actors:
           movie_actor_list.append({"id": actor.id, "name": actor.name})
       movie_dico["actors"] = movie_actor_list
       actor_list = list(Actor.objects.all().values())
       context["movie_dict"] = movie_dico
       context["actor_list"] = actor_list
       print("context", context)
       return context

   # comment the following line to show the error about not having an
   # success_url
   def get_success_url(self):
       return reverse_lazy("movies:movie_detail", args=[self.object.id])
       # you can also use it this way with kwargs, just to let you know
       # but here we have only one argument, so no mistake can be done
       # return reverse_lazy("movies:actor_detail",
       #                    kwargs={'pk':self.object.id})


```

In the template:

```
{% block js %}
  {{ block.super }}
  <script>
       var ext_csrf_token = '{{ csrf_token }}'
       var ext_form = `{{ form.as_p | safe}}`
       var ext_movie_dict = {{ movie_dict | safe }}
       var ext_actor_list = {{ actor_list | safe }}
  </script>
  {% vite_hmr_client %}
  {% vite_asset 'src/apps/movie_edit/movie_edit.js' %}
{% endblock js %}
```

In MovieEdit.vue:

```
data: function() {
  	return {
    	csrf_token: window.ext_csrf_token,
    	form: window.ext_form,
    	movie_dico: window.ext_movie_dict,
    	actor_list: window.ext_actor_list,
	}},
```
*************************************************************************************************************






