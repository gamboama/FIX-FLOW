<script setup>
import celForm from './cel-form.vue';
</script>
<template>
    <section class="container">
        <celForm class="info-container" id="cels-container"></celForm>
        <div class="info-container" id="op-container">
            <nav class="op-nav">
                <a href="#" class="op-cel">
                    <ion-icon name="add-circle-outline"></ion-icon>
                </a>
                <a href="#" class="op-cel">
                    <ion-icon name="create-outline"></ion-icon>
                </a>
                <a href="#" class="op-cel">
                    <ion-icon name="trash-outline"></ion-icon>
                </a>
            </nav>
        </div>
        <div class="info-container" id="ic-container">
            <div class="info-cell-1">
                <h3>CONTEO DE CELULARES EN TURNO:</h3>
                <span>2</span>
            </div>
            <div class="info-cell-2">
                <h3>Ultimo celulares recibidos</h3>
                <ul>
                    <li>Celular 1</li>
                    <li>Celular 2</li>
                    <li>Celular 3</li>
                    <li>Celular 1</li>
                    <li>Celular 2</li>
                    <li>Celular 3</li>
                </ul>
            </div>
            <div class="info-cell-3">
                <h3>Celulares proximos a cumplir los 30 dias</h3>
                <ul>
                    <li>Celular 1</li>
                    <li>Celular 2</li>
                    <li>Celular 3</li>
                </ul>
            </div>
        </div>
    </section>
</template>
<style scoped>
.container {
    background-color: rgb(255, 255, 255);
    position: relative;
    width: 92%;
    height: 600px;
    border-radius: 10px;
    display: flex;
    overflow: hidden;
}

.info-container {
    height: 100%;
}

#cels-container {
    width: 75%;
    overflow: auto;
}

#op-container {
    width: 5%;
    background-color: rgb(36, 36, 36);
}

#ic-container {
    background-color: rgb(36, 36, 36);
    width: 20%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.info-cell-1 {
    padding: 15px;
    margin: 10px;
    border-radius: 40px;
    text-align: center;
    background-color: green;
}

.info-cell-1 h3 {
    font-size: 15px;
}

.info-cell-1 span {
    background-color: rgb(20, 71, 20);
    padding: 10px 30px;
    border-radius: 10px;
    color: white;
    height: 20%;
}

.info-cell-2 {
    height: 40%;
    margin: 10px;
    border-radius: 10px;
    background-color: rgb(97, 194, 113);
    overflow: hidden;

}

.info-cell-2 h3 {
    margin: unset;
    background-color: rgb(35, 75, 37);
    padding: 5px 10px;
    text-align: center;
    color: white;
}

.info-cell-2 ul {
    margin: unset;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 3px;
    padding: unset;
    overflow: auto;
    scrollbar-width: none;
}

.info-cell-2 ul li {
    background-color: rgba(165, 165, 165, 0.712);
    margin: unset;
    list-style: none;
    left: 0;
    padding: 10px;
}

.info-cell-3 {
    height: 40%;
    margin: 10px;
    border-radius: 10px;
    background-color: rgb(97, 194, 113);
    overflow: hidden;

}

.info-cell-3 h3 {
    margin: unset;
    background-color: rgb(35, 75, 37);
    padding: 5px 10px;
    text-align: center;
    color: white;
    font-size: 13px;
}

.info-cell-3 ul {
    margin: unset;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 3px;
    padding: unset;
    overflow: auto;
    scrollbar-width: none;
}

.info-cell-3 ul li {
    background-color: rgba(165, 165, 165, 0.712);
    margin: unset;
    list-style: none;
    left: 0;
    padding: 10px;
}
.op-nav{
    display: flex;
    flex-direction: column;
    padding: 10px;
    align-items: center;
    gap: 20px;
    justify-content: flex-start;
}
.op-cel{
    background-color: rgb(65, 65, 65);
    padding: 5px 10px;
    border-radius: 10px;
    color: white;
    font-weight: bolder;
    font-size: 25px;
    transition: transform .2s ease;
}
.op-cel:hover{
    transform: scale(1.1);
}
</style>