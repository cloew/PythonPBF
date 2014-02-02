from distutils.core import setup

setup(name='pbf.python',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Python",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf.python', 'pbf.python.Commands', 'pbf.python.templates'],
      package_data = {'pbf.python.templates':['*']},
     )