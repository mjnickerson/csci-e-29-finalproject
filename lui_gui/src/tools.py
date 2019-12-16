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

def s3_atomic_download(self):
    """
    download a file from S3Target to LocalTarget
    :param self.input(): an input S3Target to download
    :param self.output(): an output LocalTarget to download to
    """
    with self.input().open('r')as model_in:
        temp_file = model_in.read()
    with self.output().open('w') as model_out:
        model_out.write(temp_file)