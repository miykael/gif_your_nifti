"""gif_your_nifti setup."""


from setuptools import setup

VERSION = '0.2.0'

setup(name='gif_your_nifti',
      version=VERSION,
      description='Create gifs from NIfTI image.',
      url='',
      download_url=(''),
      author='Michael Notter',
      author_email='',
      license='BSD 3-Clause License',
      packages=['gif_your_nifti'],
      install_requires=['numpy', 'nibabel'],
      keywords=['nifti', 'gif'],
      entry_points={'console_scripts': [
          'gif_your_nifti = gif_your_nifti.__main__:main']},
      zip_safe=True)
