"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
python setup.py publish to publish
"""

import glob
import os
import sys

import setuptools

# Always prefer setuptools over distutils
from setuptools import find_packages
from setuptools import setup

# from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))


if sys.argv[-1] == "publish":  # requests
    os.system("python setup.py sdist")  # bdist_wheel
    os.system("twine upload dist/* --skip-existing")
    sys.exit()


# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="term-charts",  # Required
    version="1.0.0",  # Required
    description="Download stats for Python packages",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    # url="https://github.com/Abdur-RahmaanJ/greenBerry",  # Optional
    # author="Abdur-Rahmaan Janhangeer & contributors",  # Optional
    author_email="arj.python@gmail.com",  # Optional
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # 'Topic :: Weather',
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    # keywords="",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires=">=3.7",
    include_package_data=True,
    # install_requires=open(os.path.join(here, "reqs", "app.txt"), encoding="utf-8")
    # .read()
    # .split("\n"),  # Optional
    install_requires=open(os.path.join(here, "reqs", "app.txt"), encoding="utf-8")
        .read()
        .split("\n"),
    extras_require={
        "dev": open(os.path.join(here, "reqs", "dev.txt"), encoding="utf-8")
        .read()
        .split("\n"),
        "rich": ["rich"]
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/Abdur-RahmaanJ/term-charts/issues",
        "Source": "https://github.com/Abdur-RahmaanJ/term-charts/",
    },
    packages=find_packages(),
    # entry_points={"console_scripts": ["download-stats=download_stats.main:main"]},
)
# Footer

