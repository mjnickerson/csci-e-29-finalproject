import random
import io
from contextlib import contextmanager
from luigi.local_target import LocalTarget, atomic_file
from luigi.format import FileWrapper, get_default_format
from lui_gui.src.tools import get_file_path


class suffix_preserving_atomic_file(atomic_file):
    def generate_tmp_path(self, path):
        #keep base file extensions
        return (((get_file_path(path,True) + '-tmp-%09d' + (get_file_path(path,False))) % random.randrange(0, 1e10)))


class BaseAtomicProviderLocalTarget(LocalTarget):
    # Allow some composability of atomic handling
    atomic_provider = atomic_file

    def open(self, mode='r'):
        # leverage super() as well as modifying any code in LocalTarget
        # to use self.atomic_provider rather than atomic_file
        rwmode = mode.replace('b', '').replace('t', '')
        if rwmode == 'w':
            self.makedirs()
            return self.format.pipe_writer(self.atomic_provider(self.path))

        elif rwmode == 'r':
            fileobj = FileWrapper(io.BufferedReader(io.FileIO(self.path, mode)))
            return self.format.pipe_reader(fileobj)

        else:
            raise Exception("mode must be 'r' or 'w' (got: %s)" % mode)


    @contextmanager
    def temporary_path(self):
        # NB: unclear why LocalTarget doesn't use atomic_file in its implementation
        self.makedirs()
        with self.atomic_provider(self.path) as af:
            yield af.tmp_path


class SuffixPreservingLocalTarget(BaseAtomicProviderLocalTarget):
    atomic_provider = suffix_preserving_atomic_file