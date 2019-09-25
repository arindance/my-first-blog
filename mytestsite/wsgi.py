"""
WSGI config for mytestsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..' )
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestsite.settings')

#application = get_wsgi_application()