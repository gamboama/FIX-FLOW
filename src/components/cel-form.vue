<script setup>
</script>
<template>
    <section class="form-container">
        <form class="client-form">
            <div class="input-container">
                <label for="name-input">
                    <ion-icon name="people-outline"></ion-icon>
                </label>
                <input type="text" placeholder="Nombre Cliente" id="name-input">
            </div>
            <div class="input-container">
                <label for="tel-num">
                    <ion-icon name="call-outline"></ion-icon>
                </label>
                <input type="text" placeholder="Numero de Telefono" id="tel-num">
            </div>
            <div class="input-container">
                <label for="cel-num">
                    <ion-icon name="call-outline"></ion-icon>
                </label>
                <input type="number" value="1" min="1" max="5" id="cel-num">
            </div>
            <button class="nxt-btn">Siguiente</button>
        </form>
        <h3>Celular: 1</h3>
        <form class="cel-form">
            <div id="kind-container">
                <label for="kind-op">Tipo:</label>
                <select id="kind-op" name="kind-op">
                    <option value="opcion1">Celular Android</option>
                    <option value="opcion2">Celular Iphone</option>
                    <option value="opcion3">Bafle</option>
                    <option value="opcion4">SmartWatch</option>
                    <option value="opcion5">Tablet</option>
                    <option value="opcion6">Ipad</option>
                    <option value="opcion7">Otro</option>
                </select>
                <ion-icon name="chevron-down-outline"></ion-icon>
            </div>
            <div id="mark-container">
                <label for="mark-op">Marca:</label>
                <select id="mark-op" name="mark-op">
                    <option value="opcion1">Samsung</option>
                    <option value="opcion2">Iphone</option>
                    <option value="opcion3">Motorola</option>
                    <option value="opcion4">Huawei</option>
                    <option value="opcion5">Redmi</option>
                    <option value="opcion6">Otro</option>
                </select>
                <ion-icon name="chevron-down-outline"></ion-icon>
            </div>
            <div id="model-container">
                <label for="model-input">Modelo:</label>
                <input type="text" id="model-input" placeholder="Ej: A14">
            </div>
            <div id="desc-container">
                <label for="desc-input">Descripcion y anotaciones mantenimiento:</label>
                <textarea  id="desc-input" placeholder="Ej: Cambio de pantalla."></textarea>
            </div>
            <div id="price-container">
                <label for="price-input">Precio:</label>
                <input type="number" value="50000" min="0">
            </div>

            <button class="nxt-btn">Siguiente</button>
        </form>
        <form class="end-form">
            <h3>Total del pago: $$$$$$</h3>
            <div id="due-container">
                <label for="due-input">
                    <ion-icon name="cash-outline"></ion-icon>
                    <span>Abono: </span>
                </label>
                <input type="number" value="0" min="0">
            </div>
            <button class="nxt-btn" id="get-btn">Ingresar</button>
        </form>
    </section>


</template>
<style scoped>
.form-container {
    padding: 0 20px;
}

.client-form {
    display: flex;
    gap: 10px;
    justify-content: space-around;
    margin-top: 20px;
    padding: 20px 10px;

}

.input-container {
    border-radius: 30px;
    padding: 7px 12px;
    display: flex;
    align-items: center;
    background-color: rgb(192, 192, 192);
}

.input-container label {
    margin-right: 10px;
}

.input-container input {
    all: unset;
}

.nxt-btn {
    all: unset;
    background-color: rgb(20, 71, 20);
    padding: 10px 30px;
    color: white;
    font-weight: bolder;
    border-radius: 20px;
    height: 30px;
    transition: all .3s ease;
}
.nxt-btn:hover{
    background-color: rgb(35, 151, 35);
    transform: scale(1.1);
}

.cel-form {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: 20px;
    padding: 10px;
    background-color: gray;
    font-weight: bold;
}
#kind-container{
    grid-column: 1/2;
    background-color: rgb(192, 192, 192);
    border-radius: 10px;
    padding: 5px 10px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}
#kind-container select{
    all:unset;
}
#mark-container{
    grid-column: 2/3;
    background-color: rgb(192, 192, 192);
    border-radius: 10px;
    padding: 5px 10px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}
#mark-container select{
    all:unset;
}
#model-container{
    grid-column: 3/4;
    background-color: rgb(192, 192, 192);
    border-radius: 10px;
    padding: 5px 10px;
    display: flex;
    align-items: center;
    justify-content: space-around;
}
#model-container input{
    all: unset;
    padding-left: 10px;
}
#desc-container{
    grid-column: 1/3;
    grid-row: 2/4;
    background-color: rgb(192, 192, 192);
    padding: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
#desc-container textarea{
    width: 90%;
    height: 100%;
    text-align: start;
    border: none;
    padding: 10px;
    margin-top: 10px;
}
#price-container{
    grid-column: 3/4;
    background-color: rgb(192, 192, 192);
    border-radius: 10px;
    padding: 5px 10px;
    display: flex;
    align-items: center;
    justify-content: space-around;
}
#price-container input{
    all: unset;
    padding-left: 10px;
}
.end-form{
    display: flex;
    padding: 10px ;
    margin-top: 10px;
    justify-content: space-around;
    align-items: center;
}
#due-container{
    background-color: rgb(192, 192, 192);
    border-radius: 10px;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: space-around;
}
#due-container input{
    all: unset;
    padding-left: 10px;
}
#due-container label span{
    margin-left: 5px;
}
</style>