from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("helloworld",
    ["helloworld.pyx"],
    include_dirs=['/home/moshev/.local/include/python3.0'],
    library_dirs=['/home/moshev/.local/lib/python3.0'],)]
)

