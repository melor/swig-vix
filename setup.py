from setuptools import setup, find_packages, Extension

vixc_module = Extension('vix._vixc',
                       sources=['src/vixc.i'],
                       swig_opts=['-modern', '-I/usr/include',
                                  '-lcpointer.i', '-outdir', 'vix/'],
                       libraries=["vixAllProducts"],
                       library_dirs=["/usr/include/vmware-vix"],
                       )

setup(
    name = 'vix',
    version = '0.1',
    ext_modules = [vixc_module],
    packages = find_packages(),
    )
