# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


version = '1.0.0.dev0'


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='bobtemplates.cs',
    version=version,
    description='Templates for Plone projects by CodeSyntax',
    long_description=long_description,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='web plone zope skeleton project',
    author='Mikel Larreategi',
    author_email='mlarreategi@codesyntax.com',
    url='https://github.com/codesyntax/bobtemplates.cs',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
        'lxml',
        'stringcase',
    ],
    setup_requires=[],
    tests_require=[],
    extras_require={},
    entry_points={
        'mrbob_templates': [
            #'plone_addon = bobtemplates.plone.bobregistry:plone_addon',
            'cs_plone_buildout = bobtemplates.cs.bobregistry:cs_plone_buildout',  # NOQA E501
            #'plone_theme_package = bobtemplates.plone.bobregistry:plone_theme_package',  # NOQA E501
            #'plone_content_type = bobtemplates.plone.bobregistry:plone_content_type',  # NOQA E501
            #'plone_theme = bobtemplates.plone.bobregistry:plone_theme',
            #'plone_vocabulary = bobtemplates.plone.bobregistry:plone_vocabulary',  # NOQA E501
        ],
    },
)
