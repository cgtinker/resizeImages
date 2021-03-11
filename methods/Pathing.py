import os


def create_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        print("created directory at:", directory)
        os.makedirs(directory)


def get_unique_paths(output_type_dict):
    tmp_paths = []
    for entry in output_type_dict:
        tmp_paths.append(entry.sub_path)

    unique_paths = set(tmp_paths)
    return unique_paths


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def get_dir_name(path):
    return os.path.dirname(path)


def get_files_in_dir(path):
    return os.listdir(path)


def join_paths(a, b):
    return os.path.join(a, b)


def remove_extension(path):
    return os.path.splitext(path)[0]
