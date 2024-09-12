<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
const isActive = (path) => router.path
</script>

<template>
    <section class="container">

    </section>
</template>

<style scoped>
.container {
  background-color: rgb(255, 255, 255);
  position: relative;
  width: 62%;
  height: 500px;
  border-radius: 10px;
  display: flex;
  overflow: hidden;
}</style>