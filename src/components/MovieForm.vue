<script setup>
  import { ref, onMounted } from "vue";
  let csrf_token = ref("");
  let FlashMessage = ref("");
  let danger = ref(false);
  let success = ref("");
  onMounted(() => {
    getCsrfToken();
  });

  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      })
    }

  function saveMovie() {
  let movieForm =document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
      }
    })
    .then(function (response) {
    return response.json();
    })
    .then(function (data) {
      if(data.errors){
        FlashMessage.value = data.errors;
        danger.value = true;
        clearFormData();
         
      }
      if (data.data){
        FlashMessage.value = "Movie Added Successfully!";
         success.value = true;
         danger.value = false;
         clearFormData();
         console.log(data);
         
      }
    
    })
    .catch(function (error) {
      console.log(error);
    });
    }
    function clearFormData(){
       var data = document.querySelectorAll('input');
       data.forEach(input => input.value='');
    }
  
</script>

<template>
  <div class = "formbox">
    <div v-if="success" class = "alert alert-success">{{FlashMessage}}</div>
    <div v-if ="danger" class = "alert alert-danger"> 
      <li v-for= "d in FlashMessage">{{d}}</li>
    </div>
    
    <form id = "movieForm" @submit.prevent="saveMovie">

    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="formcontrol" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <input type="text" name="description" class="formcontrol" />
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" class="formcontrol" />
    </div>

    <div class="form-group mb-3">
      <button type="submit"  class="btn btn-primary mb-3" >Submit</button>
    </div>


    </form>
  </div>
</template>



<style>
/* Add any component specific styles here */
</style>