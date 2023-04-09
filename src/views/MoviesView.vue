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
  <h2>Movies</h2>
  <div class="moviecontainer">
    
    <div class = "movie" v-for="m in movies">
      <div class = "poster">
        <img :src="m.poster" alt = "poster" />
      </div>

      <div class = "info">
        <h1>{{m.title}}</h1>
        <p>{{m.description}}</p>
      </div>

    </div>
  </div>
</template>

<style>
  .moviecontainer{
    display:flex;
    flex-wrap:wrap;
    justify-content:space-evenly;
    
}
h1,p{
  padding:10px;
}
h2{
  padding:20px;
}
.poster{
  flex: 0 0 40%;
}

img{
    width: 100%;
    height: 100%;
     
}
.movie{
  display:flex;
  flex-direction:row;
  width:30%;
  height:10%;
  border: 2px;
  box-shadow: 0 0 6px;
  border-radius: 8px;
  padding: 20px;
  justify-content: center;
}
 
</style>

