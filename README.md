# VTON
# 🛍️ Virtual Try-On System

This project is a Virtual Try-On System that allows users to upload image of their views along with a clothing image. These images are processed using an OnDemand REST API, which returns an image showing the user wearing the clothing.

## Prerequisites 🛠️
Ensure the following tools are installed:

1. **[Node.js](https://nodejs.org/)** - JavaScript runtime (includes npm).  
   👉 [Download Node.js](https://nodejs.org/en/download)  

2. **[Python 3.8+](https://www.python.org/downloads/)** - For backend setup.  
   👉 [Python installation guide](https://www.python.org/downloads/)

3. **npm** - Node Package Manager (comes with Node.js).  
   Check installation:  
   ```bash
   npm -v
4. pip - Python Package Installer.
   Check installation:
   ```bash
   pip --version

-----------------------------------------------------------------------------------------------------------------------------------
## Project Structure

 Virtual-Try-On-System/
│
├── frontend/                 
│   ├── public/               
│   └── src/                  
│       ├── components/       
│       │   ├── UploadPage.vue
│       │   └── ResultPage.vue
│       ├── App.vue           
│       ├── main.js           
│       └── router.js         
│   ├── package.json          
│   └── vue.config.js         
│
├── backend/                  
│   ├── app.py                
│   ├── requirements.txt      
│   └── static/               
│
└── README.md                 

------------------------------------------------------------------------------------------------------------------------------------
## Setup Instructions

 ### Clone Repository
  ```bash
     git clone https://github.com/your-repo/virtual-try-on-system.git
     
     cd virtual-try-on-system
```
 ### Frontend Setup
  ```bash
     cd frontend
     npm install  # Install dependencies
```
 ### Backend Setup
  ```bash
     cd backend
     python3 -m venv venv  # Create a virtual environment
     source venv/bin/activate  # Activate (Linux/macOS)
```
 ### On Windows: venv\Scripts\activate
  ```bash
     cd backend
     python3 -m venv venv  # Create a virtual environment
     source venv/bin/activate  # Activate (Linux/macOS)
```
 ### On Windows: venv\Scripts\activate
```bash
     pip install -r requirements.txt  # Install dependencies
```

 Add you API key to app.py:
```bash
    API_KEY = "your_api_key_here"
```
      
          

------------------------------------------------------------------------------------------------------------------------------------------
## Running the Application
### Start the Backend Server
```bash
     cd backend
     python app.py  # Starts the Flask backend
```
 Server runs at **http://localhost:5000**.

### Start the Frontend Server
  ```bash
     cd frontend
     npm run serve  # Starts Vue frontend
```
 Access frontend at **http://localhost:8080**.

-------------------------------------------------------------------------------------------------------------------------------------------
## 🛑 Troubleshooting
  **CORS Issues:** Use Flask-CORS to allow cross-origin requests.
  
  **API Key Error:** Verify that the API key in app.py is correct.
  
  **Network Issues:** Ensure backend runs on 5000 and frontend on 8080.

-------------------------------------------------------------------------------------------------------------------------------------------
## 🤝 Contributing
 We welcome contributions! Please submit issues or pull requests to enhance the project.





