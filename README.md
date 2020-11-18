git clone https://github.com/TurkinDV/weather.git

cd weather

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

Любой логин, email и пароль

python manage.py runserver
