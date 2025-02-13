# setup.py

from setuptools import setup, find_packages

setup(
    name='dpsk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'dpsk=my_module.main:main',
        ],
    },
)
