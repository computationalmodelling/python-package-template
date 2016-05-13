from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='package_template',
    version='0.1',
    description='A simple example of a Python package',
    long_description=readme,
    author='Computational Modelling Group',
    author_email='fangohr@soton.ac.uk',
    packages=['package_template', 'package_template.tests'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
