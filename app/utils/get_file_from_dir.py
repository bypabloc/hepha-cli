from os import path as os_path
from os import listdir as os_listdir


def get_file_from_dir(file_path):
    """
    Get file from dir
    :param file_path: str
    :return: str
    """
    
    if not os_path.exists(file_path):
        raise Exception('File not found')

    if os_path.isfile(file_path):
        return file_path

    if os_path.isdir(file_path):
        files = os_listdir(file_path)
        if len(files) == 0:
            raise Exception('Dir is empty')
        if len(files) > 1:
            raise Exception('Dir has more than one file')
        return os_path.join(file_path, files[0])
