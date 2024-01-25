from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list:

    """
    Return requirements from requirements.txt file.

    Args:
        file_path (str): Path to requirements.txt file.    
        
        """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
    


setup(
name='mlproject',
version='0.1',
description='My first ML project',
author='Saleem',
author_email= "sabaitham@gmail.com",
license='MIT',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)
