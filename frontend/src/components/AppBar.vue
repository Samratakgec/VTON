<template>
    <header class="app-bar">
      <h1 class="app-bar-title">Welcome User</h1>
    </header>
  </template>
  
  <script>
  export default {
    name: 'AppBar',
  };
  </script>
  
  <style scoped>
  .app-bar {
    width: 100%;
    background: linear-gradient(135deg, #6b4f4f, #8a7d7d); /* Added gradient background */
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 80px;
    padding: 0 30px; /* Adjusted padding */
    box-sizing: border-box;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Added subtle shadow */
    border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* Added subtle border */
  }
  
  .app-bar-title {
    color: #f4f4f4; /* Softer white */
    font-size: 28px; /* Increased font size */
    font-weight: 600;
    margin: 0;
    flex: 1;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); /* Slight text shadow */
  }
  
  /* Media Queries for responsiveness */
  @media (max-width: 768px) {
    .app-bar-title {
      font-size: 22px;
    }
    .app-bar {
      height: 70px;
      padding: 0 20px;
    }
  }
  
  @media (max-width: 480px) {
    .app-bar-title {
      font-size: 18px;
    }
    .app-bar {
      height: 60px;
      padding: 0 15px;
    }
  }
  </style>
  