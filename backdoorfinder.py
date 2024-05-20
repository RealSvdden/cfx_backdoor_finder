import os
import re

def read_file_with_encodings(file_path, encodings=['utf-8', 'latin-1', 'iso-8859-1']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    return None

def search_files(directory, patterns, output_file):
    with open(output_file, 'w') as output:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".lua"):
                    file_path = os.path.join(root, file)
                    content = read_file_with_encodings(file_path)
                    if content:
                        for pattern in patterns:
                            matches = re.finditer(pattern, content)
                            for match in matches:
                                line_number = content.count('\n', 0, match.start()) + 1
                                output.write(f"Match found in {file_path}, line {line_number}: {match.group()}\n")

patterns = [
    r'\\x[0-9a-fA-F]{2}',
    r'[A-Za-z]{20,}',
    r'PerformHttpRequest',
    r'assert',
    r'load',
    r'_G'
]

project_path = r'C:\GTAFXServer' # Path to the project folder
output_file = 'matches.txt'

search_files(project_path, patterns, output_file)
