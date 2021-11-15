import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bestcompany-api-wrapper',
    version='0.0.1',
    description='Package to wrap api calls for bestcompany',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bestcompany-org/python-bestcompany-api-wrapper',
    author='Cameron Pope',
    author_email='technology@bestcompany.com',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25',
    ]
)

