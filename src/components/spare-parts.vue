<template>
  <div class="container">
    <div class="limite">
      <div class="box">
        <input type="text" placeholder="Buscar..." />
        <a href="#">
          <ion-icon name="search-circle-outline" class="fas fa-solid" style="font-size: 30px;"></ion-icon>
        </a>
      </div>
      <table class="tabla">
        <thead>
          <tr>
            <th>Dispositivos</th>
            <th>Categoria</th>
            <th>Unidades Disponibles</th>
            <th></th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Iphone 12</td>
            <td>pachas</td>
            <td class="num">3</td>
            <td>
              <ion-icon name="add-outline" class="iconoe"></ion-icon>
            </td>
            <td>
              <ion-icon name="remove-outline" class="iconob"></ion-icon>
            </td>
          </tr>
          <tr>
            <td>Samsung A22</td>
            <td>pachas</td>
            <td class="num">1</td>
            <td>
              <ion-icon name="add-outline" class="iconoe"></ion-icon>
            </td>
            <td>
              <ion-icon name="remove-outline" class="iconob"></ion-icon>
            </td>
          </tr>
          <tr>
            <td>Iphone 11</td>
            <td>Pantallas</td>
            <td class="num">2</td>
            <td>
              <ion-icon name="add-outline" class="iconoe"></ion-icon>
            </td>
            <td> 
              <ion-icon name="remove-outline" class="iconob"></ion-icon>
            </td>
          </tr>
          <tr>
            <td>Redmi 9</td>
            <td>Pantallas</td>
            <td class="num">5</td>
            <td>
              <ion-icon name="add-outline" class="iconoe"></ion-icon>
            </td>
            <td>
              <ion-icon name="remove-outline" class="iconob"></ion-icon>
            </td>
          </tr>
          <tr>
            <td>Iphone 12</td>
            <td>Baterias</td>
            <td class="num">0</td>
            <td>
              <ion-icon name="add-outline" class="iconoe"></ion-icon>
            </td>
            <td>
              <ion-icon name="remove-outline" class="iconob"></ion-icon>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <div class="contenedor">
        <div class="circulo">
          <ion-icon name="add-outline" class="logos"></ion-icon>
        </div>
        <h2 class="text">Nueva Categoria</h2>
      </div>
      <div class="contenedor">
        <div class="circulo">
          <ion-icon name="add-outline" class="logos"></ion-icon>
        </div>
        <h2 class="text">Añadir Repuesto</h2>
      </div>
      <div class="contenedor">
        <div class="circulo">
          <ion-icon name="create-outline" class="logos"></ion-icon>
        </div>
        <h2 class="text">Actualizar Repuesto</h2>
      </div>
      <div class="contenedor">
        <div class="circulo">
          <ion-icon name="trash-outline" class="logos"></ion-icon>
        </div>
        <h2 class="text">Borrar Categoria</h2>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 2fr 1fr;
  background-color: rgb(255, 255, 255);
  padding: 10px 20px;
  border-radius: 10px;
}

.tabla {

  margin: 20px;
  background-color: gray;
  color: white;
  font-size: 20px;
  table-layout: fixed;
  border-collapse: collapse;
}

.limite {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

thead {
  background: rgba(140, 243, 190, 0.4);
}

th {
  padding: 20px 15px;
  font-weight: 700;
  text-transform: uppercase;
}

td {
  padding: 15px;
  border-bottom: solid 1px rgba(255, 255, 255, 0.2);
}

.num {
  text-align: center;
}

tbody tr:hover {
  background: rgba(140, 213, 190, 0.4);
}

.iconoe {
  padding: 5px;
  width: 20px;
  height: 20px;
  background-color: yellow;
}

.iconob {
  padding: 5px;
  width: 20px;
  height: 20px;
  background-color: rgb(255, 0, 0);
}

.circulo {
  margin: 25px;
  background-color: gray;
  width: 120px;
  height: 120px;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logos {
  width: 55px;
  height: 55px;
}

.contenedor {
  display: flex;
}

.text {
  display: flex;
  justify-content: center;
  align-items: center;
}

.box {
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

.box:hover input {
  width: 400px;
}

.box input {
  width: 0px;
  outline: none;
  border: none;
  font-weight: 500;
  transition: 0.8s;
  background: transparent;
}

.box a .fas {
  color: rgba(140, 243, 190, 0.9);
  font-size: 18px;
}

.logos:hover {
  -webkit-animation: rotate-scale-up-diag-1 0.7s linear both;
  animation: rotate-scale-up-diag-1 0.7s linear both;
}

@-webkit-keyframes rotate-scale-up-diag-1 {
  0% {
    -webkit-transform: scale(1) rotate3d(1, 1, 0, 0deg);
    transform: scale(1) rotate3d(1, 1, 0, 0deg);
  }

  50% {
    -webkit-transform: scale(2) rotate3d(1, 1, 0, -180deg);
    transform: scale(2) rotate3d(1, 1, 0, -180deg);
  }

  100% {
    -webkit-transform: scale(1) rotate3d(1, 1, 0, -360deg);
    transform: scale(1) rotate3d(1, 1, 0, -360deg);
  }
}

@keyframes rotate-scale-up-diag-1 {
  0% {
    -webkit-transform: scale(1) rotate3d(1, 1, 0, 0deg);
    transform: scale(1) rotate3d(1, 1, 0, 0deg);
  }

  50% {
    -webkit-transform: scale(2) rotate3d(1, 1, 0, -180deg);
    transform: scale(2) rotate3d(1, 1, 0, -180deg);
  }

  100% {
    -webkit-transform: scale(1) rotate3d(1, 1, 0, -360deg);
    transform: scale(1) rotate3d(1, 1, 0, -360deg);
  }
}
</style>
