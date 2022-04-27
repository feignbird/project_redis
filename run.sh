python3 -m venv redis-env
source redis-env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
cd api
python manage.py makemigrations && python manage.py migrate
python manage.py loaddata fixtures/data.json
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8084