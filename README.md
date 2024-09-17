# HTMX Playground

![alt text](<docs/img/demo.gif>)

Basic CRUD application to handle a list of TODOs to try out HTMX with Django.
Stack:
- Django
- htmx
- tailwind

## Requirements
- [Poetry](https://python-poetry.org/)

## Setup
```bash
poetry install --no-root
poetry shell

cd todo_project
python manage.py migrate
python manage.py runserver

# In another terimanl tab run
python manage.py tailwind start
```

