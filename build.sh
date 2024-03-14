#!/bin/bash

# Establecer las variables de entorno
export PGDATABASE="persona"
export PGHOST="ep-yellow-sun-a20bfr41.eu-central-1.aws.neon.tech"
export PGPASSWORD="WQjce6b7izlA"
export PGUSER="ignacio.nunnez"

echo "Variables de entorno establecidas:"
echo "PGDATABASE=$PGDATABASE"
echo "PGHOST=$PGHOST"
echo "PGPASSWORD=$PGPASSWORD"
echo "PGUSER=$PGUSER"

#crear superusuario
python3 manage.py createsuperuser --noinput --username alumnodb --email alumnodb@alumnodb.com --password alumnodb