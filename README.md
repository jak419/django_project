# CIDM6330_project
Online Sales Systems written in Django

# Catalog App
The Catalog app is part of the `onlinesales` Django project. It manages product listings, customer interactions, and order processing, incorporating real-time features through Django Channels.

## Prerequisites
Before you can run this project, you'll need to have the following installed:
- Python 3.8 or higher
- Django 3.2 or higher
- Django Channels
- Redis (for WebSocket support)

Follow these steps to get your development environment set up:

1. **Clone the repository :**
   ```bash
   git clone https://github.com/yourgithubusername/onlinesales.git
   cd onlinesales

2. **Set Up a Python virtual environment :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. **Configure Redis :**
  Ensure Redis is installed and running on your machine. The default configuration expects Redis to be available on localhost on port 6379.

5. **Migrate the database :**
      ```bash
   python manage.py migrate

6. **Create a superuser (optional but recommended for accessing the Django admin panel) and signing in:**
      ```bash
   python manage.py createsuperuser
- Alternatively, you can log create a user on the 'sign in' screen as a customer.

7. **Running the Project :**
  python manage.py runserver
  This will start the Django development server, making the project accessible at http://localhost:8000

8. **Testing :**
      ```bash
      Run standard Django tests : python manage.py test
      Run WebSocket tests:  python manage.py test catalog.tests.test_websockets

9. **Logging :**
  Actions within the app such as creating, updating, or deleting orders log to CSV files within the catalog/logs directory.
