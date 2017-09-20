from setuptools import setup

with open('README.rst', 'r') as f:
    longdesc = f.read()

setup(
    name="mw-api-client",
    version="0.0.0",
    description="A simple MediaWiki client.",
    long_description=longdesc,
    url="https://github.com/Kenny2github/mw-api-client",
    author="Ken Hilton",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='mediawiki api requests',
    py_modules=['mw-api-client'],
    install_requires='requests',
    python_requires='>=2.7',
)