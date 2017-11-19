from setuptools import setup, find_packages


setup(
    name='ubuntu_news',
    version='1.0',
    author='Isaac Atia',
    author_email='atiaisaac007@gmail.com',
    description='Ubuntu News from omgubuntu site',
    long_description='Web scraping omgubuntu.co.uk to get latest news about my favourite \
    linux distro.News may include release date of ubuntu, bug fixes and other \
    tools needed for my ubuntu to function well',
    classifiers=[
        'Development Status::3-Alpha',
        'Intended Audience::Developers',
        'License::OSI Approved::MIT License',
        'Programming Language::Python::3.5'],
    license='MIT',
    packages=find_packages(),
    install_requires=['bs4', ],
    entry_points={'console_scripts': ['ubuntunews=OMG.brain:access']}
)
