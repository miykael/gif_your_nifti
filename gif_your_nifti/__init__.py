"""For having the version."""

import pkg_resources

__version__ = pkg_resources.require("gif_your_nifti")[0].version
