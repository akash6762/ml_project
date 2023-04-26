from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

# this function will return the list of required packages 
def get_requirements(file_path:str) -> List[str]:
    
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    
setup(
    
    name = "ml_project",
    version = "0.0.1",
    author = "Akash Velu",
    author_email = "akashvelu1@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
    
)