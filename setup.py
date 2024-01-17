
from setuptools import setup, find_packages

setup(
    name='NEFShutterCountReader',
    version='0.1',
    packages=find_packages(),
    description='A simple script to read the shutter count from Nikon NEF files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='MasterCard007',
    author_email='',
    url='',
    install_requires=[
        'exifread',
    ],
    entry_points={
        'console_scripts': [
            'nef-shutter-count = nef_shutter_count_reader:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
