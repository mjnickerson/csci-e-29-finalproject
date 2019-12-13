import os
from luigi.contrib.external_program import ExternalProgramTask
from luigi import format, Parameter, WrapperTask, ExternalTask, Task, LocalTarget
from luigi.contrib.s3 import S3Target
from lui_gui.io.target import SuffixPreservingLocalTarget
from lui_gui.io import s3_atomic_download


class Run_lui_gui(WrapperTask):
    """
    Wrapper Task - to set Parameters for file download
    """
    file = Parameter()
    root = Parameter()
    print(root)
    def run(self):
        print("Running Lui_GUI graph!")

    def requires(self):
        file = self.file
        root = self.root
        return {{cookiecutter.node_4}}(file,root)


class {{cookiecutter.node_2}}(ExternalTask):
    # Fetch S3Target for External File on S3
    MODEL_ROOT = os.environ.get("MODEL_ROOT")  # Root S3 path, as a constant

    model = Parameter() # Filename of the model under the root s3 path

    def output(self):
        return S3Target(os.path.join(self.MODEL_ROOT, self.model),format=format.Nop) #this is node_1


class {{cookiecutter.node_3}}(Task):
    # Download to Local Target
    file = Parameter()
    root = Parameter()
    LOCAL_ROOT = os.path.abspath("temp_run_stylize_subdir") #default root in case of failure
    S3_ROOT = os.environ.get("S3_ROOT")
    SHARED_RELATIVE_PATH = 'saved_models'

    def requires(self):
        # Depends on the SavedModel ExternalTask being complete
        return {{cookiecutter.node_2}}(self.file)

    def run(self):
        {{cookiecutter.node_3_run}})self
        # Atomically copy the file locally
        # s3_atomic_download(self)

    def output(self):
        self.LOCAL_ROOT = os.path.abspath(self.root) #set root directory for LocalTarget
        return LocalTarget((os.path.join(self.LOCAL_ROOT, self.SHARED_RELATIVE_PATH, self.file)),format=format.Nop)


class {{cookiecutter.node_4}}(ExternalProgramTask):
    """
    Stylize image with specified torch model
    """
    file = Parameter() #file name
    root = Parameter()  #subdirectory for model
    LOCAL_ROOT = os.path.abspath("temp_run_stylize_subdir")
    output_dir_name = 'stylized_images'
    output_dir = (os.path.join(LOCAL_ROOT, output_dir_name))


    def requires(self):
        """ Requires Model and Image already downloaded
        :return model: Local Target of Model
        :return image: Local Target of Image
        Note: passes Luigi Parameters for model and image
        """
        return {
            'model': {{cookiecutter.node_3}}(self.file, self.root),
        }


    def program_args(self):
        """ Command line arguments to call torch model
        :return args: CLI args
        """
        return ['python','-m','neural_style', 'eval', '--content-image', os.path.join(self.LOCAL_ROOT, {{cookiecutter.node_3}}.SHARED_RELATIVE_PATH, self.image) ,'--model',
                os.path.join(self.LOCAL_ROOT, {{cookiecutter.node_3}}.SHARED_RELATIVE_PATH, self.file) ,'--output-image', self.temp_output_path ,'--cuda', '0']

    def run(self):
        # torch neural_style write does not create missing directories
        if not os.path.exists(self.output_dir):  # if missing
            os.makedirs(self.output_dir) # create dir
        with self.output().temporary_path() as self.temp_output_path: # atomic write
            super().run()

    def output(self):
        self.LOCAL_ROOT = os.path.abspath(self.root) #set root directory for SufPresLocTarg
        self.output_dir = (os.path.join(self.LOCAL_ROOT, self.output_dir_name)) #set output directory for SufPresLocTarg
        # return SuffixPreservingLocalTarget of the stylized image
        output_file_name = (os.path.splitext(self.file)[0]+"_processed")
        return SuffixPreservingLocalTarget(os.path.join(self.output_dir, output_file_name),format=format.Nop)
