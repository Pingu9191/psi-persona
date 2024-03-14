# gunicorn.conf.py

import os

def on_starting(server):
    os.environ["PGDATABASE"] = "persona"
    os.environ["PGHOST"] = "ep-yellow-sun-a20bfr41.eu-central-1.aws.neon.tech"
    os.environ["PGPASSWORD"] = "WQjce6b7izlA"
    os.environ["PGUSER"] = "ignacio.nunnez"
