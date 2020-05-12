from __future__ import absolute_import
from setuptools import setup, find_packages
from oauth_provider import __version__ as version
import os


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list([_f for _f in [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()] if _f])


install_requires = reqs('requirements.txt')
test_requires = reqs('test-requirements.txt')

setup(
    name='django-oauth-plus',
    version=version,
    description='Support of OAuth 1.0a in Django using python-oauth2.',
    author='David Larlet',
    author_email='david@larlet.fr',
    url='https://bitbucket.org/david/django-oauth-plus/',
    packages=find_packages(),
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
    ],
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    include_package_data=True,
    zip_safe=False,
    test_requires=test_requires,
    install_requires=install_requires
)
