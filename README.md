# Workout API

## 📌 Overview
The Workout API is a RESTful API built with Django and Django REST Framework (DRF) to manage personalized workout plans. It includes predefined exercises, user authentication, progress tracking, and API documentation.

## 🛠️ Features
- User authentication with JWT (login, signup)
- Predefined exercises with database seeding
- Personalized workout plans
- Progress tracking
- API documentation using Swagger
- Docker support (optional bonus feature)

## 🚀 Tech Stack
- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** PostgreSQL (or SQLite for local development)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Documentation:** Swagger (drf-yasg)
- **Version Control:** Git & GitHub

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/your-username/workout-api.git
 cd workout-api
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```
SECRET_KEY=your_secret_key
DEBUG=True  # Set to False in production
DATABASE_URL=sqlite:///db.sqlite3  # Change for PostgreSQL if needed
```

### 5️⃣ Apply Migrations
```sh
python manage.py migrate
```

### 6️⃣ Seed the Database with Exercises
```sh
python manage.py seed_exercises
```

### 7️⃣ Run the Development Server
```sh
python manage.py runserver
```
API will be available at `http://127.0.0.1:8000/`

---

## 📖 API Documentation
Swagger UI is enabled for easy testing.

- **Access Swagger UI**: [`http://127.0.0.1:8000/swagger/`](http://127.0.0.1:8000/swagger/)
- **Alternative (Redoc)**: [`http://127.0.0.1:8000/redoc/`](http://127.0.0.1:8000/redoc/)

To generate documentation:
```sh
python manage.py generate_swagger
```

---

## 🐳 Running with Docker (Optional)
Ensure Docker is installed, then run:
```sh
docker-compose up --build
```

---

## ✅ Testing the API
Run the Django test suite:
```sh
python manage.py test
```

---

## 📩 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Added feature X'`)
4. Push to GitHub (`git push origin feature-name`)
5. Open a pull request

---

💬 **For any questions or issues, feel free to open an issue on GitHub!** 🚀

