import os


def write_file(working_directory, file_path, content):
    path = os.path.abspath(os.path.join(working_directory, file_path))
    if path.startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(path):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(path) and os.path.isdir(path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error writing to file: {e}"