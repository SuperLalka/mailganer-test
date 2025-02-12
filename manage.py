#!/usr/bin/env python

import os
import sys
from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    # https://stackoverflow.com/a/35392978
    os.environ.setdefault('C_FORCE_ROOT', 'true')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "app"))

    execute_from_command_line(sys.argv)
