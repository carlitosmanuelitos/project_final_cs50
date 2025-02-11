import os
from pathlib import Path
from datetime import datetime

def bundle_code(root_dir='.', output_file='code_bundle.txt', exclude_dirs={'.venv', 'tests', 'node_modules', '__pycache__'}):
    """
    Recursively reads all files in a directory and bundles their contents into a single file.
    
    Args:
        root_dir (str): Root directory to start scanning from
        output_file (str): Name of the output file
        exclude_dirs (set): Set of directory names to exclude
    """
    
    # Text file extensions to include
    text_extensions = {
        '.py', '.js', '.css', '.html', '.txt', '.md', '.json', 
        '.yml', '.yaml', '.ini', '.cfg', '.conf', '.sh', '.env',
        '.django', '.sql', '.jsx', '.tsx', '.ts'
    }
    
    def is_binary(file_path):
        """Check if file is binary by reading its first few bytes"""
        try:
            with open(file_path, 'tr') as check_file:
                check_file.read(1024)
                return False
        except UnicodeDecodeError:
            return True
    
    try:
        with open(output_file, 'w', encoding='utf-8') as bundle:
            # Write header with timestamp
            bundle.write(f"Code Bundle Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            bundle.write("="* 80 + "\n\n")
            
            # Walk through directory tree
            for dirpath, dirnames, filenames in os.walk(root_dir):
                # Remove excluded directories
                dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
                
                # Get relative path
                rel_path = os.path.relpath(dirpath, root_dir)
                
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    extension = os.path.splitext(filename)[1].lower()
                    
                    # Skip if not a text file extension or if it's a binary file
                    if extension not in text_extensions or is_binary(file_path):
                        continue
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            # Write file header
                            bundle.write(f"File: {os.path.join(rel_path, filename)}\n")
                            bundle.write("-" * 80 + "\n")
                            
                            # Write file contents
                            bundle.write(f.read())
                            bundle.write("\n\n" + "=" * 80 + "\n\n")
                            
                    except Exception as e:
                        bundle.write(f"Error reading file {file_path}: {str(e)}\n\n")
                        
        print(f"Bundle created successfully: {output_file}")
        
    except Exception as e:
        print(f"Error creating bundle: {str(e)}")

if __name__ == "__main__":
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Create output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"code_bundle_{timestamp}.txt"
    
    # Set of directories to exclude
    exclude_dirs = {'.venv', 'tests', 'node_modules', '__pycache__'}
    
    # Run the bundler
    bundle_code(current_dir, output_filename, exclude_dirs)