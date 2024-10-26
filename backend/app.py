from flask import Flask, request, jsonify
import requests
from preprocess import preprocessInput

from PIL import Image
import numpy as np

app = Flask(__name__)

# OnDemand API endpoint
ONDEMAND_API_URL = "http://localhost:5000/api/process"

# API Key for OnDemand (if required)
API_KEY = "a8kP5OGcKiBZe0z6orDQwQDVb8KJZoZE"

@app.route('/api/try-on', methods=['POST'])
def virtual_try_on():
    try:
        # Get the JSON payload from the request
        data = request.json

        # Extract base64 strings from the request
        user_image_b64 = data.get('user_image')
        clothing_image_b64 = data.get('clothing_image')

        # Check if all images are provided
        if not all([user_image_b64, clothing_image_b64]):
            return jsonify({"error": "All images are required"}), 400

        # Prepare the payload for OnDemand API
        payload = {
            "user_image": user_image_b64,
            "clothing_image": clothing_image_b64
        }

        # Send request to OnDemand API
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        response = requests.post(ONDEMAND_API_URL, json=payload, headers=headers)

        # Handle the response from OnDemand API
        if response.status_code == 200:
            image_url = response.json().get("image_url")
            return jsonify({"image_url": image_url}), 200
        else:
            return jsonify({"error": response.json()}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/preprocess', methods=['POST'])
def preprocess():
    
    try:
        import requests

        url = "https://api.on-demand.io/media/v1/public/file"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

        print(response.text)
        
        preprocess_user = preprocessInput()

        op_user = preprocess_user.remove_bg(r'C:\React\VTON\user.jpg')
        arr_user = preprocess_user.transform()
        return jsonify({"image_url": arr_user}), 200
        # Image.fromarray(arr).show()

        # preprocess_cloth = preprocessInput()
        # op_cloth = preprocess_cloth.remove_bg(r'C:\React\VTON\cloth_img1.jpg')
        # def transform(width=768, height=1024):
        #         newsize = (width, height)

        #         pic = op_cloth
        #         img = Image.fromarray(pic).resize(newsize)
        #         background = Image.new("RGBA", newsize, (0, 0, 0, 0))
        #         background.paste(img, mask=img.split()[3])
        #         save_path = r"C:\React\VTON\cloth_img1" + 'new.jpg'
        #         # background.convert('RGB').save(save_path, 'JPEG')

        #         return np.asarray(background.convert('RGB'))
        # arr_user = transform()
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port="5000")
