import os

# Define all directories to be created (relative to the project root)
directories = [
    "health_tracker_project",
    "health_tracker_project/health_tracker",
    "health_tracker_project/apps",
    "health_tracker_project/apps/core",
    "health_tracker_project/apps/core/migrations",
    "health_tracker_project/apps/core/templates",
    "health_tracker_project/apps/core/templates/core",
    "health_tracker_project/apps/users",
    "health_tracker_project/apps/users/migrations",
    "health_tracker_project/apps/users/templates",
    "health_tracker_project/apps/users/templates/users",
    "health_tracker_project/static",
    "health_tracker_project/static/css",
    "health_tracker_project/static/js",
    "health_tracker_project/static/images",
    "health_tracker_project/templates",
]

# Define all files to be created (files can be left blank)
files = [
    "health_tracker_project/Dockerfile",
    "health_tracker_project/docker-compose.yml",
    "health_tracker_project/requirements.txt",
    "health_tracker_project/.env",
    "health_tracker_project/manage.py",
    # Project package files
    "health_tracker_project/health_tracker/__init__.py",
    "health_tracker_project/health_tracker/settings.py",
    "health_tracker_project/health_tracker/urls.py",
    "health_tracker_project/health_tracker/wsgi.py",
    # Core app files
    "health_tracker_project/apps/core/__init__.py",
    "health_tracker_project/apps/core/admin.py",
    "health_tracker_project/apps/core/apps.py",
    "health_tracker_project/apps/core/migrations/__init__.py",
    "health_tracker_project/apps/core/models.py",
    "health_tracker_project/apps/core/views.py",
    "health_tracker_project/apps/core/urls.py",
    "health_tracker_project/apps/core/templates/core/dashboard.html",
    "health_tracker_project/apps/core/templates/core/food_diary.html",
    "health_tracker_project/apps/core/templates/core/goals.html",
    "health_tracker_project/apps/core/templates/core/diet_database.html",
    "health_tracker_project/apps/core/templates/core/ai_insights.html",
    "health_tracker_project/apps/core/templates/core/tips.html",
    # Users app files
    "health_tracker_project/apps/users/__init__.py",
    "health_tracker_project/apps/users/admin.py",
    "health_tracker_project/apps/users/apps.py",
    "health_tracker_project/apps/users/migrations/__init__.py",
    "health_tracker_project/apps/users/models.py",
    "health_tracker_project/apps/users/views.py",
    "health_tracker_project/apps/users/forms.py",
    "health_tracker_project/apps/users/urls.py",
    "health_tracker_project/apps/users/templates/users/login.html",
    "health_tracker_project/apps/users/templates/users/register.html",
    "health_tracker_project/apps/users/templates/users/profile.html",
    # Static assets
    "health_tracker_project/static/css/tailwind.css",
    "health_tracker_project/static/js/main.js",
    # Global templates
    "health_tracker_project/templates/base.html",
]

def create_directories(dirs):
    """Create directories from the provided list."""
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_files(file_list):
    """Create blank files from the provided list."""
    for filepath in file_list:
        # Ensure the parent directory exists (should be covered by our directories list)
        parent_dir = os.path.dirname(filepath)
        os.makedirs(parent_dir, exist_ok=True)
        # Create the file (or overwrite with blank content)
        with open(filepath, "w") as f:
            pass  # Leaving the file blank
        print(f"Created file: {filepath}")

if __name__ == "__main__":
    create_directories(directories)
    create_files(files)
    print("\nDirectory structure created successfully.")
