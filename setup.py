import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = ['pyramid', 'WebError', 'pymongo','pyramid_jinja2', 'pyramid_chameleon']

setup(name='my_blog',
      version='0.0',
      description='my_blog',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Christian Murphy",
      author_email='christheromguy@gmail.com',
      url='',
      keywords='web pyramid pylons mongodb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="my_blog",
      entry_points = """\
      [paste.app_factory]
      main = my_blog:main
      """,
      paster_plugins=['pyramid'],
      )

