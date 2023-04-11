import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def read_resource_file(file_name):
    with open(f'{dir_path}/resources/{file_name}', 'r') as f:
        return f.read()
