.PHONY: app db console test

app:
	gunicorn tada:app

db:
	postgres -D /usr/local/var/postgres

migrate:
	python migrate.py

console:
	python shell.py

sql:
	psql -d tada_dev

test:
	nosetests

install:
	pip install -r requirements.txt
