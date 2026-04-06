# ✈️ Flight Booking System

## 📌 Overview

This project is a full-stack flight booking system built with Django and Django REST Framework.

It allows users to:
- Register and authenticate
- View available flights
- Create bookings
- Add passengers dynamically
- Manage and cancel reservations

The system was designed focusing on **real-world business rules**, **clean architecture**, and **user experience**.

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

flight-booking-challenge/
├── apps/
│   ├── bookings/
│   ├── customers/
│   ├── flights/
│   ├── planes/
├── config/
├── templates/
│   ├── pages/
│   └── partials/
├── challenges/
│   └── two_sum.py
├── questionnaire.md
├── README.md
├── requirements.txt

---

## ⚙️ Setup Instructions

1. Clone the repository  
2. Create virtual environment  
3. Install dependencies  
4. Configure environment variables  
5. Run migrations  
6. Create superuser  
7. Run server  

---

## 🌐 Access Points

- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/
- Login: http://127.0.0.1:8000/api-auth/login/

---

## 🔌 API Endpoints

### Flights
GET /api/flights/

### Bookings
GET /api/bookings/
POST /api/bookings/

### Customers
GET /api/customers/
POST /api/customers/

---

## 🧠 Business Rules

- A flight cannot exceed its seat capacity
- Seat numbers must be valid
- A seat can only be assigned once per flight
- Users can only access their own bookings

---

## 👤 Passenger Logic

- Passengers are created dynamically
- Each passenger is linked to a user
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

## 🧪 Tests

Run:

python manage.py test

---

## 💡 Design Decisions

- Business rules centralized in models
- Validation reused in API layer
- Separation between API and frontend

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