<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- <WelcomeComp/> -->
   <HomePage/>
</template>

<script>
import HomePage from './components/HomePage.vue';

// import HelloWorld from './components/HelloWorld.vue'
// import WelcomeComp from './components/WelcomeComp.vue';

export default {
  name: 'App',
  components: {
    // HelloWorld
    // WelcomeComp
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
