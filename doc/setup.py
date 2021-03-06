from setuptools import setup

setup(name='dpx_func_python',
    version='0.2',
    description='DPX control software',
    author='Sebastian Schmidt',
    author_email='schm.seb@gmail.com',
    license='MIT',
    packages=['dpx_func_python'],
    entry_points={
        'console_scripts' : [
            'dpx_func_python = dpx_func_python.dpx_func_python:main',
        ]
    },
    install_requires=[
        'matplotlib',
        'hickle',
        'pandas',
        'numpy',
        'scipy',
        'pyserial',
        'pyyaml',
        'configparser',
        'tqdm'
        # 'sphinx',
        # 'sphinx_rtd_theme'
    ])
