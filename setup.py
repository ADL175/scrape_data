"""Scraper setup."""

from setuptools import setup

requires = [
    'appnope',
    'beautifulsoup4',
    'certifi',
    'chardet',
    'click',
    'decorator',
    'geocoder',
    'html5lib',
    'idna',
    'ipython',
    'ipython-genutils',
    'jedi',
    'pexpect',
    'pickleshare',
    'prompt-toolkit',
    'ptyprocess',
    'Pygments',
    'ratelim',
    'requests',
    'simplegeneric',
    'six',
    'traitlets',
    'urllib3',
    'wcwidth',
    'webencodings',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
]

setup(
    name='scraper',
    version='0.0',
    description='Scraper',
    long_description=README
    author='David Lim',
    author_email='',
    license="MIT",
    url='',
    keywords='scraper',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
)
