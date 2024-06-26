from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirememnts=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
    
    return requirements

setup(
name="mlproject",
versio='0.0.1',
author='spoorthi',
author_email='aspoorthirai@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)