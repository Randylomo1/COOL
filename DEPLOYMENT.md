# Django Deployment Guide for PythonAnywhere

This guide provides step-by-step instructions for deploying the "coolshawara" Django project to PythonAnywhere.

## Prerequisites

- PythonAnywhere account (Hacker plan or higher recommended for production)
- Git repository with your Django project
- Basic knowledge of PythonAnywhere interface

## 1. Project Setup on PythonAnywhere

### 1.1 Clone Your Repository
```bash
git clone https://github.com/yourusername/coolshawara.git
cd coolshawara
```

### 1.2 Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 1.3 Install Dependencies
```bash
pip install -r requirements.txt
```

### 1.4 Run Initial Setup
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## 2. Environment Variables Setup

Set the following environment variables in PythonAnywhere:

### Via Web Interface:
1. Go to PythonAnywhere Dashboard
2. Navigate to "Web" tab
3. Click on your web app
4. Go to "Environment variables" section
5. Add the following variables:

```
SECRET_KEY=your-very-long-random-secret-key-here
DEBUG=False
DATABASE_URL=sqlite:///home/yourusername/coolshawara/db.sqlite3
```

### Or via Console:
```bash
# In your PythonAnywhere bash console
echo "export SECRET_KEY='your-very-long-random-secret-key-here'" >> ~/.bashrc
echo "export DEBUG=False" >> ~/.bashrc
echo "export DATABASE_URL='sqlite:///home/yourusername/coolshawara/db.sqlite3'" >> ~/.bashrc
source ~/.bashrc
```

**Important:** Replace `yourusername` with your actual PythonAnywhere username.

## 3. Database Configuration

### Option 1: SQLite (Current Setup)
- No additional configuration needed
- Suitable for small applications
- Limitations: Not ideal for high-traffic sites

### Option 2: MySQL (Recommended for Production)
1. Create MySQL database in PythonAnywhere
2. Update DATABASE_URL:
```
DATABASE_URL=mysql://yourusername:password@yourusername.mysql.pythonanywhere-services.com/yourusername$databasename
```

## 4. Static Files Configuration

The project is already configured with:
- WhiteNoise middleware for static file serving
- STATIC_ROOT set to `/home/yourusername/COOL/staticfiles`

### Collect Static Files:
```bash
python manage.py collectstatic --noinput
```

## 5. WSGI Configuration

### 5.1 Create WSGI File
In PythonAnywhere Web tab, create/update the WSGI configuration file:

```python
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/yourusername/coolshawara'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolshawara.settings'

# Set the virtual environment
activate_this = '/home/yourusername/coolshawara/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import your Django project
import django
django.setup()

# Import the WSGI application
from coolshawara.wsgi import application
```

### 5.2 Update Web App Configuration
- **Source code:** `/home/yourusername/coolshawara`
- **Working directory:** `/home/yourusername/coolshawara`
- **WSGI configuration file:** `/var/www/yourusername_pythonanywhere_com_wsgi.py`
- **Virtualenv:** `/home/yourusername/coolshawara/venv`

## 6. Security Considerations

### 6.1 HTTPS Enforcement
PythonAnywhere provides free SSL certificates. Ensure:
- Force HTTPS is enabled in Web tab
- Update CSRF_TRUSTED_ORIGINS if needed

### 6.2 Secret Key
- Never commit SECRET_KEY to version control
- Use a long, random string for production
- Rotate keys periodically

### 6.3 Debug Mode
- Ensure DEBUG=False in production
- Remove debug information from error pages

## 7. Deployment Checklist

- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Environment variables set
- [ ] Database configured and migrated
- [ ] Static files collected
- [ ] WSGI configuration updated
- [ ] Web app reloaded
- [ ] HTTPS enabled
- [ ] Site tested

## 8. Troubleshooting

### Common Issues:

1. **ImportError: No module named 'xyz'**
   - Ensure all dependencies are installed in virtualenv
   - Check requirements.txt is complete

2. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Verify STATIC_ROOT path
   - Check WhiteNoise configuration

3. **Database connection errors**
   - Verify DATABASE_URL format
   - Check database credentials
   - Ensure database exists

4. **WSGI errors**
   - Check WSGI file paths
   - Verify DJANGO_SETTINGS_MODULE
   - Ensure virtualenv is activated in WSGI

### Logs:
- Check PythonAnywhere error logs in Web tab
- Use `python manage.py check --deploy` for deployment checks

## 9. Maintenance

### Updating Code:
```bash
cd coolshawara
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

### Reloading Web App:
- Go to PythonAnywhere Web tab
- Click "Reload" button

### Backup:
- Regularly backup database
- Keep code in version control
- Document configuration changes

## 10. Performance Optimization

- Use PythonAnywhere's paid plans for better performance
- Consider using Redis for caching
- Optimize static files delivery
- Monitor resource usage

## Support

For PythonAnywhere specific issues:
- Check PythonAnywhere help pages
- Use their forums
- Contact support for account-specific issues

For Django deployment issues:
- Refer to Django documentation
- Check Django security checklist
- Use `python manage.py check --deploy`
