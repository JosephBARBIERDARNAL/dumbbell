from setuptools import setup, find_packages

setup(
    name="dumbbell",
    version="0.0.0.9",
    packages=find_packages(),
    description="Dumbbell and lollipop",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/dumbbell",
    install_requires=["matplotlib"],
)
