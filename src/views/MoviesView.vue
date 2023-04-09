<script setup>
import { ref, onMounted } from "vue";
let movies = ref([]);
 
   
  onMounted(() => {
    fetch("/api/v1/movies", {method: 'GET'})
    .then((response) => response.json())
    .then((data)=>{
      movies.value = data.movies
    }) 
    .catch((error)  => console.log(error))
  })
</script>

   

<template>
  <div class="moviecontainer">
    <h2>Movies</h2>
    <div class = "card" v-for="m in movies">
     <img :src="m.poster" alt = "poster" />
    <h1>{{m.title}}</h1>
    <p>{{m.description}}</p>
    </div>
  </div>
</template>

<style>
</style>

