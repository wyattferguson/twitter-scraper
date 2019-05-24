import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitterscraper",
    version="0.0.1",
    author="Wyatt Ferguson",
    author_email="wyattf@gmail.com",
    description="A python twitter scraper with no-api keys required.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wyattferguson/twitter-scraper",
    packages=['twitterscraper'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)