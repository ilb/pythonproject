from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='library',
    packages=['library'],
    version='0.0.1',
    description='This is library',
    install_requires=required
    # add some information, like name, email, etc
)
