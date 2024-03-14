#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    import os
    import django

    # Establecer las variables de entorno aquí
    os.environ.setdefault("PGDATABASE", "persona")
    os.environ.setdefault("PGUSER", "ignacio.nunnez")
    os.environ.setdefault("PGPASSWORD", "WQjce6b7izlA")
    os.environ.setdefault("PGHOST", "ep-yellow-sun-a20bfr41.eu-central-1.aws.neon.tech")

    # Resto del código para iniciar Django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
