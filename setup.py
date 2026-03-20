import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="cosmopy",
    version="0.1.0",
    author="Michael Garstka, Richard Ziegahn",
    author_email="richard.ziegahn@mail.mcgill.ca",
    description="An interface to the Julia solver COSMO.jl based on JuliaCall.",
    url="https://github.com/RickyZiegahn/cosmo-python",
    install_requires=["numpy >= 1.7", "scipy >= 0.13.2", "juliacall"],
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages= setuptools.find_packages(),
    python_requires='>=3.6',
    license='Apache 2.0'
)
