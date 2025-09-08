# TODO for Fixing Deployment Issues on PythonAnywhere

- [x] Verify the existing groups on the PythonAnywhere server to confirm if 'coolshawara' group exists.
- [x] If the group 'coolshawara' does not exist, identify the correct group to use (likely the username or 'users').
- [x] Update any deployment or manual commands to use the correct group for chown.
- [x] Check if the SQLite database file (db.sqlite3) exists in the project directory on the server.
- [x] If the database file does not exist, create it by running `python manage.py migrate`.
- [x] Ensure the database file and project directory have the correct permissions for the web server user.
- [x] Rerun the deployment script to verify that migrations and static file collection succeed without errors.
- [x] Fix virtual environment path mismatch in WSGI configuration
- [x] Update deployment scripts to use correct virtualenv path
- [x] Add chdir to project directory in WSGI file
- [x] Test the Django application to confirm it can connect to the database and run properly.

# Next Steps
- The deployment script has been updated with automatic permission fixes
- WSGI configuration fixed with correct virtualenv path
- Changes have been committed and pushed to GitHub
- Deploy the updated script on PythonAnywhere to test the fixes
- Reload the web app in PythonAnywhere dashboard
- Monitor uWSGI logs for any remaining errors
- Assist with any further troubleshooting if errors persist.
