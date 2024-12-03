# setup.py

from setuptools import setup, find_packages

setup(
    name='safe-pip',
    version='1.0.1',
    author='Guy Kaplan',
    author_email='gkpln3@gmail.com',
    description='A safer pip that checks package health before installation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gkpln3/safe-pip',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'safe-pip=safe_pip.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
