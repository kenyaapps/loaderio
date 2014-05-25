import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Loaderio",
    version = "0.1",
    author = "Felix Cheruiyot",
    author_email = "felix@kenyaapps.net",
    description = ("Python api wrapper for loader.io."),
    license = "BSD",
    keywords = "loader.io loader load balancing",
    url = "https://github.com/kenyaapps/pyloader.git",
    packages=['loaderio', 'loaderio/resources', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
	'requests == 2.0.1'
    ]
)
