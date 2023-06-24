from setuptools import setup, find_packages

setup(
    name='hepha-cli',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'boto3==1.26.160',
        'click==8.1.3',
        'PyYAML==6.0',
        'Jinja2==3.1.2',
        'requests==2.31.0',
        'autopep8==2.0.2',
        'pylint==2.17.4',
        'flake8==6.0.0',
    ],
    entry_points='''
        [console_scripts]
        hepha=hepha.cli:cli
    ''',
    author='Pablo Contreras (bypabloc)',
    author_email='pacg1991@gmail.com',
    description='Hepha CLI: Una herramienta de desarrollo para la creación y gestión de API Gateway en AWS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bypabloc/hepha-cli',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
