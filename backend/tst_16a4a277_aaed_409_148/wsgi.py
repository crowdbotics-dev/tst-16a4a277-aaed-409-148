"""
WSGI config for tst_16a4a277_aaed_409_148 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_16a4a277_aaed_409_148.settings"
)

application = get_wsgi_application()
