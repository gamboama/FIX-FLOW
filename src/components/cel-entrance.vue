<script setup>
</script>
<template>
    <section class="container">
        <form class="cel-form">
            <h2>Ingreso de facturas</h2>
            <label for="in-client-name" class="in-container">
                <span>Nombre Cliente: </span>
                <input type="text" id="in-client-name">
            </label>
        </form>
        <section class="cells-container">
            a
        </section>
    </section>

</template>
<style scoped>
.container{
    all: unset;
    display: flex;
    background-color: aqua;
    height: 90%;
    width: 90%;
    gap: 20px;
    padding: 10px;
}
.cel-form{
    border: 2px solid red;
    width: 80%;
    padding: 10px 30px;
    display: grid;
}

.in-container {
    background-color: gray;
    padding: 20px;
    margin-top: 30px;
}
</style>