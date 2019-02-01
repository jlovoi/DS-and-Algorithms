from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DS and Algorithms',
    version='0.0.1',
    description='MIT Open CourseWork for Algorithms',
    long_description=readme,
    author='Joseph Lovoi',
    author_email='joelovoi@gmail.com',
    url='https://github.com/jlovoi/DS-and-Algorithms',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)