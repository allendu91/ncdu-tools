from setuptools import setup
setup(
    name='ncdu-tools',
    version='0.1',
    py_modules=['ncdu-tools'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        find_big_files=find_big_files:cli
    ''',
)