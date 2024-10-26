<template>
    <div class="preview-container">
      <h2>Preview</h2>
      <div class="image-wrapper">
        <!-- Show the selected shirt image -->
        <img v-if="shirtImage" :src="shirtImage" alt="Selected Shirt" class="preview-image" />
        <!-- Show the user-uploaded image if it exists -->
        <img v-if="imageUrl" :src="imageUrl" alt="User Uploaded Image" class="preview-image" />
      </div>
      <!-- Show the video if it exists -->
      <video v-if="videoUrl" controls class="preview-video">
        <source :src="videoUrl" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <!-- Submit Button -->
      <button class="submit-button" @click="submitImages">Submit</button>
      <!-- Display the resulting image -->
      <div v-if="resultImage" class="result-wrapper">
        <h3>Achieved Image</h3>
        <img :src="resultImage" alt="Achieved Result" class="result-image" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'VideoResp',
    props: {
      frontFile: {
        type: File,
        required: false, // Make it optional for flexibility
      },
      imageText: {
        type: String,
        required: true,
      },
      shirtImage: {
        type: String,
        required: true, // Ensure a shirt image is always passed
      },
    },
    data() {
      return {
        imageUrl: null,
        videoUrl: null,
        resultImage: null, // To hold the achieved image
      };
    },
    created() {
      this.loadMedia();
    },
    methods: {
      loadMedia() {
        // Load the media based on the file type
        if (this.frontFile) {
          if (this.frontFile.type.startsWith('image/')) {
            this.imageUrl = URL.createObjectURL(this.frontFile);
          } else if (this.frontFile.type.startsWith('video/')) {
            this.videoUrl = URL.createObjectURL(this.frontFile);
          }
        }
      },
      async submitImages() {
        try {
          const formData = new FormData();
          // Append the shirt image and the user-uploaded file to the FormData
          formData.append('shirtImage', this.shirtImage);
          if (this.frontFile) {
            formData.append('userImage', this.frontFile); // Send the user-uploaded image
          }
  
          // Fetch API to send the images
          const response = await fetch('/api/img', {
            method: 'POST',
            body: formData,
          });
  
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
  
          // Handle successful response
          const data = await response.json();
          if (data.result) {
            // Set the achieved image to display
            this.resultImage = `data:image/png;base64,${data.result}`;
          } else {
            console.error('Error: ', data.error);
          }
        } catch (error) {
          console.error('Error submitting images:', error);
        }
      },
    },
    beforeUnmount() {
      // Release the object URL when the component is unmounted
      if (this.imageUrl) {
        URL.revokeObjectURL(this.imageUrl);
      }
      if (this.videoUrl) {
        URL.revokeObjectURL(this.videoUrl);
      }
    },
  };
  </script>
  
  <style scoped>
  /* Maintain existing styles for consistency */
  .preview-container {
    text-align: center;
    max-width: 600px; /* Limit width for better presentation */
    margin: 0 auto; /* Center the container */
    padding: 20px;
    background-color: #ffffff; /* White background for contrast */
    border-radius: 10px; /* Rounded corners */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  }
  
  h2 {
    margin-bottom: 20px;
    font-size: 24px;
    color: #333; /* Darker text for better readability */
  }
  
  .image-wrapper {
    display: flex; /* Flex layout for images */
    flex-direction: column; /* Stack images vertically */
    align-items: center; /* Center images */
    margin-bottom: 20px; /* Space below the images */
  }
  
  .preview-image {
    display: block;
    margin: 10px 0; /* Space between images */
    max-width: 100%;
    height: auto;
    border-radius: 10px; /* Rounded corners for images */
    border: 2px solid #007bff; /* Border color for images */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Shadow for images */
    transition: transform 0.2s; /* Animation for hover effect */
  }
  
  .preview-image:hover {
    transform: scale(1.02); /* Slight zoom on hover */
  }
  
  .preview-video {
    display: block;
    margin: 20px auto; /* Adjusted margin for spacing */
    max-width: 100%;
    border-radius: 10px; /* Rounded corners for video */
  }
  
  .submit-button {
    margin-top: 20px;
    background-color: #007bff; /* Primary button color */
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s; /* Animation for hover effect */
  }
  
  .submit-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    transform: scale(1.05); /* Slightly larger on hover */
  }
  
  .result-wrapper {
    margin-top: 20px;
  }
  
  .result-image {
    margin: 10px auto;
    max-width: 100%;
    height: auto;
    border-radius: 10px; /* Rounded corners for result image */
    border: 2px solid #28a745; /* Green border for distinction */
  }
  </style>
  