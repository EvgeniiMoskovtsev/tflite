import setuptools, os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='tflite',
    version='0.0.1-alpha-0',
    description="A package to parse TFLite models (*.tflite)",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords=['tflite', 'tensorflow'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=[ 'flatbuffers',],

    # author='王振华（Zhenhua WANG）',
    # author_email='i@jackwish.net',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url="https://jackwish.net/tflite",

    # project_urls={
    #     'Bug Reports': 'https://github.com/jackwish/tflite/issues',
    #     'Source': 'https://github.com/jackwish/tflite',
    # },
)