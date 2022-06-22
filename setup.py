import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphsp",                     # This is the name of the package
    version="1.0.0",                        # The initial release version
    author="Jainam Shah",                     # Full name of the author
    description="Graphsp Package for Graph Data Structure",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["graphsp"],             # Name of the python package
    # Directory of the source code of the package
    package_dir={'': 'graphsp/src'},
    install_requires=[],                     # Install other dependencies if any
    keywords=["graph", "algorithms", "DFS",
              "BFS", "Dijkstra", "Floyd Warshall"],
    url="https://github.com/jainam2385/graphsp",
)
