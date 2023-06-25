from os import path as os_path
from os import listdir as os_listdir


def get_name_dirs_from_dir(dir_path):
    """
    Obtiene los nombres de los directorios de un directorio
    :param dir_path: str
    :return: list
    """
    return [name for name in os_listdir(dir_path) if os_path.isdir(os_path.join(dir_path, name))]