import os

def get_file_path(path, get_path=False):
    """ Returns path or multiple file extensions
    :param path: current file path to a file
    :param get_path: bool ot indicate what return to provide
    :return current_path: current path without extensions (filename and directories)
    :return ext: Multiple File extensions of path
    """
    current_path = path
    ext = os.path.splitext(current_path)[1]
    while ("." in current_path):
        current_path = os.path.splitext(current_path)[0]
        ext = (os.path.splitext(current_path)[1] + ext)
    if get_path:
        return current_path
    else:
        return ext