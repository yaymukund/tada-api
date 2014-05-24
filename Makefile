.PHONY: app db console

app:
	gunicorn tada:app

db:
	postgres -D /usr/local/var/postgres

console:
	python shell.py

sql:
	psql -d tada_dev
