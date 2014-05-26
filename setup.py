import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Loaderio",
    version = "1.0.2",
    author = "Felix Cheruiyot",
    author_email = "felix@kenyaapps.net",
    description = ("Python api wrapper for loader.io."),
    license = "MIT",
    keywords = "loader.io loader load balancing",
    url = "https://github.com/kenyaapps/loaderio.git",
    packages=['loaderio', 'loaderio/resources', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
	   'requests == 2.0.1'
    ]
)
