
#create virtual environment
python -m venv env

#create django project
django-admin startproject drfcommerce

#run local development server
./manage.py runserver

#python shell
python maange.py shell

#generate secret key
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())