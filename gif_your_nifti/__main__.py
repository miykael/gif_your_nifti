"""Main entry point."""

import argparse
import gif_your_nifti.config as cfg
from gif_your_nifti import core


def main():
    """Commandline interface."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',  metavar='path', nargs='+',
        help="Path to image. Multiple files can be provided."
        )
    parser.add_argument(
        '--mode', type=str, required=False,
        metavar=cfg.mode, default=cfg.mode,
        help="Gif creation mode. Available options are: 'normal', \
        'pseudocolor', 'depth', 'rgb'"
        )
    parser.add_argument(
        '--fps', type=int, required=False,
        metavar=cfg.fps, default=cfg.fps,
        help="Frames per second."
        )
    parser.add_argument(
        '--size', type=float, required=False,
        metavar=cfg.size, default=cfg.size,
        help="Image resizing factor."
        )
    parser.add_argument(
        '--cmap', type=str, required=False,
        metavar=cfg.cmap, default=cfg.cmap,
        help="Color map. Used only in combination with 'pseudocolor' mode."
        )

    args = parser.parse_args()
    cfg.mode = args.mode
    cfg.size = args.size
    cfg.fps = args.fps
    cfg.cmap = args.cmap

    if cfg.mode is 'normal':
        core.write_gif_normal(args.filename[0], cfg.size, cfg.fps)
    elif cfg.mode is 'pseudocolor':
        core.write_gif_cmap(args.filename[0], cfg.size, cfg.fps)
    elif cfg.mode is 'depth':
        core.write_gif_depth(args.filename[0], cfg.size, cfg.fps)
    elif cfg.mode is 'rgb':
        core.write_gif_rgb(args.filename[0], cfg.size, cfg.fps)
    else:
        raise ValueError("Unrecognized mode.")

    print('Finished.')

if __name__ == "__main__":
    main()
