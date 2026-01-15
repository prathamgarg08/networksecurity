'''
setup.py file is an essential part of packaging and distributing python projects. It is used by
setuptools (or distutils in older python versions) to define the configuration of your project
such as metadata,dependencies and more. -e . in requirements.txt
is referring to the setup.py file which will execute it and setup the python project as a package 
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file is not found')
    
    return requirement_lst

setup(
    name='Network Security',
    version='0.0.1',
    author='Pratham Garg',
    author_email='prathamgarg89@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()


)

