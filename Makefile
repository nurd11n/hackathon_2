run:
	python3 manage.py runserver
migrate:
	python3 manage.py migrate
superuser:
	python3 manage.py createsuperuser
virtual:
	source venv/bin/activate
celery:
	celery -A config worker --loglevel=info
test_account:
	python3 manage.py test applications.account.tests
test_views:
	python manage.py test applications.bilets.tests
run_bot:
	python3 telebot_py.py
run_pars:
	python3 parser.py
