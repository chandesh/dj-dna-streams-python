from distutils.core import setup
from setuptools import find_packages
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dnaStreaming',
    version='2.0.3',
    description='Dow Jones DNA Streaming Project',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Zachary Kagan',
    author_email='zachary.kagan@dowjones.com',
    url='https://github.com/dowjones/dj-dna-streams-python',
    download_url='https://github.com/dowjones/dj-dna-streams-python/archive/release-2.0.0.tar.gz',
    keywords=['DOWJONES', 'FACTIVA', 'STREAMS'],
    packages=find_packages(exclude='tests'),

    # metadata for upload to PyPI
    license="MIT",

    include_package_data=True,

    install_requires=[
        'googleapis-common-protos>=1.55.0',
        'google-auth>=2.6.0',
        'google-cloud-pubsub>=2.10.0',
        'google-cloud-core>=2.2.2',
        'google-api-core>=2.4.0',
        'mock>=4.0.0',
        'requests>=2.22.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
