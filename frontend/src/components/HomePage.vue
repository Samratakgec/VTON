<template>
  <div>
    <AppBar />
    <div v-if="!submitted">
      <div style="height: 100px;"></div>
      <div class="form-container">
        <h2>Upload User Images</h2>
        <form @submit.prevent="submitForm">
          <div class="input-group">
            <label for="front-view">Front View:</label>
            <input type="file" id="front-view" @change="(e) => handleImageUpload(e, 'front')" accept="image/png" />
          </div>
          <button type="submit">Submit</button>
        </form>
        <div v-if="frontFile" class="preview-container">
          <h3>Image Previews</h3>
          <div class="preview">
            <h4>Front View:</h4>
            <img v-if="frontURL" :src="frontURL" alt="Front View Preview" />
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <WelcomeComp :pngfile="frontFile" />
    </div>
  </div>
</template>

<script>
import AppBar from './AppBar.vue';
import WelcomeComp from './WelcomeComp.vue';

export default {
  name: 'HomePage',
  components: {
    AppBar,
    WelcomeComp,
  },
  data() {
    return {
      frontFile: null,
      frontURL: '',
      submitted: false,
    };
  },
  methods: {
    handleImageUpload(event, view) {
      const input = event.target;
      if (input.files && input.files[0]) {
        const file = input.files[0];
        if (view === 'front') {
          this.frontFile = file;
          this.frontURL = URL.createObjectURL(file);
        }
      }
    },
    submitForm() {
      if (this.frontFile) {
        console.log("Front File: ", this.frontFile);
        alert("Image uploaded successfully!");
        this.submitted = true; // Display the WelcomeComp component
      } else {
        alert("Please upload the front view image.");
      }
    },
  },
};
</script>

<style scoped>
.form-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
}

.input-group {
  margin: 15px 0;
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

input[type="file"] {
  padding: 5px;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  display: block;
  margin: 20px auto;
}

button:hover {
  background-color: #45a049;
}

.preview-container {
  margin-top: 30px;
}

.preview {
  text-align: center;
  margin: 15px 0;
}

img {
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
}
</style>
