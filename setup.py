from setuptools import setup, find_namespace_packages

setup(name='homework_2.8',
      version=1,
      description='Inserting records into MongoDB from .json',
      author='Bartosz Szczepan',
      packages=find_namespace_packages(),
      requires=['mongoengine', 'pika', 'faker'],
      entry_points={'console_scripts': ['seed = homework_2_8.seed:insert_from_json']}
)