import os
import urllib.parse  # For encoding spaces in URLs

# GitHub repository URL (replace with your actual GitHub repository URL)
GITHUB_REPO_URL = "https://github.com/Grado-en-Gestion-de-la-Ciberseguridad/1-Ciberseguridad-web/tree/v4/content"  # Modify this URL

# Function to create an Obsidian-style link for .md and .pdf files, including the file extension
def create_obsidian_link(file_name, directory, base_directory):
    # Get the relative path from the base directory to the file
    relative_path = os.path.relpath(os.path.join(directory, file_name), base_directory).replace("\\", "/")
    return f"[[{relative_path}]]"

# Function to create a GitHub link for other file types, handling spaces in filenames
def create_github_link(file_name, directory, base_directory):
    # Get the relative path to the file from the base directory and encode spaces and special characters
    relative_path = os.path.relpath(os.path.join(directory, file_name), base_directory).replace("\\", "/")
    encoded_relative_path = urllib.parse.quote(relative_path)  # Encode spaces and special characters
    return f"[{file_name}]({GITHUB_REPO_URL}/{encoded_relative_path})"

# Function to delete any existing index file
def delete_existing_index_file(directory, index_file_name):
    index_file_path = os.path.join(directory, index_file_name)
    if os.path.exists(index_file_path):
        os.remove(index_file_path)
        print(f"Deleted: {index_file_path}")

# Function to create the index file in each subdirectory
def create_file_index(directory, base_directory):
    # Get directory name
    dir_name = os.path.basename(os.path.abspath(directory))
    index_file_name = f"00. {dir_name}.md"
    index_file_path = os.path.join(directory, index_file_name)

    # List subdirectories, excluding those starting with '.'
    subdirs = [
        d for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d)) and not d.startswith('.')
    ]

    # List files, excluding the index file itself
    files = [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and
           f != index_file_name and
           not (f.startswith("00. ") and f.endswith(".md"))
    ]

    # Prepare content with title and #index tag
    content = f"# File Index for {dir_name}\n#index\n\n"

    # Child directories
    if subdirs:
        content += "## Child Directories\n\n"
        for subdir in sorted(subdirs):
            subdir_index_file = f"00. {subdir}.md"
            subdir_index_full_path = os.path.join(directory, subdir, subdir_index_file)
            # Get the relative path from the base directory to the child index file
            subdir_index_relative_path = os.path.relpath(subdir_index_full_path, base_directory).replace("\\", "/")
            content += f"- [[{subdir_index_relative_path}]]\n"
        content += "\n"

    # Files
    if files:
        content += "## Files\n\n"
        for file in sorted(files):
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.md', '.pdf']:
                # Obsidian link with full relative path from base directory
                link = create_obsidian_link(file, directory, base_directory)
            else:
                # GitHub link with encoded path
                link = create_github_link(file, directory, base_directory)
            content += f"- {link}\n"

    # Write to index file
    try:
        with open(index_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {index_file_path}")
    except Exception as e:
        print(f"Failed to create {index_file_path}: {e}")

# Function to recursively scan directories, delete old index files, and create new ones
def scan_and_create(base_directory):
    for root, dirs, files in os.walk(base_directory):
        # Skip directories that start with '.'
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Determine directory name for index file
        dir_name = os.path.basename(os.path.abspath(root))
        index_file_name = f"00. {dir_name}.md"

        # Delete existing index file before creating a new one
        delete_existing_index_file(root, index_file_name)

        # Create the index file in the current directory
        create_file_index(root, base_directory)

# Main function
if __name__ == "__main__":
    root_directory = "./"  # Specify the root directory to start the scan
    scan_and_create(root_directory)
