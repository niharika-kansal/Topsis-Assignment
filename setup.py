from setuptools import setup, find_packages

setup(
    name='topsis-Niharika-102203344',  
    version='1.0.0',  # Initial version
    description='Python library for implementing TOPSIS for multi-criteria decision analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    author='Niharika',  
    author_email='niharikaniharika979@gmail.com',  
    url='https://github.com/niharika-kansal/topsis-Niharika-102203344',  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy>=1.18.0', 
        'pandas>=1.0.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis:main',
        ],
    },
    license='MIT',
)
