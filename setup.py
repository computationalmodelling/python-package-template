from distutils.core import setup

setup(
    name='package_template',
    version='0.1',
    description='A simple example of a Python package',
    author='Computational Modelling Group',
    author_email='fangohr@soton.ac.uk',
    packages=['package_template', 'package_template.tests'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
