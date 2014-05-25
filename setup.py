import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyloader",
    version = "0.1",
    author = "Felix Cheruiyot",
    author_email = "felixc@kenyaapps.net",
    description = ("Python api wrapper for loader.io."),
    license = "BSD",
    keywords = "loader.io loader load balancing",
    url = "https://github.com/kenyaapps/pyloader.git",
    packages=['pyloader', 'pyloader/resources', 'tests'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: API",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
	'requests == 2.0.1'
    ]
)
