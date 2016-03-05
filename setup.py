from setuptools import setup, find_packages

setup(name='bookry',
      version='0.0.1',
      description='Bookry compares book price between Books & Eslite',
      author='Thomas Lin',
      author_email='ithomaslin@gmail.com',
      license='Apache License',
      packages=find_packages(),
      install_requires=[
          'progressbar',
          'requests',
          'lxml',
          'pyquery',
          'httplib2',
          'google-api-python-client',
          'urllib3'
      ],
      zip_safe=False
)