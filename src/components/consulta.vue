<script>
import { ref, onMounted } from "vue";
import axios from "axios";
export default {
  setup() {
    const dato = ref([]);
    const consultaDatosCliente = async () => {
      try {
        const respuesta = await axios.get("http://127.0.0.1:8000/datosfire");
        if (Array.isArray(respuesta.data)) {
          dato.value = respuesta.data;
        } else {
          console.error("No se cargaron los datos", respuesta.data);
        }
      } catch (error) {
        console.error("Error no hay respuesta", error);
      }
    };
    let intervalo = null

    onMounted(() => {
        consultaDatosCliente()
        intervalo = setInterval(consultaDatosCliente, 2000);
    })
    onMounted(consultaDatosCliente);
    return { dato };
  }
};
</script>

<template>
  <section class="section">
    <h1>Clientes</h1>
    <table class="table">
      <thead>
        <tr class="tr">
          <th class="th" id="th-name">Nombre</th>
          <th class="th">Documento</th>
          <th class="th">Apellido</th>
          <th class="th">Telefono</th>
          <th class="th">Direccion</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="i in dato" :key="i" class="tr">
          <td class="td" id="td-name">{{ i.name }}</td>
          <td class="td">{{ i.doc }}</td>
          <td class="td">{{ i.secondName }}</td>
          <td class="td">{{ i.cel }}</td>
          <td class="td">{{ i.direction }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<style scoped>
  .section{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 20px;
  }
  .table{
    margin: 10px;
    background-color: rgb(33, 174, 97);
    padding: 30px 20px;
    border: 2px solid black;
  }
  .th, .td{
    padding: 10px;
    text-align: center;
    transition: all .3s ease-in-out;
    border: 2px solid black;
    margin: 0;
  }

  .td:hover{
    background-color: rgb(19, 97, 55);
    border-radius: 10px;
  }

  #td-name, #th-name{
    background-color: rgb(30, 110, 22);
  }
</style>