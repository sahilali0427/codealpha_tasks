# Event Registration System

A simple web-based Event Registration System built using Django and MySQL. This project allows users to create an account, log in, browse available events, register for events, and manage their registrations. It was developed as a learning project to gain practical experience in full-stack web development using Django.

## Features

* User Registration and Login
* View Available Events
* Search Events by Name
* Register for Events
* View My Registrations
* Cancel Event Registrations
* Admin Panel for Managing Events and Registrations
* MySQL Database Integration

## Technologies Used

### Frontend

* HTML
* CSS

### Backend

* Python
* Django

### Database

* MySQL

## Database Design

### Event Table

* Event Name
* Description
* Venue
* Date

### Registration Table

* User
* Event

## How to Run the Project

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd event_system
```

3. Install required packages

```bash
pip install django mysqlclient
```

4. Configure MySQL database settings in `settings.py`

5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create an admin account

```bash
python manage.py createsuperuser
```

7. Start the server

```bash
python manage.py runserver
```

8. Open the browser

```text
http://127.0.0.1:8000
```

## Learning Outcomes

Through this project, I learned:

* Django project structure
* URL routing and views
* User authentication
* Database integration with MySQL
* Django ORM
* CRUD operations
* Template rendering
* Basic frontend design using HTML and CSS

## Future Improvements

* Email notifications for registrations
* Event categories
* User profile management
* Event capacity management
* Responsive mobile-friendly design
