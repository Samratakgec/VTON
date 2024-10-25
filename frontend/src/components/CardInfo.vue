<template>
    <div class="container">
      <div class="card">
        <h2 class="name">{{ name }}</h2>
        <div class="image-container">
          <img :src="imagetext" class="image" alt="Card Image" />
        </div>
        <div class="details-container">
          <p class="description">{{ description }}</p>
        </div>
        <button class="action-button">Try Me</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CardInfo',
    props: {
      name: {
        type: String,
        required: true
      },
      description: {
        type: String,
        required: true
      },
      imagetext: {
        type: String,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    text-align: center;
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Center vertically */
  }
  
  .card {
    padding: 20px;
    margin: 20px;
    max-width: 400px;
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
    border-radius: 15px;
    background: linear-gradient(145deg, #ffffff, #e6e6e6);
    overflow: hidden;
    width: 80%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .card:hover {
    transform: translateY(-10px);
    box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.3);
  }
  
  .image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .image {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #fff;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
    transition: box-shadow 0.3s ease;
  }
  
  .image:hover {
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
  }
  
  .name {
    font-size: 26px;
    font-weight: 700;
    color: #333;
    margin-top: 0px;
    margin-bottom: 15px;
  }
  
  .details-container {
    text-align: left;
    padding: 10px 0;
    border-top: 1px solid #eee;
    font-size: 16px;
  }
  
  .description {
    color: #555;
    line-height: 1.5;
  }
  
  .action-button {
    background-color: #ff6b6b;
    color: #ffffff;
    border: none;
    padding: 12px 24px;
    cursor: pointer;
    border-radius: 25px;
    font-size: 16px;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    margin-top: 20px;
  }
  
  .action-button:hover {
    background-color: #ff4a4a;
    box-shadow: 0px 6px 15px rgba(255, 107, 107, 0.4);
  }
  </style>
  