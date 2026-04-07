# ✈️ Flight Booking System (Django + DRF)

## 📌 Overview

This project is a full-stack flight booking system built with Django and Django REST Framework.

It allows users to:
- Register and authenticate
- View available flights
- Create bookings
- Add passengers dynamically
- Manage and cancel reservations

The system was designed focusing on real-world business rules, clean architecture, and user experience.

---

## 🧠 Key Features

- Flight listing with dynamic data
- Booking system with seat validation
- Dynamic passenger creation during booking
- Authentication and user-based data isolation
- Booking cancellation with confirmation
- REST API with validation layer
- Automated tests (model + API)
- Django Admin as backoffice

---

## 🏗️ Project Structure
````
flight-booking-challenge/
│
├── apps/
│   ├── bookings/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │   └── tests_api.py
│   ├── customers/
│   ├── flights/
│   ├── planes/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── templates/
│   ├── pages/
│   └── partials/
│
├── challenges/
│   └── two_sum.py
│
├── questionnaire.md
├── requirements.txt
└── README.md
````
---

## ⚙️ Setup Instructions

1. Clone the repository

git clone <your-repo-url>
cd flight-booking-challenge

2. Create virtual environment

python -m venv venv

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Create superuser

python manage.py createsuperuser

6. Run server

python manage.py runserver

---

## 🌐 Access Points

Home: http://127.0.0.1:8000/  
Admin: http://127.0.0.1:8000/admin/  
API: http://127.0.0.1:8000/api/  
Login: http://127.0.0.1:8000/api-auth/login/

---

## 🔌 API Endpoints

Flights  
GET /api/flights/

Bookings  
GET /api/bookings/  
POST /api/bookings/

Customers  
GET /api/customers/  
POST /api/customers/

---

## 🔐 Permissions

- GET requests are public  
- POST requests are allowed without authentication (for testing purposes)  
- Authenticated users can only access their own bookings  
- Update and delete operations require authentication  

---

## 🧠 Business Rules

- A flight cannot exceed its seat capacity  
- Seat numbers must be valid  
- A seat can only be assigned once per flight  
- Users can only access their own bookings  

---

## 👤 Passenger Logic

- Passengers are created dynamically during booking  
- Each passenger is linked to a user when authenticated  
- Supports booking for multiple people  

---

## 🔄 Booking Flow

User registers / logs in  
→ Views flights  
→ Selects a flight  
→ Adds passenger  
→ Chooses seat  
→ Creates booking  
→ Views or cancels booking  

---

## ⚡ Performance Considerations

- Optimized queries using select_related  
- Avoids N+1 query problems  

---

## 🧪 Tests

Run tests with:

python manage.py test

---

## 💡 Design Decisions

- Business rules centralized in models  
- Validation reused in serializers  
- Separation between API and frontend  
- Custom permission to support tests and security  

---

## 🧠 Logic Challenges

Located in:
challenges/

Implemented:
- Two Sum  

---

## 👨‍💻 Author

Gabriel Rodrigues  
Backend Developer (Python / Django)
