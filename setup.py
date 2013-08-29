from distutils.core import setup

setup(
    name='dudebot',
    version='0.0.4',
    author='Sujay Mansingh',
    author_email='sujay.mansingh@gmail.com',
    packages=['dudebot', 'dudebot.examples'],
    package_data={
        'dudebot': ['README.md']
    },
    scripts=[],
    url='https://github.com/sujaymansingh/dudebot',
    license='LICENSE.txt',
    description='A really simple framework for chatroom bots',
    long_description=open('README.md').read(),
    install_requires=[
        'jabberbot==0.15',
        'xmpppy==0.5.0rc1',
        'feedparser==5.1.3',
    ],
)
