# Calorie Counter Web Application (Django)

This project is a **Calorie Counter Web Application** developed with **Python (Django)**.  
It helps users calculate the number of calories they need daily based on their personal details and allows them to track daily consumed calories. The app also provides simple guidelines for maintaining, gaining, or losing weight.

---

## 🔢 Calorie Calculation Formula

The app uses the **Basal Metabolic Rate (BMR)** formula:

- **For Male**  
BMR = 66.47 + (13.75 × weight in kg) + (5.003 × height in cm) − (6.755 × age in years)
**For Female**
BMR = 655.1 + (9.563 × weight in kg) + (1.850 × height in cm) − (4.676 × age in years)

---

## 📌 Features

1. User authentication:  
 - Registration (username, email, password, confirm password)  
 - Login (username/email and password)  

2. User profile with details:  
 - Name, Age, Gender, Height, Weight  

3. Input form for daily consumed calories:  
 - Item name, Calories consumed  

4. Dashboard to view:  
 - Required calories per day  
 - Consumed calories per day  

5. Django Admin integration for managing data.

---

## 🛠️ Job Specification

- Create a new Django project named:  
**`Name_ID_CaloryCounter`**

- Steps:
1. Create Django models for **Calorie Counter**.  
2. Create views for login, registration, and dashboard.  
3. Use Django forms to take input:  
   - User details (Name, Age, Gender, Height, Weight)  
   - Daily consumed calories (Item name, Calories)  
4. Configure URL patterns.  
5. Implement calorie calculation logic in `views.py`.  
6. Create a superuser and register models in Django Admin.  

---

## ⚡ Installation & Setup

1. **Clone the repository**
bash
 git clone https://github.com/yourusername/calorie-counter.git
 cd calorie-counter
2. **Create and activate virtual environment**
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3. **Install dependencies**
pip install django
4. **Create Django project**
django-admin startproject Name_ID_CaloryCounter
cd Name_ID_CaloryCounter
5. **Run migrations**
python manage.py makemigrations
python manage.py migrate
6. **Create superuser**
python manage.py createsuperuser
# username: admin
# password: 1234
7. **Run server**
python manage.py runserver

---

## 📊 Models Overview

User Profile → Name, Age, Gender, Height, Weight

CaloriesConsumed → Item name, Calories
## Dashboard (Example)

Shows:

Required calories for the day (BMR calculation)

Total consumed calories

Remaining calories
## 👩‍💻 Author

Developed as part of Web Application Development with Python (Level-4) coursework.
