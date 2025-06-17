import os


def get_files_info(working_directory, directory=None):
    path = os.path.abspath(working_directory)
    if directory:
        path = os.path.abspath(os.path.join(working_directory, directory))

    if path.startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(path) == False:
        return f'Error: "{directory}" is not a directory'
    
    content = os.listdir(path)
    try:
        represent_lst = []
        for item in content:
            item_path = os.path.abspath(os.path.join(working_directory, os.path.join(directory, item)))
            size_item = os.path.getsize(item_path)
            represent_lst.append(f"- {item}: file_size={size_item} bytes, is_dir={os.path.isdir(item_path)}")
        return "\n".join(represent_lst)
    except Exception as e:
        return f"Error listing files: {e}"
    
