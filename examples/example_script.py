"""Example usage of gif_your_nifti."""

import gif_your_nifti.core as gif2nif

# Shows the creation of a normal grayscale gif - based on T1 MNI template
gif2nif.write_gif_normal('mni_icbm152_t1_tal_nlin_asym_09c.nii',
                         size=1, fps=20)

# Shows the creation of colored gif - based on a individual brain image
gif2nif.write_gif_cmap('Me_2014.nii', size=1, fps=20, 'Spectral_r')

# Shows the creation of a depth gif - based on the gray matter MNI template
gif2nif.write_gif_depth('mni_icbm152_gm_tal_nlin_asym_09c.nii', size=1, fps=20)

# Shows the creation of a RGB gif - based on the gray matter, white matter
# and CSF MNI template
input_red = 'mni_icbm152_gm_tal_nlin_asym_09c.nii'
input_green = 'mni_icbm152_wm_tal_nlin_asym_09c.nii'
input_blue = 'mni_icbm152_csf_tal_nlin_asym_09c.nii'
gif2nif.write_gif_rgb(input_red, input_green, input_blue, size=1, fps=20)

# Shows how to change the size of the gif on different colored GM templates
input = 'mni_icbm152_gm_tal_nlin_asym_09c.nii'

gif2nif.write_gif_cmap(input, size=0.5, fps=20, 'bone', 'gif')
gif2nif.write_gif_cmap(input, size=0.5, fps=20, 'cubehelix', 'gif')
gif2nif.write_gif_cmap(input, size=0.5, fps=20, 'CMRmap', 'gif')
gif2nif.write_gif_cmap(input, size=0.5, fps=20, 'inferno', 'gif')
gif2nif.write_gif_cmap(input, size=0.5, fps=20, 'viridis', 'gif')
