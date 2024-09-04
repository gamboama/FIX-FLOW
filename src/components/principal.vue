<script></script>

<template>
  <nav>
    <router-link to="/users" class="router">Usuario</router-link>
    <router-link to="/tec" class="router">Tecnicos</router-link>
    <router-link to="/phones" class="router">Celulares</router-link>
    <router-link to="/spareparts" class="router">Repuestos</router-link>
  </nav>
</template>

<style scoped>
nav{
  background-color: rgb(3, 43, 10);
  display: flex;
  flex-direction: column;
  padding: 10px;
  height: 100%;
  width: 100%;
}
.router{
  color: white;
  margin: 10px 0;
  text-decoration: none;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
</style>
