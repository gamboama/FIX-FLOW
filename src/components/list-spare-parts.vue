<script setup>
import { ref } from "vue";
const optionsSp = ref(["Pantallas", "Pachas", "Baterias"]);
</script>

<template>
  <div id="container">
    <form id="Search-Form">
      <select name="" id="Search-Bar">
        <option id="Search-Option" v-for="i in optionsSp" :key="i">
          {{ i }}
        </option>
      </select>
      <div id="box">
        <input type="text" placeholder="Buscar..." />
        <a href="#">
          <ion-icon
            name="search-circle-outline"
            class="fas fa-solid"
            style="font-size: 30px"
          ></ion-icon>
        </a>
      </div>
      <button type="submit">Buscar</button>
    </form>
  </div>
</template>

<style scoped>
* {
  all: unset;
}
#container {
  background-color: rgb(255, 255, 255);
  position: relative;
  width: 62%;
  height: 500px;
  border-radius: 10px;
  display: flex;
  overflow: hidden;
}
#Search-Bar {
  background-color: rgb(0, 0, 0);
  padding: 10px;
  width: 50%;
  height: auto;
  padding: 20px 50px;
  margin-top: 20px;
  border-radius: 40px;
}
#Search-Form {
  display: flex;
  justify-content: space-around;
}
#box {
  justify-content: center;
  width: 400px;
  height: 30px;
  display: flex;
  cursor: pointer;
  padding: 10px 20px;
  background: #fff;
  border-radius: 30px;
  align-items: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}

#box:hover input {
  width: 400px;
}

#box input {
  width: 0px;
  outline: none;
  border: none;
  font-weight: 500;
  transition: 0.8s;
  background: transparent;
}

#box a .fas {
  color: rgb(216, 75, 23);
  font-size: 18px;
}
</style>
