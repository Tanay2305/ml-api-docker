# ML API with FastAPI and Docker

## 🚀 Overview
This project is a simple machine learning API built using FastAPI and deployed using Docker.

## 🧠 Features
- Predicts whether a number is SMALL or LARGE
- Uses a trained ML model (scikit-learn)
- API built with FastAPI
- Containerized using Docker

## ⚙️ Tech Stack
- Python
- FastAPI
- scikit-learn
- Docker

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload

🐳 Run with Docker
docker build -t ml-api .
docker run -p 8000:8000 ml-api

🌐 API Endpoint
GET /predict?num=25

Response:
{"result": "SMALL"}