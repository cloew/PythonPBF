from distutils.core import setup

setup(name='pbf_python',
      version='.3',
      description="Programmer's Best Friend Utility Extension for Python",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_python', 'pbf_python.Commands', 'pbf_python.helpers', 'pbf_python.templates'],
      package_data = {'pbf_python.templates':['*']},
     )