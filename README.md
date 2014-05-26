# Tada

The last todo list you'll ever need. No, really. We promise.

## Installation

```bash
$ git clone https://github.com/yaymukund/tada-api.git
$ cd tada-api
$ virtualenv env --no-site-packages
$ source env/bin/activate

# This next command will take a second...
$ pip install -r requirements.txt

# Run this in another window and keep it running.
$ make db

$ make migrate
$ make app
$ open http://localhost:8000
```

## Commands

The `Makefile` has everything:

* `make install` - Installs prerequisites using `pip`.
* `make app` - Start a server.
* `make db` - Start the local postgresql server. This presumes you have
              installed postgres under `/usr/local/var/postgres`
* `make migrate` - Blows away all development data and then rebuilds it.
* `make console` - Opens a convenient console that lets you quickly run
                   commands against the database.
* `make sql` - Opens `psql` to the dev database.
* `make test` - Runs tests using `nose`.
