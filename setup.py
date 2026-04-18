'''
    The setup.py file is an essential part of packaging and distributing
    Python projects. It is used by setuptools or disutils(in older python versions)
    to define the configuration of your project such as its metadata, dependencies,
    and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
        This func will return list of requiremnets
    '''

    try:

        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()

            requirement_lst:List[str] = []
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if(requirement and requirement != '-e .'):
                    requirement_lst.append(requirement)
        
    except FileNotFoundError:
        print('requirement.txt file not found')

        return 
    
    return requirement_lst

setup (
    name = 'NetworkSecurity',
    version = '0.0.1',
    author= 'Pawan Rai',
    author_email= 'pawanvirat32@gmail.com',
    packages= find_packages(exclude=['notebooks', 'network_data']),
    install_requires= get_requirements()

)

