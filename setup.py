from setuptools import setup

version = '1.23'

long_description = '\n\n'.join(
    [open('README.rst').read(),
     open('CHANGES.rst').read(),
     ])

install_requires = [
    'setuptools',
    'Cheetah',
    'PasteScript>=1.6',
    ]

tests_require = [
    'nose',
    ]


setup(
    name='nensskel',
    version=version,
    author='Reinout van Rees',
    author_email='reinout.vanrees@nelen-schuurmans.nl',
    url='http://pypi.python.org/pypi/nensskel',
    download_url='',
    description='Skeleton for Nelen & Schuurmans projects',
    long_description=long_description,
    license='GPL',
    packages=['nensskel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points={
        'console_scripts': [
            'nensskel = nensskel.cmdline:main',
            ],
        'paste.paster_create_template': [
            'nens_library = nensskel.library:Library',
            'nens_djangoapp = nensskel.djangoapp:Djangoapp',
            'nens_lizardsite = nensskel.lizardsite:Lizardsite',
            ],
        },
    )
