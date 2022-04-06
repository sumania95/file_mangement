"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
# activate_this = 'D:/Project/file_management/env/Scripts/activate_this.py'
# # execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
#
# application = get_wsgi_application()

import os
import sys
from django.core.wsgi import get_wsgi_application
from pathlib import Path

# Add project directory to the sys.path
path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
	sys.path.append(path_home)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
application = get_wsgi_application()
