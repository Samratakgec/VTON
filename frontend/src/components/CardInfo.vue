<template>
  <div class="card">
    <img :src="imagetext" alt="Product Image" class="card-image" />
    <h3>{{ name }}</h3>
    <p>{{ description }}</p>
    <button @click="tryMe">Try Me</button>
  </div>
</template>

<script>
export default {
  name: 'CardInfo',
  props: {
    description: {
      type: String,
      required: true,
    },
    imagetext: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
  methods: {
    tryMe() {
      this.$emit('try-me', {
        image: this.imagetext, // Emit the image path
        name: this.name, // Optionally, you can pass the name or other properties
      });
    },
  },
};
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
  transition: box-shadow 0.3s;
}

.card:hover {
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}

.card-image {
  width: 100%;
  height: auto;
  max-width: 200px;
  border-radius: 5px;
}

button {
  margin-top: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
