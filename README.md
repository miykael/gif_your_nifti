# Gif your brain

The script `brain2gif.py` allows you to create nice looking gifs from any NIfTI image. If you don't have your own brain images, than I recommend you to download the [ICBM152 template](http://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009) - which are based on the MNI-152 template.

For the examples below, I've downloaded the [ICBM 2009c Nonlinear Asymmetric](http://www.bic.mni.mcgill.ca/~vfonov/icbm/2009/mni_icbm152_nlin_asym_09c_nifti.zip) and used the T1 (`mni_icbm152_t1_tal_nlin_asym_09c.nii`) and gray matter (`mni_icbm152_gm_tal_nlin_asym_09c.nii`) template.

*Note: If you really want a high resolution gif, I recommend to us the high resolution T1 template `mni_icbm152_t1_tal_nlin_asym_09b_hires.nii` from [ICBM 2009b Nonlinear Asymmetric](http://www.bic.mni.mcgill.ca/~vfonov/icbm/2009/mni_icbm152_nlin_asym_09b_nifti.zip). This brain image has a voxel resolution of 0.5 x 0.5 x 0.5mm. But be aware, that a gif with this high resolution is about 200MB big.*

It is also possible to use your own brain image, as I will show below. The only thing that you need to make sure is, that your brain image has the right orientation. You can reorient your NIfTI image according to the MNI template standard with the FSL command: `fslreorient2std my_brain.nii my_brain.nii`.


# Examples

## Grayscale GIF

To create a simple gray scale gif, use `write_gif_normal(nifti_name, size, frames_per_second, filetype)`:

```python
write_gif_normal('mni_icbm152_t1_tal_nlin_asym_09c.nii', 1, 20, 'gif')
```

<img src="mni_icbm152_t1_tal_nlin_asym_09c.gif">


## Colored GIF

To create a colored gif, use `write_gif_cmap(nifti_name, size, frames_per_second, colormap, filetype)`:

```python
write_gif_cmap('Me_2014.nii', 1, 20, 'Spectral_r', 'gif')
```

<img src="Me_2014_Spectral_r.gif" width="342">

Where the colormap can be any colormap from the [matplotlib colormaps](https://matplotlib.org/examples/color/colormaps_reference.html).


## Depth GIF

To create a depth gif, use `write_gif_depth(nifti_name, size, frames_per_second, filetype)`:

```python
write_gif_depth('mni_icbm152_gm_tal_nlin_asym_09c.nii', 1, 20, 'gif')
```

<img src="mni_icbm152_gm_tal_nlin_asym_09c_depth.gif">

The image shows you in color what the value of the next slice will be. If the color is slightly red or blue it means that the value on the next slide is brighter or darker, respectifely. It therefore encodes a certain kind of depth into the gif.


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

Changing the size of a gif also changes the frames per second parameter, so that the overall tempo stays the same. Meaning, if you have a gif of original size with 24fps, changing the size to 50%, will cause the smaller gif to run at 12fps, so that both take the same amount for a cycle.
