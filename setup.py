from setuptools import setup

setup(
    name="clean_folder",
    version="0.1.0",
    entry_points={"console_scripts": ["clean_folder=clean_folder.clean:main"]}

)