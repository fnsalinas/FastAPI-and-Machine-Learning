
from setuptools import setup, find_packages

setup(
    name='FastAPI_and_Machine_Learning',
    version='1.0',
    description='Testing the FastAPI with a Machine Learning project.',
    author='Fabio Salinas',
    author_email='fabio.salinas1982@gmail.com',
    license='',
    packages=find_packages(
        where='src',
        include=['src', 'src.*']
    ),
    package_dir={
        '':'src'
    },
    zip_safe=False
)
