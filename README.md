# 🏠 House Price Prediction System

A machine learning-based web application for predicting house prices using various input features. This project leverages Python, Django, and a trained ML model to deliver real-time predictions.

## 🎯 Project Objective

To provide a user-friendly interface where users can input house attributes and receive an estimated price based on a trained machine learning model.

## 🚀 Features

- House price prediction using regression models
- Web interface built with Django
- User input form to collect house features
- Model integration for real-time results
- Clean and responsive UI

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap
- **Model**: Trained using housing dataset (e.g., square footage, bedrooms, location, etc.)


## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- pip
- virtualenv (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/ayanchyaziz123/house-price-prediction-system.git

cd house-price-prediction-system

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run the development server
python manage.py runserver


