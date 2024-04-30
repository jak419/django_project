# django_project
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

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourgithubusername/onlinesales.git
   cd onlinesales

2. **Set Up a Python virtual environment:**
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Configure Redis**
  Ensure Redis is installed and running on your machine. The default configuration expects Redis to be available on localhost on port 6379.

4. **Migrate the database**
  python manage.py migrate

5. **Create a superuser (optional but recommended for accessing the Django admin panel)**
  python manage.py createsuperuser

6. **Running the Project**
  python manage.py runserver
  This will start the Django development server, making the project accessible at http://localhost:8000

7. **Testing**
  Run standard Django tests : python manage.py test
  Run WebSocket tests:  python manage.py test catalog.tests.test_websockets

8. **Logging**
  Actions within the app such as creating, updating, or deleting orders log to CSV files within the catalog/logs directory.
