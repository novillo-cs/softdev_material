### Django (views.py):

```
class MovieUpdatebisView(View):
   def post(self, request, *args, **kwargs):
       movie = get_object_or_404(Movie, pk=self.kwargs["pk"])
       # Create a form instance with POST data
       form = MovieForm(request.POST, instance=movie)
       if form.is_valid():
           form.save()
           return JsonResponse({"success": True})
       else:
           return JsonResponse({"success": False, "errors": form.errors})
```

### Vue.js:

The template is the same as the last one, just change the function in the submit button:

```
<button type="submit" class="btn btn-primary"
      @click.prevent="submit_form_fetch"
      :disabled="submitting_form">
      Submit
</button>
```

Add these lines to display error or successful update:

```
<br><br>
	With fetch this time
	<br><br>
	<div v-if="form_error">
    	<ul>
        	<li v-for="(error, index) in form_error">
            	{{error}}
        	</li>
    	</ul>
	</div>
	<div v-if="form_updated">
    	{{ form_updated }}
	</div>
```

The data:

```
data: function() {
  	return {
    	csrf_token: ext_csrf_token,
    	update_bis_url: ext_update_bis_url,
    	form: ext_form,
    	movie_dico: ext_movie_dict,
    	actor_list_source: ext_actor_list,
    	date: this.init_date(ext_movie_dict.release_date),
    	time: this.init_time(ext_movie_dict.running_time),
    	actor_list: ext_movie_dict.actors,
    	submitting_form: false,
    	form_error: [],
    	form_updated: "",
	}},
```

And the methods:

```
submit_form_fetch(){
        	this.form_error = []
        	this.form_updated = ""
        	let formData = new FormData();
        	let form_data = {
            	'name': this.movie_dico.name,
            	'running_time': this.get_time_string,
            	'director': this.movie_dico.director,
            	'release_date': this.get_date_string,
        	}
        	for (var key in form_data) {
            	formData.append(key, form_data[key])
        	}
        	this.actor_list.map(dic => formData.append('actors', dic.id))
        	fetch(this.update_bis_url,
            	{
                	method: "post",
                	body: formData,
                	headers: {'X-CSRFToken': this.csrf_token},
                	credentials: 'same-origin'
            	}
        	).then(function(response) {
            	console.log('response', response)
            	return response.json()}).then(
            	this.handleResponse).catch(
                	(error) => {
                	console.log('error', String(error))
                	this.form_error=["error"]
    	})
    	},
    	handleResponse(response) {
        	console.log('json response', response)
        	if ('success' in response){
            	if (response['success'] == true) {
                	this.form_updated = "Movie has been updated"
            	} else {
                	if ('errors' in response){
                    	for (const [key, value] of Object.entries(response['errors'])) {
                        	for (const error of value) {
                            	this.form_error.push(`${key}: ${error}`)
                        	}
                    	}
                	} else {
                    	this.form_error=["Update failed - An error occurred but do not have more information about it"]
                	}
            	}
        	} else {
            	this.form_error=["Update failed - It has been an error on the form request"]
        	}
    	}
```
