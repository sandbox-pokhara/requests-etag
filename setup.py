import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='requests-etag',
    version='1.0.1',
    author='Pradish Bijukchhe',
    author_email='pradishbijukchhe@gmail.com',
    description='Wrapper over requests package to support etag caching by default',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sandbox-pokhara/requests-etag',
    project_urls={
        'Bug Tracker': 'https://github.com/sandbox-pokhara/requests-etag/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    packages=['requests_etag'],
    python_requires='>=3',
    install_requires=['requests'],
)
