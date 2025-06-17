import os


def get_file_content(working_directory, file_path):
    path = os.path.abspath(os.path.join(working_directory, file_path))
    if path.startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(path) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    try:
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string = file_content_string + f'...File "{file_path}" truncated at 10000 characters'
    except Exception as e:
        return f"Error listing files content: {e}"
    return file_content_string
