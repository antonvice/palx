from setuptools import setup, find_packages

setup(
    name='px',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow', 'numpy', 'scikit-learn'  
    ],
    entry_points={
        'console_scripts': [
            'px=px.main:main', 
        ],
    },
)