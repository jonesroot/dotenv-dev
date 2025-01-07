import setuptools

from dotenv_dev import (__author__, __author_contact__, __description__,
                        __name__, __url__, __version__)

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_contact__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
