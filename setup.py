from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()
    
setup(
    name='catrix',
    version='1.0.0',
    description='A virtual realm simulation of mindful and exploring cats.',
    author='Ishan Oshada',
    packages=find_packages(),
    author_email='ic31908@gmail.com',
    
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/Catrix',
    install_requires=["pyfiglet"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='virtual realm simulation cats mindful exploring'
)
