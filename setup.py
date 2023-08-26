<<<<<<< HEAD
from setuptools import setup,find_packages
from typing import List

def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path, 'r') as f:
        requirements=f.readlines()
        requirements=[i.replace('\n','') for i in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements



setup(author='Anirudha sutar',
      name='movie-recomendations',
      version='0.0.1',
      author_email='sutaranirudha604@gmail.com',
    #   packages = find_packages(),
      install_requires = get_requirements('requirements.txt')
)
=======
from setuptools import setup,find_packages
from typing import List

def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path, 'r') as f:
        requirements=f.readlines()
        requirements=[i.replace('\n','') for i in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements



setup(author='Anirudha sutar',
      name='movie-recomendations',
      version='0.0.1',
      author_email='sutaranirudha604@gmail.com',
    #   packages = find_packages(),
      install_requires = get_requirements('requirements.txt')
)
>>>>>>> 0548a8193520b6c266e96cb2766c530e2c8df109
