import os

def list_directory_structure(base_path, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {'.venv', 'tests'}
    
    directory_structure = {}

    # Walk through the directory
    for root, dirs, files in os.walk(base_path):
        # Get the relative path to the base path
        relative_root = os.path.relpath(root, base_path)
        
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        # Skip the base directory itself
        if relative_root == '.':
            continue

        # Build the directory structure dictionary
        directory_structure[relative_root] = {
            "dirs": dirs,
            "files": files
        }

    return directory_structure


def print_directory_structure(structure, indent=0):
    for directory, contents in structure.items():
        print("  " * indent + f"{directory}/")
        
        # Print directories
        for subdir in contents['dirs']:
            print("  " * (indent + 1) + f"{subdir}/")

        # Print files
        for file in contents['files']:
            print("  " * (indent + 1) + file)


# Get the current directory
base_path = os.getcwd()

# Get the directory structure, excluding .venv and tests
structure = list_directory_structure(base_path)

# Print the structure
print_directory_structure(structure)
