<template>
  <div class="main-background">
    <AppBar v-if="!showVideoResp" />
    <div style="height: 50px;"></div>
    <div v-if="!showVideoResp" class="card-container">
      <CardInfo 
        v-for="(shirt, index) in shirts"
        :key="index"
        :description="shirt.description"
        :imagetext="shirt.image"
        :name="shirt.name"
        @try-me="openVideoResp(shirt.image)"
      />
    </div>
    <div v-if="showVideoResp">
      <VideoResp 
        :front-file="pngfile" 
        :image-text="selectedImageFile" 
        :shirt-image="selectedImageFile"
      />
    </div>
  </div>
</template>

<script>
import AppBar from './AppBar.vue';
import CardInfo from './CardInfo.vue';
import VideoResp from './VideoResp.vue';

// Import images from the assets folder
import shirt1 from '@/assets/shirt1.png';
import shirt2 from '@/assets/shirt2.png';
import shirt3 from '@/assets/shirt3.png';
import shirt4 from '@/assets/shirt4.png';

export default {
  name: 'WelcomeComp',
  components: {
    AppBar,
    CardInfo,
    VideoResp,
  },
  props: {
    pngfile: {
      type: File,
      required: true,
    },
  },
  data() {
    return {
      selectedImageFile: null,
      showVideoResp: false,
      shirts: [
        {
          description: "Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: White",
          image: shirt1,
          name: "Raymond Cotton Shirt",
        },
        {
          description: "Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: Blue",
          image: shirt2,
          name: "Raymond Cotton Shirt",
        },
        {
          description: "Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: Black",
          image: shirt3,
          name: "Raymond Cotton Shirt",
        },
        {
          description: "Raymond Cotton Shirt Fabric for Men 1.6 Meters (Big Pana) Pattern: Self Design Slub, Color: Red",
          image: shirt4,
          name: "Raymond Cotton Shirt",
        },
      ],
    };
  },
  methods: {
    openVideoResp(imageFile) {
      this.selectedImageFile = imageFile;
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
