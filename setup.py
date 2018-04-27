from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='adbpy',
    version='0.1.1',
    description=readme,
    author="Yicheng Zhang",
    license=license,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["libs/ *"],
    }
)
