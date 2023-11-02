from setuptools import setup

setup(
    name="clean_folder",
    version="0.1.0",
    description="folder_sorter_program",
    author="GoIT_student_Olga_Ivanko",
    url="https://github.com/olga-ivanko/clean_folder",
    license="MIT",
    entry_points={"console_scripts": [
        "clean_folder=clean_folder.clean:main"]})