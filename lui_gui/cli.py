import argparse
from luigi import build
from .ccs.{{cookiecutter.dag_name}}.tasks.tasks import Run_lui_gui

parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument("-i", "--image", default="luigi.jpg") # what torch model to use
parser.add_argument("-m", "--model", default="mosaic.pth") # what image to stylize
parser.add_argument("-r", "--root", default="data") # subdirectory for model


def main_script(args=None):
    args = parser.parse_args(args=args)

    build([
        Run_lui_gui(args.model, args.root)
    ], local_scheduler=True)