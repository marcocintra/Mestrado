from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as np                           # <---- New line

setup(
    ext_modules=cythonize("*.pyx"),
    annotate=True,
    include_path = [np.get_include()]
)