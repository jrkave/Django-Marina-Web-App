# Marina Management System

## Introduction

Welcome to Marina, a demo web application designed to streamline marina operations by providing users with tools to manage boat registrations, licenses, and marina space reservations. 
Far from a fully functional, real-world application, this web application is merely reflective of my learning experiences with Django. 

### Key Functionalities

- **User Authentication:** Users can create accounts and log in securely as a result of Django's built-in authentication modules.

- **Boat Registration:** Easily register boats in the system that can later be registered and "rented" into the marina's available spaces.

- **License Management:** Upload valid boat license information before reserving a space on the marina.

- **Boatspace Reservation:** Reserve spaces within the marina for specific boats, ensuring organized and efficient marina management.

- **Dynamic Pages:** The system utilizes dynamic web pages generated through Django templates, providing a user-friendly and responsive interface.

## Database

The system uses an SQLite database, with the database schema defined in `marina/models.py`.

## Views

The views in `marina/views.py` handle various functionalities, including user authentication, boat registration, and marina space reservation.

## URLs

URL patterns and routing logic are defined in `marina/urls.py`. This dictates how different views are mapped to specific URLs.

## Forms

User input is managed through forms defined in `marina/forms.py`. These forms handle data validation and submission.

## Static Files

- **CSS Files**: Styles for different pages (e.g., boat, boatspaces, forms, index, login, profile).
- **Image Files**: Images used in the application (e.g., auth, home, profile, reservations).

## Templates


- **HTML Files**: Templates for different pages (e.g., add_boat, base, boatspace_list, edit_boatspace, index, license, login, profile, registration, signup, success).

## Installation and Setup

### Requirements

- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Setup Instructions

1. Install this project using ```git clone```.  
2. Make sure you are in the directory of this project (Django-Marina) in your terminal. 
3. Install dependencies using Pipenv with the command ```pipenv sync```.
4. Activate the virtual environment with the command ```pipenv shell```.
5. To run the development server, type ```python3 manage.py runserver```.
6. Visit the link provided and add '/marina' add the end of the URL. **Do not** forget this step, or you will get a 404 error. The URL should look something like: http://localhost:8000/marina
7. Explore!





