import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lego-mp-extension",
    version="0.1.5",
    author="Lee Tzilantonis",
    author_email="LTzilantonis@gmail.com",
    description="Extension for the Lego EV3 MicroPython Port",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/klutzybubbles/lego-micropython-extension",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)