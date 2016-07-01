from setuptools import setup, find_packages

VERSION = '0.0.5'

LONG_DESCRIPTION = open('README.rst').read()

setup(name='overlayUtils',
    version=VERSION,
    description='overlayUtils',
    long_description=LONG_DESCRIPTION,
    keywords='overlayfs',
    author='Alex Goodman',
    url='https://github.com/wagoodman/overlayUtils',
    license='MIT',
    platforms='Ubuntu',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'subwrap',
    ],
    entry_points={},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Build Tools',
    ],
)
