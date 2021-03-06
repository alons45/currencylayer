import setuptools

setuptools.setup(
    name="currencylayer",
    version="1.0",
    url="https://github.com/Said007/currencylayer",

    author="Said Ali",
    author_email="said.ali@msn.com",

    description="currencylayer for python API client",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['requests>=2.9.1'],
    keywords=['currency', 'currencylayer', 'exchangerate', 'rates'],

    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
