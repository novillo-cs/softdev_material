<template>
<a :href="this.movie_list_url">Movies list</a><br/>
<a :href="this.movie_update_url">Update Movie</a><br/>
<a :href="this.movie_delete_url">Delete Movie</a><br/>
<h1>{{ this.movie.name }}</h1>
Actors:<br/>
<span v-for="actor in this.movie.actors">
{{actor.name}}<br/></span>
<br/>
Running time: {{this.convert_time_to_string(this.movie.running_time)}}<br/>
Director: {{this.movie.director}}<br/>
Release date: {{this.convert_date_to_string(this.movie.release_date)}}<br/>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data: function() {
      return {
        movie_error: [],
        movie_id: ext_movie_id,
        movie_detail_js_url: ext_movie_detail_js_url,
        movie_list_url: ext_movie_list_url,
        movie_update_url: ext_movie_update_url,
        movie_delete_url: ext_movie_delete_url,
        movie: {}
    }},
    methods: {
        get_movie_info(){
            fetch(this.movie_detail_js_url,
                {
                    method: "get",
                    credentials: 'same-origin'
                }
            ).then(function(response) {
                console.log('response', response)
                return response.json()}).then(this.assign_movie).catch(
                    (error) => { 
                    console.log('error', error)
                    this.movie_error=["error when loading movie information"]
        })
        },
        assign_movie(movie_json) {
            console.log('json', movie_json)
            this.movie = movie_json['movie']
            this.movie.running_time = this.convert_string_to_time(
                this.movie.running_time)
            this.movie.release_date = this.init_date(
                this.movie.release_date
            )
        },
        convert_string_to_time(time_string) {
            return new Date("1970-01-01T" + time_string)
        },
        init_date(date_string){
            let dato = new Date(date_string)
            const offset = dato.getTimezoneOffset()
            dato = new Date(dato.getTime() + (offset*60*1000))
            return dato
        },
        convert_date_to_string(dato){
            if (dato) {
                const offset = dato.getTimezoneOffset()
                dato = new Date(dato.getTime() - (offset*60*1000))
                console.log('date', dato, dato.toISOString())
                return dato.toISOString().split('T')[0]
            }
        },
        convert_time_to_string(timo){
            if (timo) {
                return `${timo.getHours()} hours ${timo.getMinutes()} minutes`
            }
        }
    },
    computed: {
    },
    beforeMount() {
        this.get_movie_info()
    },
}
</script>