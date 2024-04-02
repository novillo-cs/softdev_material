### MovieEdit.vue

- Import multiselect:

```import Multiselect from 'vue-multiselect'```


- Activate the component:

```
components: {
	VueDatePicker,
	Multiselect
  },
```

- Add the css (at the end of the file)

```<style src="vue-multiselect/dist/vue-multiselect.css"></style>```

- Data section should look like this:

```
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
```

- The actors field block should look like this:

```
<p>
    <label for="id_actors">Actors:</label>
    <select hidden name="actors" required="" id="id_actors" multiple="">
        <option v-for="actor in actor_list" :value="actor.id" selected=""></option>
    </select>
    <multiselect v-model="actor_list" :options="actor_list_source" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Choose the actors" label="name" track-by="name" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
        <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
    </multiselect>
   
</p>
```
