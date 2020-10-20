from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='PythonPals',
    version='1.8',
    packages=['PythonPals'],
    data_files=[('PythonPals', ["PythonPals/python_questions.xlsx", "PythonPals/coffee1.png", "PythonPals/coffee2.png",
                                "PythonPals/coffee3.png", "PythonPals/coffee4.png", "PythonPals/coffee5.png",
                                "PythonPals/coffee6.png", "PythonPals/snake1.png", "PythonPals/snake2.png",
                                "PythonPals/snake4.png", "PythonPals/snake5.png", "PythonPals/snake6.png",
                                "PythonPals/requirements.txt"])],
    url='https://github.com/nathanhilton/PythonPals/tree/development',
    author='Sheamus Cooper',
    author_email='sheamus.cooper@ufl.edu',
    description='Prototype Submission',
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": [
            "python-pals=PythonPals.main:init",
        ]
    },
)
