
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

#environment variables configuration
from dotenv import load_dotenv
load_dotenv()

#pytest coverage
pip install coverage
pip install pytest-cov
pytest
coverage run -m pytest
coverage html 
pytest --cov


#django spectacular
pip install django-spectacular  
pip install drf-spectacular
python manage.py spectacular --file schema.yml

