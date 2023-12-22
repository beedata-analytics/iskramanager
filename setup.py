from setuptools import setup, find_packages

VERSION = "0.1.0"

with open("requirements.txt", "r") as req:
    INSTALL_REQUIRES = [x.strip() for x in req.readlines()]

DESCRIPTION = "iskramanager"

setup(
    name="iskramanager",
    version=VERSION,
    packages=find_packages(),
    url="https://github.com/beedata-analytics/iskramanager.git",
    license="",
    install_requires=INSTALL_REQUIRES,
    author="Beedata analytics",
    author_email="info@beedataanlytics.com",
    description=DESCRIPTION,
    testsuite="iskramanager",
    package_data={"": []},
    include_package_data=True,
)
