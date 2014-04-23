import sys
import numpy
import os
import sphinx
import sphinx.apidoc
import urllib
import warnings
import setuptools
import setuptools.command.develop


class SphinxCommandProxy(setuptools.Command):
    user_options = []
    description = 'sphinx'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # metadata contains information supplied in setup()
        metadata = self.distribution.metadata
        src_dir = (self.distribution.package_dir or {'': ''})['']
        src_dir = os.path.join(os.getcwd(),  src_dir)

        # Build docs from docstrings in *.py files
        sphinx.apidoc.main(
            ['',
             '-o', os.path.join('docs', 'source','api'), src_dir])

        # Build the doc sources
        sphinx.main(['', '-c', 'docs',
                     '-D', 'project=' + metadata.name,
                     '-D', 'version=' + metadata.version,
                     '-D', 'release=' + metadata.version,
                     os.path.join('docs', 'source'),
                     os.path.join('docs', 'build')])


setuptools.setup(
    # Name of the project
    name='frft',

    # Version
    version='0.1',

    # Description
    description='Fractional Fourier transform for NumPy.',

    # Your contact information
    author='Nils Werner',
    author_email='nils.werner@gmail.com',

    # License
    license='MIT',

    # Packages in this project
    # find_packages() finds all these automatically for you
    packages=setuptools.find_packages(),

    # Dependencies, this installs the entire Python scientific
    # computations stack
    install_requires=[
        'nose>=1.3.0',
        'numpy>=1.8',
        'scipy>=0.13.0',
        'sphinx',
        'sphinx_rtd_theme'
    ],

    tests_require=[
        'nose>=1.3.0'
    ],
    test_suite="nose.collector",

    classifiers=[
        'Development Status :: 2 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'
    ],

    # Register custom commands
    cmdclass={
        'build_sphinx': SphinxCommandProxy
    },
    zip_safe=False,
)
