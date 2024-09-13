<script setup>
import { ref, computed } from 'vue';

const technicians = ref([
  { name: 'Juan Pérez', position: 'Ingeniero de Soporte' },
  { name: 'María García', position: 'Técnico de Mantenimiento' },
  { name: 'Carlos Rodríguez', position: 'Especialista en Redes' },
]);

const searchQuery = ref('');
const filteredTechnicians = computed(() => {
  return technicians.value.filter(technician =>
    technician.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const isFormVisible = ref(false);
const isEditing = ref(false); // Nuevo estado para saber si estamos editando o añadiendo
const currentEditIndex = ref(null); // Guardamos el índice del técnico a editar

const newTechnician = ref({
  name: '',
  position: ''
});

const toggleView = () => {
  isFormVisible.value = !isFormVisible.value;
  isEditing.value = false; // Reiniciar estado de edición
  newTechnician.value = { name: '', position: '' }; // Limpiar formulario
};

const addOrUpdateTechnician = () => {
  if (newTechnician.value.name && newTechnician.value.position) {
    if (isEditing.value) {
      // Actualizar técnico existente
      technicians.value[currentEditIndex.value] = { ...newTechnician.value };
      isEditing.value = false;
    } else {
      // Añadir nuevo técnico
      technicians.value.push({ ...newTechnician.value });
    }
    newTechnician.value = { name: '', position: '' };
    isFormVisible.value = false;
  } else {
    alert('Por favor, completa ambos campos.');
  }
};

const editTechnician = (index) => {
  isEditing.value = true;
  currentEditIndex.value = index;
  newTechnician.value = { ...technicians.value[index] }; // Poblar el formulario con los datos del técnico
  isFormVisible.value = true;
};

const deleteTechnician = (index) => {
  if (confirm(`¿Seguro que deseas eliminar al técnico: ${technicians.value[index].name}?`)) {
    technicians.value.splice(index, 1);
  }
};
</script>

<template>
<<<<<<< Updated upstream
  <section id="container">
    <div v-if="isFormVisible" class="form-container">
      <h2>{{ isEditing ? 'Editar Técnico' : 'Añadir Técnico' }}</h2>
      <input v-model="newTechnician.name" type="text" placeholder="Nombre del técnico" />
      <input v-model="newTechnician.position" type="text" placeholder="Cargo del técnico" />
      <button @click="addOrUpdateTechnician" class="save-btn">{{ isEditing ? 'Actualizar' : 'Guardar' }}</button>
      <button @click="toggleView" class="cancel-btn">Cancelar</button>
    </div>

    <div v-else>
      <div class="header">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Buscar técnico por nombre..."
          class="search-input"
        />
        <button @click="toggleView" class="add-btn">+</button>
      </div>

      <ul class="technician-list">
        <li v-for="(technician, index) in filteredTechnicians" :key="index" class="technician-item">
          <div class="technician-info">
            <span class="technician-name">{{ technician.name }}</span>
            <span class="technician-position">{{ technician.position }}</span>
          </div>
          <div class="action-buttons">
            <button @click="editTechnician(index)" class="edit-btn">✎</button>
            <button @click="deleteTechnician(index)" class="delete-btn">✖</button>
          </div>
        </li>
      </ul>

      <p>Total de Técnicos: {{ filteredTechnicians.length }}</p>
    </div>
  </section>
=======
    <section id="container">
        <div class="container-sec">
            <form id="tec-form">
                <h2>Ingrese para empezar turno</h2>
                <span>Ingrese su usuario y clave</span>
                <div class="container-input">
                    <ion-icon name="person-outline"></ion-icon>
                    <input type="text" placeholder="Usuario" />
                </div>
                <div class="container-input">
                    <ion-icon name="lock-closed-outline"></ion-icon>
                    <input type="password" placeholder="Clave" />
                </div>
                <button class="button">INICIAR SESION</button>
            </form>
        </div>
        <div class="container-sec">
            <nav id="tec-nav">

            </nav>
        </div>
    </section>
>>>>>>> Stashed changes
</template>

<style scoped>
#container {
  background-color: rgb(255, 255, 255);
  position: relative;
  width: 62%;
  height: auto;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Barra de búsqueda */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  width: 85%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.add-btn {
  background-color: #ff7700;
  border: none;
  color: white;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  font-size: 1.5em;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.add-btn:hover {
  background-color: #ff9c40;
  transform: scale(1.1);
}

/* Listado de técnicos */
.technician-list {
  list-style-type: none;
  padding: 0;
}

.technician-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  margin-bottom: 10px;
  background-color: #f0f0f0;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.technician-info {
  display: flex;
  flex-direction: column;
}

.technician-name {
  font-weight: bold;
}

.technician-position {
  font-size: 0.9em;
  color: #666;
}

/* Botones de acción */
.action-buttons {
  display: flex;
  gap: 10px;
}

button {
  border: none;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2em;
  cursor: pointer;
}

.edit-btn {
  background-color: #ff7700;
  color: white;
}

.delete-btn {
  background-color: #333;
  color: white;
}

/* Estilos del formulario */
.form-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-container input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

/* Botones largos con efectos minimalistas */
.save-btn,
.cancel-btn {
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.save-btn {
  background-color: #4caf50;
  color: white;
}

.save-btn:hover {
  background-color: #66bb6a;
  color: white;
}

.cancel-btn {
  background-color: #f44336;
  color: white;
}

.cancel-btn:hover {
  background-color: #e57373;
  color: white;
}
</style>
