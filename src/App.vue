<script setup>
import principal from "./components/principal.vue";
</script>

<template>
  <section class="body">
    <principal></principal>
    <section>
      <router-view></router-view>
    </section>
    
  </section>
</template>

<style scoped>
*{
  font-family: "Roboto Mono", monospace;
}
.body{
  background-color: rgba(50, 116, 50, 0.548);
  display: grid;
  grid-template-columns: 10% 90%;
  grid-template-rows: 100%;
  position: fixed;
  left: 10px;
  right: 10px;
  top: 10px;
  bottom: 10px;
}
section{
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
