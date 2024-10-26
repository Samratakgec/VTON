from flask import Flask, jsonify, request, send_from_directory
import requests
import base64
from PIL import Image
import io
from io import BytesIO

# Initialize Flask app
app = Flask(__name__, static_folder="../frontend/dist")

@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")

# Serve static assets (JavaScript, CSS, etc.)
@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# Basic route to check the server status
@app.route('/api/img', methods=["POST"])
def home():
    try:
        # Check if files are present in the request
        clothing_image = request.files.get('shirtImage')
        user_image = request.files.get('userImage')

        if not clothing_image or not user_image:
            return jsonify({"error": "Both 'shirtImage' and 'userImage' are required"}), 400

        # Convert images to Base64
        clothing_image_base64 = convert_image_to_base64(clothing_image)
        user_image_base64 = convert_image_to_base64(user_image)

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

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            img = pil_image_to_base64(image)  # Convert image to base64
            return jsonify({"result": img}), 200
        else:
            print("Failed to retrieve image. Status code:", response.status_code)
            print("Response:", response.content)
            return jsonify({"error": "Failed to retrieve processed image."}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def convert_image_to_base64(image):
    # Read the image file and convert it to Base64
    image = Image.open(image)
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        png_bytes = output.getvalue()  # Get the byte data
        return base64.b64encode(png_bytes).decode('utf-8')  # Encode to Base64

def pil_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_base64

if __name__ == '__main__':
    app.run(debug=True)
