"""
WSGI config for sprinto_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

project_folder = os.path.dirname(__file__)
load_dotenv(os.path.join(project_folder, 'sprinto_proj.settings'))



application = get_wsgi_application()
