from setuptools import setup

long_description = '\n\n'.join(
    [open('README.txt').read(),
     open('CHANGES.txt').read(),
     open('TODO.txt').read()])
version = '0.1dev'
install_requires = [
    'setuptools',
    'Cheetah',
    'PasteScript>=1.6',
    'uuid',
    'z3c.testsetup',
    ]
tests_require = []


setup(
    name='nensskel',
    version=version,
    author='Reinout van Rees',
    author_email='reinout.vanrees@nelen-schuurmans.nl',
    url='',
    download_url='',
    description='Skeleton for Nelen & Schuurmans projects',
    long_description=long_description,
    license='GPL',
    packages=['nensskel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            ],
        'paste.paster_create_template':
        [#'tha_website = thaskel.tha:WebSite',
            ]},
    )
