                                                      Idea Management Tool


View website here: http://ideatoolmanagement.pythonanywhere.com/


### Installation:

Requirements:

- Python 3 runtime
- Django==3.2.6
- django-crispy-forms==1.12.0

- Other dependencies in `requirements_personal.txt`

Procedure:


Follow these steps:

```
git clone https://github.com/Hemanth-Gattu/Production_House_Management.git
```


Setup Locally:

Make sure you have python 3 and pipenv installed on your pc.

Then follow these steps:

```
cd <project-directory>/backend/

cp .env.example .env

(use 'copy' instead of 'cp' in windows)
```

```
pipenv install --dev
```

- Activate the new virtual environment:

```
pipenv shell
```

- cd into project:

```
cd Idea_Management_Tool/
```

- Make database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser

```
python manage.py createsuperuser
```

- Run development server on localhost

```
python manage.py runserver
```

#### Dummy Data for Testing [OPTIONAL]:

This will populate the database with random values for testing:

```
python manage.py createfixture
```
