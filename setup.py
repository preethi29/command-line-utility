from setuptools import setup

setup(
    name='bahmnicli',
    version='0.1',
    py_modules=['bahmnicli'],
    install_requires=[
        'Click',
        'ansible==1.9.4'
    ],
    entry_points='''
        [console_scripts]
        bahmnicli=bahmnicli:cli
    ''',
)
