<script setup>
import { computed, ref } from "vue"; // Importado para usar propiedades computadas
import { useRoute } from "vue-router"; // Importado para obtener la ruta actual

const route = useRoute(); // Obtiene la ruta actual
const isActive = (path) => route.path.startsWith(path);
</script>

<template>
  <nav>
    <router-link
      to="/users"
      class="router"
      :class="{ active: isActive('/users') }"
      >Usuario</router-link
    >
    <router-link to="/tec" class="router" :class="{ active: isActive('/tec') }"
      >Tecnicos</router-link
    >
    <router-link
      to="/phones"
      class="router"
      :class="{ active: isActive('/phones') }"
      >Celulares</router-link
    >
    <router-link
      to="/spareParts"
      class="router"
      :class="{ active: isActive('/spareParts') }"
      >Repuestos</router-link
    >
  </nav>
</template>

<style scoped>
nav {
  background-color: rgb(216, 75, 23);
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}
.router {
  color: white;
  padding: 20px;
  text-decoration: none;
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
  transition: all 0.3s ease;
}

.router.active {
  background-color: white;
  color: black;
  transform: translateX(5px);
  box-shadow: -5px 5px 5px rgba(0, 0, 0, 0.418);
}
</style>
