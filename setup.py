import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
log_path = here + '/blog/logs'
if not os.path.exists(log_path):
  os.makedirs(log_path+'/access_logs')
  os.makedirs(log_path+'/api_logs')

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'paste',
    'pyramid_exclog',
    'mysql-python',
    'cornice',
    'colander'
    ]

setup(name='blog',
      version=0.1,
      description='blog app',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Atul Kumar',
      author_email='atul.kumar0401@gmail.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points = """\
      [paste.app_factory]
      main=blog:main
      """,
      paster_plugins=['pyramid'])
