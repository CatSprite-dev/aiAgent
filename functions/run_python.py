import os
import subprocess


def run_python_file(working_directory, file_path, args = None):
    path = os.path.abspath(os.path.join(working_directory, file_path))
    if path.startswith(os.path.abspath(working_directory)) == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(path) == False:
        return f'Error: File "{file_path}" not found.'
    if file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python3", file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(commands, timeout = 30, capture_output = True, cwd=os.path.abspath(working_directory), text=True)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if len(output) == 0:
            return "No output produced"
        return " ".join(output)

    except Exception as e:
        f"Error: executing Python file: STDERR:{e}"
    