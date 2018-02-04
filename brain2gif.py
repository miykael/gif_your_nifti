import nibabel as nb
import numpy as np
from pylab import get_cmap
from imageio import mimwrite
from skimage.transform import resize


def reshape_image(filename, size=1):

    # Load NIfTI file
    data = nb.load(filename).get_data()

    # Pad data array with zeros to make the shape isometric
    maximum = np.max(data.shape)

    out_img = np.zeros([maximum] * 3)

    a, b, c = data.shape
    x, y, z = (list(data.shape) - maximum) / -2

    out_img[int(x):a + int(x),
            int(y):b + int(y),
            int(z):c + int(z)] = data

    out_img /= out_img.max()

    # Resize image by the following factor
    if size != 1:
        out_img = resize(out_img, [int(size * maximum)] * 3)

    return out_img, int(maximum * size)


def create_mosaic_normal(out_img, maximum):

    # Create grayscale output image of template brain
    new_img = np.array(
        [np.hstack((
            np.hstack((
                np.flip(out_img[i, :, :], 1).T,
                np.flip(out_img[:, maximum - i - 1, :], 1).T)),
            np.flip(out_img[:, :, maximum - i - 1], 1).T))
         for i in range(maximum)])

    return new_img


def create_mosaic_depth(out_img, maximum):

    # Load normal mosaic image
    new_img = create_mosaic_normal(out_img, maximum)

    # Create RGB image (where red and blue mean a positive or negative shift in
    # the direction of the depicted axis)
    rgb_img = [new_img[i:i + 3, ...] for i in range(maximum - 3)]

    # Make sure to have correct data shape
    out_img = np.rollaxis(np.array(rgb_img), 1, 4)

    # Add the 3 lost images at the end
    out_img = np.vstack(
        (out_img, np.zeros([3] + [o for o in out_img[-1].shape])))

    return out_img


def create_mosaic_RGB(out_img1, out_img2, out_img3, maximum):

    # Load normal mosaic image
    new_img1 = create_mosaic_normal(out_img1, maximum)
    new_img2 = create_mosaic_normal(out_img2, maximum)
    new_img3 = create_mosaic_normal(out_img3, maximum)

    # Create RGB image (where red and blue mean a positive or negative shift
    # in the direction of the depicted axis)
    rgb_img = [[new_img1[i, ...], new_img2[i, ...], new_img3[i, ...]]
               for i in range(maximum)]

    # Make sure to have correct data shape
    out_img = np.rollaxis(np.array(rgb_img), 1, 4)

    # Add the 3 lost images at the end
    out_img = np.vstack(
        (out_img, np.zeros([3] + [o for o in out_img[-1].shape])))

    return out_img


def write_gif_normal(filename, size=1, fps=18, filetype='gif'):

    # Load NIfTI and put it in right shape
    out_img, maximum = reshape_image(filename, size)

    # Create output mosaic
    new_img = create_mosaic_normal(out_img, maximum)

    # Write gif file
    mimwrite(filename.replace('.nii', '.%s' % filetype), new_img,
             format=filetype, fps=int(fps * size))


def write_gif_depth(filename, size=1, fps=18, filetype='gif'):

    # Load NIfTI and put it in right shape
    out_img, maximum = reshape_image(filename, size)

    # Create output mosaic
    new_img = create_mosaic_depth(out_img, maximum)

    # Write gif file
    mimwrite(filename.replace('.nii', '_depth.%s' % filetype),
             new_img, format=filetype, fps=int(fps * size))


def write_gif_rgb(filename1, filename2, filename3, size=1, fps=18,
                  filetype='gif'):

    # Load NIfTI and put it in right shape
    out_img1, maximum1 = reshape_image(filename1, size)
    out_img2, maximum2 = reshape_image(filename2, size)
    out_img3, maximum3 = reshape_image(filename3, size)

    if maximum1 == maximum2 and maximum1 == maximum3:
        maximum = maximum1

    # Create output mosaic
    new_img = create_mosaic_RGB(out_img1, out_img2, out_img3, maximum)

    # Write gif file
    mimwrite(filename1.replace('.nii', '_rgb.%s' % filetype),
             new_img, format=filetype, fps=int(fps * size))


def write_gif_cmap(filename, size=1, fps=18, colormap='hot', filetype='gif'):

    # Load NIfTI and put it in right shape
    out_img, maximum = reshape_image(filename, size)

    # Create output mosaic
    new_img = create_mosaic_normal(out_img, maximum)

    # Transform values according to the color map
    cmap = get_cmap(colormap)

    color_transformed = [cmap(new_img[i, ...]) for i in range(maximum)]

    cmap_img = np.delete(color_transformed, 3, 3)

    # Write gif file
    mimwrite(filename.replace('.nii', '_%s.%s' % (colormap, filetype)),
             cmap_img, format=filetype, fps=int(fps * size))


if __name__ == '__main__':

    # How many frames per second
    fps = 20

    # Shows the creation of a normal grayscale gif - based on T1 MNI template
    write_gif_normal('mni_icbm152_t1_tal_nlin_asym_09c.nii', 1, fps, 'gif')

    # Shows the creation of colored gif - based on a individual brain image
    write_gif_cmap('Me_2014.nii', 1, fps, 'Spectral_r', 'gif')

    # Shows the creation of a depth gif - based on the gray matter MNI template
    write_gif_depth('mni_icbm152_gm_tal_nlin_asym_09c.nii', 1, fps, 'gif')

    # Shows the creation of a RGB gif - based on the gray matter, white matter
    # and CSF MNI template
    write_gif_rgb('mni_icbm152_gm_tal_nlin_asym_09c.nii',
                  'mni_icbm152_wm_tal_nlin_asym_09c.nii',
                  'mni_icbm152_csf_tal_nlin_asym_09c.nii',
                  1, fps, 'gif')

    # Shows how to change the size of the gif on different colored GM templates
    write_gif_normal('mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'gif')
    write_gif_cmap(
        'mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'bone', 'gif')
    write_gif_cmap(
        'mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'cubehelix', 'gif')
    write_gif_cmap(
        'mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'CMRmap', 'gif')
    write_gif_cmap(
        'mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'inferno', 'gif')
    write_gif_cmap(
        'mni_icbm152_gm_tal_nlin_asym_09c.nii', 0.5, fps, 'viridis', 'gif')
