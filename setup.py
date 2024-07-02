from setuptools import setup, find_packages

setup(
    name='sc3py',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sc3py=sc3py.cli:main',  # Assuming 'main' is the entry function in compiler.py
        ],
    },
    package_data={
        'sc3py.compiler': ['conf/*'],
    },
    # Add other package info as needed
)
#这个是怎么用啊，看不懂，出个教程