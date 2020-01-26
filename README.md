 # Django CRUD with Class Based Views

## About

Building a simple CRUD with Django and Class Based Views. You can find more details at <https://blog.albertosenna.com/2020/01/26/django-crud-with-class-based-views/>.

## Installation
- Clone the repository:
```shell
git clone https://github.com/albertosdneto/django_simple_crud_cbv.git
```
- Enter the folder and create a virtual environment with python 3.6.
```shell
cd django_simple_crud_cbv
python3 -m venv venv
```
- Activate the virtual environment you have just created:
```shell
source venv/bin/activate
```
- Upgrade the virtual environment you have just activated:
```shell
pip install --upgrade pip setuptools
```
- Install the requirements:
```shell
pip install -r requirements.txt
```

- Migrate database:
```shell
python manage.py makemigrations
python manage.py migrate
```
- Run the project:
```shell
python manage.py runserver
```
- Go to the project url <http://127.0.0.1:8000/> and verify if it is running.

Good luck!

