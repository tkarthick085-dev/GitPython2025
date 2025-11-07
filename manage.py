#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    global execute_from_command_line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjangoProject.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        ...
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

