#!/bin/bash
# Final Django Deployment Script for PythonAnywhere
# This script handles the complete deployment process

set -e  # Exit on any error

echo "🚀 Starting Django Deployment for PythonAnywhere"
echo "================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="/home/coolshawara/COOL"
VENV_DIR="/home/coolshawara/.virtualenvs/coolshawara"
PYTHON_VERSION="python3.9"

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're on PythonAnywhere
if [[ ! -d "/home/coolshawara" ]]; then
    print_error "This script is designed for PythonAnywhere environment"
    print_error "Please run this on PythonAnywhere or modify paths accordingly"
    exit 1
fi

cd "$PROJECT_DIR" || exit 1

print_status "Working directory: $(pwd)"

# Step 1: Create necessary directories
print_status "Creating necessary directories..."
mkdir -p static/css
mkdir -p staticfiles
print_status "Directories created successfully"

# Step 2: Activate virtual environment
print_status "Activating virtual environment..."
source "$VENV_DIR/bin/activate"
print_status "Virtual environment activated"

# Step 3: Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Step 4: Install requirements
print_status "Installing requirements..."
pip install -r requirements.txt
print_status "Requirements installed successfully"

# Step 5: Set environment variables
print_status "Setting environment variables..."
export SECRET_KEY="${SECRET_KEY:-django-insecure-change-this-in-production}"
export DEBUG="${DEBUG:-False}"
export DATABASE_URL="${DATABASE_URL:-sqlite:///$PROJECT_DIR/db.sqlite3}"
print_status "Environment variables set"

# Step 6: Ensure database file exists
if [[ ! -f "$PROJECT_DIR/db.sqlite3" ]]; then
    print_status "Creating database file..."
    touch "$PROJECT_DIR/db.sqlite3"
    print_status "Database file created"
fi

# Step 6.5: Fix database file permissions and ownership
print_status "Setting database file permissions..."
chown coolshawara:coolshawara "$PROJECT_DIR/db.sqlite3" 2>/dev/null || chown coolshawara:users "$PROJECT_DIR/db.sqlite3" 2>/dev/null || print_warning "Could not set ownership, continuing..."
chmod 664 "$PROJECT_DIR/db.sqlite3"
print_status "Database file permissions set"

# Step 7: Run database migrations
print_status "Running database migrations..."
python manage.py migrate
print_status "Database migrations completed"

# Step 8: Collect static files
print_status "Collecting static files..."
python manage.py collectstatic --noinput --clear
print_status "Static files collected successfully"

# Step 9: Create superuser (optional)
if [[ "$CREATE_SUPERUSER" == "true" ]]; then
    print_status "Creating superuser..."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell
    print_warning "Superuser created with username: admin, password: admin123"
    print_warning "Please change the password after first login!"
fi

# Step 10: Run security check
print_status "Running Django security check..."
python manage.py check --deploy

# Step 11: Test the application
print_status "Testing application startup..."
timeout 10 python manage.py runserver 127.0.0.1:8000 &
SERVER_PID=$!
sleep 5
if kill -0 $SERVER_PID 2>/dev/null; then
    print_status "Application started successfully"
    kill $SERVER_PID
else
    print_error "Application failed to start"
    exit 1
fi

print_status ""
print_status "🎉 DEPLOYMENT COMPLETED SUCCESSFULLY!"
print_status ""
print_status "Next steps:"
print_status "1. Go to PythonAnywhere Web tab"
print_status "2. Create a new web app or modify existing one"
print_status "3. Set the following configuration:"
print_status "   - Source code: $PROJECT_DIR"
print_status "   - Working directory: $PROJECT_DIR"
print_status "   - Virtualenv: $VENV_DIR"
print_status "   - WSGI file: $PROJECT_DIR/pythonanywhere_wsgi.py"
print_status "4. Reload the web app"
print_status ""
print_status "Your Django application should now be live!"
print_status ""

# Optional: Create a simple status check
print_status "Creating deployment status file..."
cat > deployment_status.txt << EOF
Django Deployment Status
========================
Date: $(date)
Project: coolshawara
Environment: PythonAnywhere
Status: SUCCESS

Configuration:
- Project Directory: $PROJECT_DIR
- Virtual Environment: $VENV_DIR
- Static Root: $PROJECT_DIR/staticfiles
- Database: SQLite (default)

Next Steps:
1. Configure web app in PythonAnywhere dashboard
2. Set WSGI configuration file
3. Reload web app
4. Test your application

Environment Variables Set:
- SECRET_KEY: ${SECRET_KEY:0:10}...
- DEBUG: $DEBUG
- DATABASE_URL: ${DATABASE_URL:0:20}...
EOF

print_status "Deployment status saved to deployment_status.txt"
print_status ""
print_status "🚀 Deployment script completed successfully!"
