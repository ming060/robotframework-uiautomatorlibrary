from distutils.core import setup

setup(
    name = 'robotframework-uiautomatorlibrary',
    packages = ['uiautomatorlibrary'],
    version = '0.1',
    author='ming060',
    author_email = 'lym060@gmail.com',
    url = 'https://github.com/ming060/robotframework-uiautomatorlibrary',
    description = 'Robot Framework Android Test Library Based on Python uiautomator',
    long_description = 
    """
    This is a test library for `Robot Framework <https://pypi.python.org/pypi/robotframework>`_ to bring keyword-driven testing to Android apps..

    It uses by using `Python uiautomator <https://pypi.python.org/pypi/uiautomator>`_ internally.
    """,
    install_requires = ['uiautomator >= 0.1.28'],
    classifiers  = [
                    'Programming Language :: Python :: 2.7',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: Microsoft :: Windows :: Windows 7',
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Testing'
                    ]
)