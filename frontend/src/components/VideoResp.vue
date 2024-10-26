<template>
    <div class="video-container">
      <h2>Video Response</h2>
      <p>{{ imageText }}</p> <!-- Display the image text -->
      <textarea placeholder={{frontBase64}}></textarea>
      <textarea placeholder={{imageText}}></textarea>
      <button class="send-button" @click="sendData">Send Data</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'VideoResp',
    props: {
      frontBase64: {
        type: String,
        required: true,
      },
      imageText: {
        type: String,
        required: true,
      },
    },
    methods: {
      async sendData() {
        const dataToSend = {
        cloth_image: this.imageText,
          user_image: this.frontBase64,
        };
        console.log(this.frontBase64) ;
          console.log(this.imageText) ;
        try {
          const response = await fetch('/api/img', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataToSend),
          });
  
          if (response.ok) {
            const result = await response.json();
            console.log('Data sent successfully:', result);
          } else {
            console.error('Failed to send data:', response.statusText);
          }
        } catch (error) {
          console.error('Error:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .video-container {
    padding: 20px;
    text-align: center;
  }
  
  .send-button {
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
  
  .send-button:hover {
    background-color: #ff4a4a;
    box-shadow: 0px 6px 15px rgba(255, 107, 107, 0.4);
  }
  </style>
  