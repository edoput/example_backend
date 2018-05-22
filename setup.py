from setuptools import setup, find_packages

setup(
    name='example_backend',
    version='0.0.0',
    description='an example to illustrate a netjsonconfig backend as an external module',
    packages=find_packages(),
    entry_points={
        'netjsonconfig.backends': [
            'example=example_backend.__init__:ExampleBackend',
        ]
    }
)
