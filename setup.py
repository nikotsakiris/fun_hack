from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='niko_hack',
    url='https://github.com/jladan/package_demo',
    author='Niko Tsakiris',
    author_email='nikostsakiris2711@gmail.com',
    # Needed to actually package something
    packages=['niko_hack'],
    # Needed for dependencies
    install_requires=['email','imaplib','time','gtts','playsound'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT'
)