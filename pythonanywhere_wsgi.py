# PythonAnywhere WSGI Configuration for coolshawara
# Copy this content to your PythonAnywhere WSGI configuration file
# Usually located at: /var/www/coolshawara_pythonanywhere_com_wsgi.py

import os
import sys

# Add your project directory to the sys.path
project_home = '/home/coolshawara/COOL'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Change to project directory
os.chdir(project_home)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolshawara.settings'

# Set the virtual environment
activate_this = '/home/coolshawara/.virtualenvs/coolshawara/bin/activate_this.py'
import os
if not os.path.exists(activate_this):
    activate_this = '/home/coolshawara/COOL/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import your Django project
import django
django.setup()

# Import the WSGI application
from coolshawara.wsgi import application
