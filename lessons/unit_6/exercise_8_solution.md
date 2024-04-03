Button in your template:
```
        <button type="submit" class="btn btn-primary"
            @click.prevent="submit_form"
            :disabled="submitting_form">
            Submit
        </button>
```
Method to submit the JS form. Read, understand the following code, and **add the needed variables to the data section**.
```
        submit_form(){
            if (this.submitting_form === true) {
            return;
            }
            this.submitting_form = true
            var form = document.createElement('form');
            form.setAttribute('method', 'post');
            let form_data = {
                'csrfmiddlewaretoken': this.csrf_token,
                'name': this.movie_dico.name,
                'running_time': this.get_time_string,
                'director': this.movie_dico.director,
                'release_date': this.get_date_string,
            }
            console.log('actor_list', this.actor_list)
            console.log("form_data", form_data)
            for (var key in form_data) {
                var html_field = document.createElement('input')
                html_field.setAttribute('type', 'hidden')
                html_field.setAttribute('name', key)
                html_field.setAttribute('value', form_data[key])
                form.appendChild(html_field)
            }
            var actor_field = document.createElement('select')
            actor_field.setAttribute('name', 'actors')
            actor_field.setAttribute('id', 'id_actors')
            actor_field.setAttribute('multiple', '')
            for (var actor of this.actor_list) {
                console.log('actor', actor)
                var option_field = document.createElement('option')
                option_field.setAttribute('value', actor.id)
                option_field.setAttribute('selected', '')
                actor_field.appendChild(option_field)
            }
            form.appendChild(actor_field)
            document.body.appendChild(form);
            form.submit()
        },
```
