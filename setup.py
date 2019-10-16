from distutils.core import setup
setup(
    name='LaraPy',         # How you named your package folder (MyLib)
    packages=['LaraPy'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='A python implementation of laravel framework for machine learning, AI, datascience and data intensive work.',
    author='Bedram Tamang',                   # Type in your name
    author_email='tmgbedu@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/bedus-creation/LaraPy',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],
    install_requires=[            # I get to this in a second
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
    ],
)
