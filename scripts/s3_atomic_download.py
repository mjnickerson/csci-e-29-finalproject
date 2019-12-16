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