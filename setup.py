"""gif_your_nifti setup."""

from setuptools import setup

VERSION = '0.2.1'

setup(name='gif_your_nifti',
      version=VERSION,
      description='Create gif from nifti image.',
      url='',
      download_url=(''),
      author='Michael Notter',
      license='BSD 3-Clause License',
      packages=['gif_your_nifti'],
      install_requires=[
            'numpy',
            'nibabel',
            'imageio<2.28',  # SEE: https://github.com/miykael/gif_your_nifti/issues/12
            'matplotlib'
      ],
      keywords=['nifti', 'gif'],
      entry_points={'console_scripts': [
          'gif_your_nifti = gif_your_nifti.__main__:main']},
      zip_safe=True)
