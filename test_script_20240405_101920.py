import os
import re
from PyPDF2 import PdfReader

def sanitize_filename(name):
    """
    Sanitize the file name by removing or replacing characters that are not allowed in file names.
    """
    return re.sub(r'[\\/*?:"<>|]', "", name)

def pdf_to_txt_converter(source_folder, target_folder="output"):
    """
    Converts all PDF files in the source folder to text files in the target folder.
    Automatically creates an output folder if not specified.
    """
    # Ensure target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.pdf'):
            # Construct full file path
            source_path = os.path.join(source_folder, filename)
            # Read PDF content
            try:
                reader = PdfReader(source_path)
                text_content = ''
                for page in reader.pages:
                    text_content += page.extract_text() + '\n'
                # Sanitize and construct target file name
                target_filename = sanitize_filename(filename[:-4] + '.txt')
                target_path = os.path.join(target_folder, target_filename)
                # Write text content to target file
                with open(target_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(text_content)
                print(f"Converted '{filename}' to '{target_filename}' successfully.")
            except Exception as e:
                print(f"Failed to convert '{filename}'. Error: {e}")

# Example usage
pdf_to_txt_converter('books')
