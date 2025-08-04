# 🏨 MLOPS Hotel Reservation Project

This project demonstrates a complete **MLOps pipeline** for a **Hotel Reservation Prediction System** using Flask, Jenkins, Docker, and cloud deployment. It covers all stages from data preprocessing, model training, CI/CD, and deployment.

---

### 📁 Project Structure

├── MLOPS_Hotel_Reservation_Project.egg-info/  # Project metadata for packaging  
├── application.py                             # Main Flask application  
├── artifacts/                                 # Model artifacts (saved model, transformers, etc.)  
├── config/                                    # Configuration files for training and prediction  
├── custom_jenkins/                            # Jenkins pipeline configuration and scripts  
├── logs/                                      # Logging for training and prediction  
├── notebook/                                  # Jupyter notebooks for EDA and model experimentation  
├── pipeline/                                  # Code for training and prediction pipelines  
├── src/                                       # Source code: training modules, components  
├── static/                                    # Static files for the Flask web app (CSS, JS, etc.)  
├── templates/                                 # HTML templates for the Flask frontend  
├── utils/                                     # Utility functions (data preprocessing, evaluation, etc.)  
├── .DS_Store                                  # macOS system file (safe to ignore)  
├── .gitignore                                 # Files/folders to ignore in version control  
├── Dockerfile                                 # Docker setup for containerizing the app  
├── Jenkinsfile                                # Jenkins CI/CD pipeline script  
├── README.md                                  # Project documentation  
├── requirements.txt                           # Python dependencies  
├── setup.py                                   # Setup script for building/installing the project  

---

### 🔧 Key Features

- ✅ End-to-end MLOps pipeline  
- 📊 Data preprocessing and model training  
- 🔁 CI/CD with Jenkins  
- 🐳 Containerized using Docker  
- 🌐 Web app with Flask and HTML templates  
- ☁️ Cloud-ready deployment pipeline  
- 📁 Modular project structure  

---

### 🚀 How to Run

#### 📦 Step 1: Clone the Repository

git clone https://github.com/beniamine3155/MLOPS_Hotel_Reservation_Project.git  
cd MLOPS_Hotel_Reservation_Project  

#### 📁 Step 2: Set Up Virtual Environment

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
pip install -r requirements.txt  

#### 🏃 Step 3: Run Flask App

python application.py  

> App will be live at: `http://localhost:5000`  

---

### 🐳 Docker Setup

#### 🏗️ Build Docker Image

docker build -t hotel-reservation-app .  

#### 🚀 Run Docker Container

docker run -p 5000:5000 hotel-reservation-app  

---

### 🧪 CI/CD with Jenkins

- Jenkins is configured via `Jenkinsfile`  
- Auto-trigger training, testing, and deployment upon Git push  
- Setup includes stages for:  
  - Code linting  
  - Unit testing  
  - Docker image creation  
  - Cloud deployment (e.g., GCP, AWS, etc.)  

---

### 📂 Notebooks

Located in the `notebook/` directory, these provide:

- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Experimentation and Testing  

---

### 🧠 Technologies Used

- **Python**  
- **Flask**  
- **Pandas**  
- **Scikit-learn**  
- **Docker**  
- **Jenkins**  
- **HTML/CSS**  
- **Google Cloud / AWS (optional deployment)**  

---






