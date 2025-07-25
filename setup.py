from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT = "-e ."

def get_requirements(filename:str) -> List[str]:

    requirements = []
    with open(filename, "r") as f:
        requirements = f.readlines()

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        requirements = [requirement.replace("\n", "") for requirement in requirements]

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    author='Srinu',
    author_email='srinunayakk7@gmail.com',
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
)
