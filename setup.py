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
                                "PythonPals/C1.png", "PythonPals/C2.png", "PythonPals/C3.png", "PythonPals/C4.png",
                                "PythonPals/cave.jpg", "PythonPals/jazz.mp3", "PythonPals/lava.png",
                                "PythonPals/Ruby_fire.png", "PythonPals/Ruby_hurt.png", "PythonPals/Ruby_Idle.png"
                                , "PythonPals/Ruby_left.png", "PythonPals/Ruby_prep.png", "PythonPals/Ruby_start.png",
                                "PythonPals/treasure.png", "PythonPals/Snake_Firemid.png", "PythonPals/Snake_start.png",
                                "PythonPals/python_questions_capitals.xlsx", "PythonPals/python_questions_timeline.xlsx"
                                , "PythonPals/JandaManateeSolid.ttf", "PythonPals/background_boss_music.wav",
                                "PythonPals/background_laundr.wav", "PythonPals/jungleBackground.png",
                                "PythonPals/requirements.txt"])],
    url='https://github.com/nathanhilton/PythonPals/tree/development',
    author='Sheamus Cooper',
    author_email='sheamus.cooper@ufl.edu',
    description='Production Release',
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": [
            "python-pals=PythonPals.main:init",
        ]
    },
)
