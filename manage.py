#!/usr/bin/env python
"""Django loyihasini boshqarish uchun buyruq qatori vositasi."""
import os
import sys


def main():
    """Django buyruqlarini bajarish (runserver, migrate va h.k.)."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homehub.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django o'rnatilmagan. Virtual environment faollashtirilganini "
            "va 'pip install -r requirements.txt' bajarilganini tekshiring."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
