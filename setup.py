from setuptools import setup, find_packages


def readme():
    with open('PythonPals/README.md') as f:
        README = f.read()
    return README


setup(
    name='PythonPals',
    version='1.0',
    packages=["PythonPals"],
    include_package_data=True,
    install_requires=["pygame", "openpyxl"],
    url='https://github.com/nathanhilton/PythonPals',
    author='Sheamus Cooper',
    author_email='sheamus.cooper@ufl.edu',
    description='First iteration of setup',
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": [
            "python-pals=PythonPals.main:init",
        ]
    },
)
