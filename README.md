# Gif your brain

The script `brain2gif.py` allows you to create nice looking gifs from any NIfTI image. If you don't have your own brain images, than I recommend you to download the [ICBM152 template](http://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009). For the examples below, I've downloaded [ICBM 2009c Nonlinear Asymmetric](http://www.bic.mni.mcgill.ca/~vfonov/icbm/2009/mni_icbm152_nlin_asym_09c_nifti.zip) and used the T1 and gray matter  template thereof.

It is also possible to use your own brain image, as I will show below. The only thing that you need to make sure is, that your brain image has the right orientation. You can reorient your NIfTI image according to the MNI template standard with the FSL command: `fslreorient2std my_brain.nii my_brain.nii`.


# Examples

## Grayscale GIF

To create a simple gray scale gif, use `write_gif_normal(nifti_name, size, frames_per_second, filetype)`:

<img src="mni_icbm152_t1_tal_nlin_asym_09c.gif">

Command: `write_gif_normal('mni_icbm152_t1_tal_nlin_asym_09c.nii', 1, 20, 'gif')`


## Colored GIF

To create a colored gif, use `write_gif_cmap(nifti_name, size, frames_per_second, colormap, filetype)`:

<img src="Me_2014_Spectral_r.gif" width="687">

Command: `write_gif_cmap('Me_2014.nii', 1, 20, 'Spectral_r', 'gif')` - Where the colormap can be any colormap from the [matplotlib colormaps](https://matplotlib.org/examples/color/colormaps_reference.html).


## Depth GIF

To create a depth gif, use `write_gif_depth(nifti_name, size, frames_per_second, filetype)`:

<img src="mni_icbm152_gm_tal_nlin_asym_09c_depth.gif">

Command: `write_gif_depth('mni_icbm152_gm_tal_nlin_asym_09c.nii', 1, 20, 'gif')` - The image shows you in color what the value of the next slice will be. If the color is slightly red or blue it means that the value on the next slide is brighter or darker, respectifely. It therefore encodes a certain kind of depth into the gif.


## Resize GIF

It is also possible to change the size of a gif, by changing the `size` parameter in any function above. The following are examples of resizing the images to 50% of it's original size, with:

```python
write_gif_normal('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'gif')
write_gif_cmap('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'bone', 'gif')
write_gif_cmap('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'cubehelix', 'gif')
write_gif_cmap('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'CMRmap', 'gif')
write_gif_cmap('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'inferno', 'gif')
write_gif_cmap('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'viridis', 'gif')
```

<img src="mni_icbm152_gm_tal_nlin_asym_09c.gif"><img src="mni_icbm152_gm_tal_nlin_asym_09c_bone.gif">
<img src="mni_icbm152_gm_tal_nlin_asym_09c_cubehelix.gif"><img src="mni_icbm152_gm_tal_nlin_asym_09c_CMRmap.gif">
<img src="mni_icbm152_gm_tal_nlin_asym_09c_inferno.gif"><img src="mni_icbm152_gm_tal_nlin_asym_09c_viridis.gif">

**Note:** Changing the size of a gif also changes the frames per second parameter, so that the overall tempo stays the same. Meaning, if you have a gif of original size with 24fps, changing the size to 50%, will cause the smaller gif to run at 12fps, so that both take the same amount for a cycle.
