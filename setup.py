from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function returns the list of requirements"""
    
    requirements = []
    with open(file_path, encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Saud Khan',
    author_email='saudkhan2154@gmail.com',
    packages=find_packages(where="src"),   # Look inside src
    package_dir={"": "src"},                # Map packages to src
    install_requires=get_requirements('requirements.txt')
)