MovieEdit.vue

```
<template>
    <div>
        This is the page where we are going to edit movie in vuejs, this is cool
        This is the form coming from django, displayed in vue
    </div>
    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Name:</label>
                <input type="text" name="name" value="Matrix" maxlength="100" required="" id="id_name">
            </p>
            <p>
                <label for="id_running_time">Running time:</label>
                <input type="hidden" name="running_time" :value="get_time_string" required="" id="id_running_time">
                <VueDatePicker style="display:inline-block;width: 150px;padding-bottom:10px;padding-left:10px" v-model="time" :time-picker="true" enable-seconds></VueDatePicker>
            </p>
            
            <p>
                <label for="id_actors">Actors:</label><br>
                <select name="actors" required="" id="id_actors" multiple="">
                    <option value="2">Carrie-Anne Moss</option>
                    <option value="1" selected="">Keanu Reeves</option>
                </select>
            </p>
            <p>
                <label for="id_director">Director:</label>
                <input type="text" name="director" value="The Wachowskis" maxlength="200" required="" id="id_director">
            </p>
            <p>
                <label for="id_release_date">Release date:</label>
                <input type="hidden" name="release_date" :value="get_date_string" required="" id="id_release_date">
                <VueDatePicker style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px" v-model="date" :enable-time-picker="false"></VueDatePicker>
            </p>
                <button type="submit" class="btn btn-primary">
                    Submit
                </button>                    
        </form>
    </div>
    <br><br>
    
</template>

<script>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'App',
  components: {
    VueDatePicker,
  },
  data: function() {
      return {
        csrf_token: ext_csrf_token,
        form: ext_form,
        movie_dico: ext_movie_dict,
        actor_list_source: ext_actor_list,
        date: this.init_date(ext_movie_dict.release_date),
        time: this.init_time(ext_movie_dict.running_time),
        actor_list: ext_movie_dict.actors
    }},
    methods: {
        convert_date_to_string(dato){
            const offset = dato.getTimezoneOffset()
            dato = new Date(dato.getTime() - (offset*60*1000))
            console.log('date', dato, dato.toISOString())
            return dato.toISOString().split('T')[0]
        },
        init_date(date_string){
            let dato = new Date(date_string)
            const offset = dato.getTimezoneOffset()
            dato = new Date(dato.getTime() + (offset*60*1000))
            return dato
        },
        init_time(time_string){
            let time_split = time_string.split(':')
            return {
                'hours': time_split[0],
                'minutes': time_split[1],
                'seconds': time_split[2]
            }
        },
    },
    computed: {
        get_date_string() {
            if (this.date == null) {
                return ""
            } else {
                return this.convert_date_to_string(this.date)
            }
        },
        get_time_string(){
            if (this.time == null) {
                return ""
            } else {
                return `${this.time.hours}:${this.time.minutes}:${this.time.seconds}`
            }
        }
    }
}
</script>
```
