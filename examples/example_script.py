"""Example usage of gif_your_nifti."""

import gif_your_nifti.core as gif2nif

filename = 'mni_icbm152_t1_tal_nlin_asym_09c.nii'

# Create a normal grayscale gif.
gif2nif.write_gif_normal(filename)

# Create a pseudocolored gif.
gif2nif.write_gif_pseudocolor(filename, colormap='plasma')

# Create a depth gif.
gif2nif.write_gif_depth(filename)

# Change the size of gifs.
gif2nif.write_gif_pseudocolor(filename, size=0.5, colormap='cubehelix')
gif2nif.write_gif_pseudocolor(filename, size=0.5, colormap='inferno')
gif2nif.write_gif_pseudocolor(filename, size=0.5, colormap='viridis')

# Create an RGB gif, based on gray matter, white matter and cerebrospinal fluid
# images from MNI template.
filename1 = 'mni_icbm152_gm_tal_nlin_asym_09c.nii'
filename2 = 'mni_icbm152_wm_tal_nlin_asym_09c.nii'
filename3 = 'mni_icbm152_csf_tal_nlin_asym_09c.nii'
gif2nif.write_gif_rgb(filename1, filename2, filename3)
