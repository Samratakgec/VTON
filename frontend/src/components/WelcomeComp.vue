<template>
  <div class="main-background">
    <AppBar v-if="!showVideoResp" />
    <div style="height: 50px;"></div>
    <div v-if="!showVideoResp" class="card-container">
      <CardInfo 
        description="Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: White"
        :imagetext="shirt1"
        name="Raymond Cotton Shirt"
        @try-me="openVideoResp"
      />
      <CardInfo 
        description="Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: Blue"
        :imagetext="shirt2"
        name="Raymond Cotton Shirt"
        @try-me="openVideoResp"
      />
      <CardInfo 
        description="Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: Black"
        :imagetext="shirt3"
        name="Raymond Cotton Shirt"
        @try-me="openVideoResp"
      />
      <CardInfo 
        description="Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: Red"
        :imagetext="shirt4"
        name="Raymond Cotton Shirt"
        @try-me="openVideoResp"
      />
    </div>
    <div v-if="showVideoResp">
      <VideoResp :front-base64="frontBase64" :image-text="selectedImageText" />
    </div>
  </div>
</template>

<script>
import AppBar from './AppBar.vue';
import CardInfo from './CardInfo.vue';
import VideoResp from './VideoResp.vue';
import { shirt1, shirt2, shirt3, shirt4 } from '@/assets/shirtimgs.js';

export default {
  name: 'WelcomeComp',
  components: {
    AppBar,
    CardInfo,
    VideoResp
  },
  props: {
    frontBase64: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      shirt1,
      shirt2,
      shirt3,
      shirt4,
      selectedImageText: '',
      showVideoResp: false,
    };
  },
  methods: {
    openVideoResp(imagetext) {
      this.selectedImageText = imagetext;
      this.showVideoResp = true; // Show VideoResp component
    },
  },
};
</script>

<style scoped>
.main-background {
  background: linear-gradient(to right, #f0f4c3, #a8d8ea);
  min-height: 100vh;
  padding: 30px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  padding: 20px;
  justify-items: center;
  width: 100%;
  max-width: 1200px;
}

/* Optional: Add smooth animations */
.card-container > div {
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease;
}

.card-container > div:hover {
  transform: scale(1.03);
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
}
</style>
