from flask import Flask, jsonify, request
import requests
import base64
from PIL import Image
from io import BytesIO

# Initialize Flask app
app = Flask(__name__)

# Basic route to check the server status
@app.route('/api/img')
def home():
    try:
        data = request.get_json()

        clothing_image_base64 = data.get("cloth_image")
        user_image_base64 = data.get("user_image")

        if not clothing_image_base64 or not user_image_base64:
            return jsonify({"error": "Both 'clothing_image' and 'user_image' are required"}), 400
        

        api_key = "SG_1afd12a7789c2be8"
        url = "https://api.segmind.com/v1/try-on-diffusion"

        # Request payload
        data = {
        "model_image": user_image_base64, 
        "cloth_image": clothing_image_base64, 
        "category": "Upper body",
        "num_inference_steps": 35,
        "guidance_scale": 2,
        "seed": 12467,
        "base64": False
        }

        headers = {'x-api-key': api_key}

        response = requests.post(url, json=data, headers=headers)
        
        def pil_image_to_base64(image):
            # Create an in-memory bytes buffer
            buffered = BytesIO()
            
            # Save the PIL image to the buffer in PNG format (or any format of your choice)
            image.save(buffered, format="PNG")
            
            # Get the image bytes and encode them to Base64
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return img_base64
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            # image.show()  # Opens the image in the default viewer
            img = pil_image_to_base64(image)
            return jsonify({"result" : img}), 200
        else:
            print("Failed to retrieve image. Status code:", response.status_code)
            print("Response:", response.content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
