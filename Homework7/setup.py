from setuptools import setup,find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Homework7. Clean folder',
    author='Yakov Gladkykh',
    author_email='yakov.gladkykh@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']}
)
