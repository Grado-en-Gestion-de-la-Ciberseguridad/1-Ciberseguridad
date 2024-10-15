import os
import urllib.parse
import argparse
import logging
from pathlib import Path
import subprocess
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# GitHub repository URL (replace with your actual GitHub repository URL)
GITHUB_REPO_URL = "https://github.com/Grado-en-Gestion-de-la-Ciberseguridad/1-Ciberseguridad-web"

# Define the branch name used in GitHub (e.g., 'main' or 'master')
GITHUB_BRANCH = "v4"  # Update if different

# Supported file types for Obsidian links
OBSIDIAN_LINK_EXTENSIONS = {'.md', '.pdf'}

# File types to convert to PDF
CONVERT_TO_PDF_EXTENSIONS = {'.docx', '.pptx'}

# Path to LibreOffice executable (if not in PATH, specify the full path)
LIBREOFFICE_EXECUTABLE = "soffice"  # Assuming 'soffice' is in PATH

def convert_to_pdf(file_path):
    """
    Converts a .docx or .pptx file to PDF using LibreOffice in headless mode.
    The PDF is saved in the same directory as the original file.
    """
    if not shutil.which(LIBREOFFICE_EXECUTABLE):
        logging.error(f"LibreOffice executable '{LIBREOFFICE_EXECUTABLE}' not found in PATH.")
        return None

    try:
        subprocess.run([
            LIBREOFFICE_EXECUTABLE,
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', str(file_path.parent),
            str(file_path)
        ], check=True)
        pdf_file = file_path.with_suffix('.pdf')
        if pdf_file.exists():
            logging.info(f"Converted '{file_path.name}' to '{pdf_file.name}'.")
            return pdf_file
        else:
            logging.error(f"Conversion failed for '{file_path.name}'. PDF not found.")
            return None
    except subprocess.CalledProcessError as e:
        logging.error(f"Error converting '{file_path.name}' to PDF: {e}")
        return None

# Function to create an Obsidian-style link for .md and .pdf files, including the file extension
def create_obsidian_link(file_path, base_directory):
    # Get the relative path from the base directory to the file
    relative_path = file_path.relative_to(base_directory).as_posix()
    return f"[[{relative_path}]]"

# Function to create a GitHub link for other file types, handling spaces in filenames
def create_github_link(file_path, base_directory):
    # Get the relative path to the file from the base directory and encode spaces and special characters
    relative_path = file_path.relative_to(base_directory).as_posix()
    encoded_relative_path = urllib.parse.quote(relative_path)
    # Use 'blob' for files
    github_blob_url = f"{GITHUB_REPO_URL}/blob/{GITHUB_BRANCH}"
    return f"[{file_path.name}]({github_blob_url}/{encoded_relative_path})"

# Function to delete any existing index file
def delete_existing_index_file(directory, index_file_name):
    index_file_path = directory / index_file_name
    if index_file_path.exists():
        index_file_path.unlink()
        logging.info(f"Deleted: {index_file_path}")

# Function to create the index file in each subdirectory
def create_file_index(directory, base_directory):
    dir_name = directory.name
    index_file_name = f"00. {dir_name}.md"
    index_file_path = directory / index_file_name

    # List subdirectories, excluding those starting with '.'
    subdirs = [d for d in directory.iterdir() if d.is_dir() and not d.name.startswith('.')]

    # List files, excluding the index file itself and other index files
    files = [
        f for f in directory.iterdir()
        if f.is_file() and
           f.name != index_file_name and
           not (f.name.startswith("00. ") and f.suffix == ".md")
    ]

    # Prepare content with title and #index tag
    content = f"# File Index for {dir_name}\n#index\n\n"

    # Child directories
    if subdirs:
        content += "## Child Directories\n\n"
        for subdir in sorted(subdirs, key=lambda x: x.name.lower()):
            subdir_index_file = subdir / f"00. {subdir.name}.md"
            if subdir_index_file.exists():
                subdir_index_relative_path = subdir_index_file.relative_to(base_directory).as_posix()
                content += f"- [[{subdir_index_relative_path}]]\n"
            else:
                # If the subdir index doesn't exist yet, create a link to create one later
                content += f"- [[{subdir.name}/00. {subdir.name}.md]]\n"
        content += "\n"

    # Files
    if files:
        content += "## Files\n\n"
        for file in sorted(files, key=lambda x: x.name.lower()):
            ext = file.suffix.lower()
            if ext in CONVERT_TO_PDF_EXTENSIONS:
                # Convert to PDF and index the PDF
                pdf_file = convert_to_pdf(file)
                if pdf_file:
                    link = create_obsidian_link(pdf_file, base_directory)
                else:
                    # If conversion fails, fallback to GitHub link to original file
                    link = create_github_link(file, base_directory)
            elif ext in OBSIDIAN_LINK_EXTENSIONS:
                # Obsidian link with full relative path from base directory
                link = create_obsidian_link(file, base_directory)
            else:
                # GitHub link with encoded path
                link = create_github_link(file, base_directory)
            content += f"- {link}\n"

    # Write to index file
    try:
        index_file_path.write_text(content, encoding='utf-8')
        logging.info(f"Created: {index_file_path}")
    except Exception as e:
        logging.error(f"Failed to create {index_file_path}: {e}")

# Function to recursively scan directories, delete old index files, and create new ones
def scan_and_create(base_directory):
    base_path = Path(base_directory).resolve()
    for directory in base_path.rglob('*'):
        if directory.is_dir() and not directory.name.startswith('.'):
            # Determine index file name
            index_file_name = f"00. {directory.name}.md"

            # Delete existing index file before creating a new one
            delete_existing_index_file(directory, index_file_name)

            # Create the index file in the current directory
            create_file_index(directory, base_path)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Generate Obsidian index files for a GitHub repository, converting .docx and .pptx files to PDF.")
    parser.add_argument(
        'root_directory',
        nargs='?',
        default='.',
        help='Root directory to start the scan (default: current directory)'
    )
    args = parser.parse_args()
    scan_and_create(args.root_directory)

if __name__ == "__main__":
    main()
