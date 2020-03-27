import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gendiff",
    version="0.0.0",
    author="otreblan",
    author_email="",
    description="diff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cs2b01-2020-1/week0-introgit-otreblan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "tabulate"
    ],

    entry_points={
        "console_scripts": [
            "gendiff = gendiff.__main__:main",
        ],
    },
    package_data={
        "": ["genomas/*.txt"]
    },
    python_requires='>=3.3',
)
