import setuptools

setuptools.setup(
    name="ivostoy_test_pkg",
    version="1.0.0",
    author="Ivo Stoyanov",
    author_email="ivostoy@email.com",
    description="my test package",
    long_description="This is the longer description and will appear on the web.",
    py_modules=["ivostoy_test_pkg"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)