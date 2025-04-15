from setuptools import find_packages,setup
from typing import List


def get_requirements() -> list[str]:

    requirement_lst:List[str]=[]
    try:
        with open ('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    
    return requirement_lst


setup(
    name = "SampleProject",
    version='0.0.1',
    author="Arjun S",
    author_email="arjunjs.m8@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)