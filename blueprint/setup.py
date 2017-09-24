from setuptools import setup

setup(
    name='blueprint',
    packages=['blueprint'],
    include_package_data=True,
    install_requires=[
        'django',
        'djangorestframework'
    ],
)