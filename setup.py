import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bestcompany-api-wrapper',
    version='0.0.1',
    description='Package to wrap api calls for bestcompany',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='git@bitbucket.org:skyrocketnow/bc-utils.git',
    author='Ryan Scott',
    author_email='rscott@bestcompany.com',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'boto3>=1.7',
        'cerberus>=1.3',
        'numpy>=1.19',
        'pandas>=1.1.1',
        'prometheus-client>=0.5',
        'requests>=2.25',
        'slack_sdk',
        'vertica-python>=0.7',
    ]
)

