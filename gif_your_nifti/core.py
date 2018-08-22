"""Core functions."""

import nibabel as nb
import numpy as np
from pylab import get_cmap
from imageio import mimwrite
from skimage.transform import resize


def reshape_image(filename, size=1):
    """Load and preprocess image data.

    Parameters
    ----------
    filename1: str
        Input file (eg. /john/home/image.nii.gz)
    size: float
        Image resizing factor.

    Returns
    -------
    out_img: numpy array

    """
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

    out_img /= out_img.max()  # scale image values between 0-1

    # Resize image by the following factor
    if size != 1:
        out_img = resize(out_img, [int(size * maximum)] * 3)

    maximum = int(maximum * size)

    return out_img, maximum


def create_mosaic_normal(out_img, maximum):
    """Create grayscale image.

    Parameters
    ----------
    out_img: numpy array
    maximum: int

    Returns
    -------
    new_img: numpy array

    """
    new_img = np.array(
        [np.hstack((
            np.hstack((
                np.flip(out_img[i, :, :], 1).T,
                np.flip(out_img[:, maximum - i - 1, :], 1).T)),
            np.flip(out_img[:, :, maximum - i - 1], 1).T))
         for i in range(maximum)])

    return new_img


def create_mosaic_depth(out_img, maximum):
    """Create an image with concurrent slices represented with colors.

    Parameters
    ----------
    out_img: numpy array
    maximum: int

    Returns
    -------
    new_img: numpy array

    """
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
    """Create RGB image.

    Parameters
    ----------
    out_img: numpy array
    maximum: int

    Returns
    -------
    new_img: numpy array

    """
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
    """Procedure for writing grayscale image.

    Parameters
    ----------
    filename: str
        Input file (eg. /john/home/image.nii.gz)
    size: float
        Between 0 and 1.
    fps: int
        Frames per second
    filetype: str

    """
    # Load NIfTI and put it in right shape
    out_img, maximum = reshape_image(filename, size)

    # Create output mosaic
    new_img = create_mosaic_normal(out_img, maximum)

    # Write gif file
    mimwrite(filename.replace('.nii', '.%s' % filetype), new_img,
             format=filetype, fps=int(fps * size))


def write_gif_depth(filename, size=1, fps=18, filetype='gif'):
    """Procedure for writing depth image.

    Parameters
    ----------
    filename: str
        Input file (eg. /john/home/image.nii.gz)
    size: float
        Between 0 and 1.
    fps: int
        Frames per second
    filetype: str

    """
    # Load NIfTI and put it in right shape
    out_img, maximum = reshape_image(filename, size)

    # Create output mosaic
    new_img = create_mosaic_depth(out_img, maximum)

    # Write gif file
    mimwrite(filename.replace('.nii', '_depth.%s' % filetype), new_img,
             format=filetype, fps=int(fps * size))


def write_gif_rgb(filename1, filename2, filename3, size=1, fps=18,
                  filetype='gif'):
    """Procedure for writing RGB image.

    Parameters
    ----------
    filename1: str
        Input file for red channel.
    filename2: str
        Input file for green channel.
    filename3: str
        Input file for blue channel.
    size: float
        Between 0 and 1.
    fps: int
        Frames per second
    filetype: str

    """
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
    """Procedure for writing pseudo color image.

    Parameters
    ----------
    filename1: str
        Input file (eg. /john/home/image.nii.gz)
    size: float
        Between 0 and 1.
    fps: int
        Frames per second
    colormap: str
        Name of the colormap that will be used.
    filetype: str

    """
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
