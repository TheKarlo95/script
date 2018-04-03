from setuptools import setup

setup(
    name='script',
    version='1.0',
    py_modules=['script'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        script=script:cli
    '''
)
