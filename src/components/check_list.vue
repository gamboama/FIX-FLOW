<script setup>
import { ref } from 'vue';

const options = ref(["N. Factura", "Cliente", "Fecha"]);
</script>

<template>
    <section class="container">
        <nav class="search-bar">
            <form action="" class="search-form">
                <select id="searchOption">
                    <option v-for="option in options" :key="option">
                        {{ option }}
                    </option>
                </select>
                <input type="text">
                <button type="submit">Buscar</button>
            </form>
        </nav>
    </section>
</template>

<style scoped>
*{
    all: unset;
}

.container{
    display: flex;
    flex-direction: column;
    align-items: center;
}
.search-bar{
    background-color: rgb(54, 54, 54);
    padding: 10px;
    width: 50%;
    height: auto;
    padding: 20px 50px;
    margin-top: 20px;
    border-radius: 40px;
}
.search-form{
    display: flex;
    justify-content: space-around;
}
.search-form *{
    border: 2px solid red;
}
.search-form select{
    background-color: white;
    padding: 5px 10px; 
}
</style>
